use std::collections::HashMap;

#[derive(Default)]
struct EnvScope {
    env: HashMap<String, String>,
}

enum StepBody {
    Uses,
    Run {
        env: HashMap<String, String>,
    },
}

struct Step {
    body: StepBody,
    job_env: EnvScope,
    workflow_env: EnvScope,
}

impl Step {
    fn job(&self) -> &EnvScope {
        &self.job_env
    }

    fn workflow(&self) -> &EnvScope {
        &self.workflow_env
    }

    fn env_is_static_fixed(&self, name: &str) -> bool {
        let mut envs = vec![];

        match &self.body {
            StepBody::Uses => (), // fixed: skip instead of panic
            StepBody::Run { env } => envs.push(env),
        };
        envs.push(&self.job().env);
        envs.push(&self.workflow().env);
        utils_env_is_static(name, &envs)
    }

    fn env_is_static_buggy(&self, name: &str) -> bool {
        let mut envs = vec![];

        match &self.body {
            StepBody::Uses => {
                panic!("API misuse: can't call env_is_static on a uses: step")
            }
            StepBody::Run { env } => envs.push(env),
        };
        envs.push(&self.job().env);
        envs.push(&self.workflow().env);
        utils_env_is_static(name, &envs)
    }
}

fn utils_env_is_static(name: &str, envs: &[&HashMap<String, String>]) -> bool {
    for env in envs {
        if env.contains_key(name) {
            return true;
        }
    }
    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_env_is_static_fixed_and_buggy() {
        let step_run = Step {
            body: StepBody::Run {
                env: HashMap::from([("KEY".to_string(), "VALUE".to_string())]),
            },
            job_env: EnvScope::default(),
            workflow_env: EnvScope::default(),
        };

        assert!(step_run.env_is_static_fixed("KEY"));
        assert!(step_run.env_is_static_buggy("KEY"));

        let step_uses = Step {
            body: StepBody::Uses,
            job_env: EnvScope::default(),
            workflow_env: EnvScope::default(),
        };

        // buggy version should panic on `Uses`
        let result = std::panic::catch_unwind(|| {
            step_uses.env_is_static_buggy("KEY");
        });
        assert!(result.is_err());

        // fixed version should not panic and return false
        let result = std::panic::catch_unwind(|| {
            assert!(!step_uses.env_is_static_fixed("KEY"));
        });
        assert!(result.is_ok());
    }
}
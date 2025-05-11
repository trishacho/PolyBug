
#[cfg(test)]
mod tests {
    use super::*;
    use sea_orm::DatabaseConnection;
    use std::sync::Arc;

    #[tokio::test]
    async fn returns_early_if_passive_sync_is_some_and_true() {
        let sm = subscribe_source::Model {
            passive_sync: Some(true),
            ..Default::default()
        };
        let db = DatabaseConnection::default();
        let ua = "test-user-agent";

        let result = passive_sync_one_subscribe_source_with_url(sm.clone(), ua, &db).await;
        assert!(result.is_ok());
        assert_eq!(result.unwrap().passive_sync, Some(true));
    }

    #[tokio::test]
    async fn delegates_to_sync_when_passive_sync_is_none_or_false() {
        let sm = subscribe_source::Model {
            passive_sync: Some(false),
            ..Default::default()
        };
        let db = DatabaseConnection::default();
        let ua = "test-user-agent";

        let result = passive_sync_one_subscribe_source_with_url(sm.clone(), ua, &db).await;
        assert!(result.is_ok());
    }
}

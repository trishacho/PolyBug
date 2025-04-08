use codespan_reporting::diagnostic::{Label, Severity};
use codespan_reporting::files::{Files, SimpleFiles};
use codespan_reporting::term::termcolor::Buffer;
use codespan_reporting::term::{emit, Config};
use codespan_reporting::diagnostic::LabelStyle;

pub type FileId = usize;

// dummy version of MultiLineDiagnostic for testing
#[derive(Default)]
pub struct MultiLineDiagnostic {
    pub file: String,
    pub src: String,
    pub title: String,
    pub labels: Vec<MultiLabel>,
}

#[derive(Clone)]
pub struct MultiLabel {
    pub style: LabelStyle,
    pub location: Location,
    pub label: String,
}

#[derive(Clone)]
pub struct Location {
    pub start: usize,
    pub end: usize,
}

pub fn write_diagnostic(mut buffer: &mut Buffer, d: MultiLineDiagnostic, severity: Severity) {
    let mut files = SimpleFiles::new();
    let file_id: FileId = files.add(d.file, d.src);

    let labels: Vec<Label<FileId>> = d
        .labels
        .iter()
        .map(|l| {
            Label::new(l.style, file_id, (l.location.start)..(l.location.end))
                .with_message(l.label.clone())
        })
        .collect();

    let diagnostic = codespan_reporting::diagnostic::Diagnostic::new(severity)
        .with_message(d.title)
        .with_labels(labels);

    let config = Config::default();
    emit(&mut buffer, &config, &files, &diagnostic).unwrap();
}

pub fn write_diagnostic_fixed(mut buffer: &mut Buffer, d: MultiLineDiagnostic, severity: Severity) {
    let mut files = SimpleFiles::new();
    let file_id: FileId = files.add(d.file, d.src);

    let labels: Vec<Label<FileId>> = d
        .labels
        .iter()
        .map(|l| {
            Label::new(l.style, file_id, (l.location.start)..(l.location.end - 1))
                .with_message(l.label.clone())
        })
        .collect();

    let diagnostic = codespan_reporting::diagnostic::Diagnostic::new(severity)
        .with_message(d.title)
        .with_labels(labels);

    let config = Config::default();
    emit(&mut buffer, &config, &files, &diagnostic).unwrap();
}

#[cfg(test)]
mod tests {
    use super::*;
    use codespan_reporting::term::termcolor::Buffer;

    #[test]
    fn test_write_diagnostic() {
        let file = "test.ifc".to_string();
        let src = "line1\nline2\nline3\nline4\nline5\n".to_string();
        let title = "An error occurred".to_string();

        let labels_buggy = vec![MultiLabel {
            style: LabelStyle::Primary,
            location: Location { start: 2, end: 4 },
            label: "buggy range".to_string(),
        }];

        let labels_fixed = vec![MultiLabel {
            style: LabelStyle::Primary,
            location: Location { start: 2, end: 4 },
            label: "fixed range".to_string(),
        }];

        let diag_buggy = MultiLineDiagnostic {
            file: file.clone(),
            src: src.clone(),
            title: title.clone(),
            labels: labels_buggy,
        };

        let diag_fixed = MultiLineDiagnostic {
            file,
            src,
            title,
            labels: labels_fixed,
        };

        let mut buffer_buggy = Buffer::no_color();
        write_diagnostic(&mut buffer_buggy, diag_buggy, Severity::Error);
        let output_buggy = String::from_utf8(buffer_buggy.into_inner()).unwrap();
        assert!(output_buggy.contains("buggy range"));

        let mut buffer_fixed = Buffer::no_color();
        write_diagnostic_fixed(&mut buffer_fixed, diag_fixed, Severity::Error);
        let output_fixed = String::from_utf8(buffer_fixed.into_inner()).unwrap();
        assert!(output_fixed.contains("fixed range"));
    }
}
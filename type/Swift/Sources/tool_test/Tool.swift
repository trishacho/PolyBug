enum ToolOutput {
    case text(String)
}

protocol CallableTool {
    var name: String { get }
    func action(_ input: RepeatToolInput) -> [ToolOutput]
}

struct Tool: CallableTool {
    let name: String
    private let actionClosure: (RepeatToolInput) -> [ToolOutput]
    
    init(name: String, action: @escaping (RepeatToolInput) -> [ToolOutput]) {
        self.name = name
        self.actionClosure = action
    }
    
    func action(_ input: RepeatToolInput) -> [ToolOutput] {
        return actionClosure(input)
    }
}

struct RepeatToolInput {
    let text: String
    let y: Double
}

@MainActor
let tools: [any CallableTool] = [
    Tool(name: "repeat") { (input: RepeatToolInput) in
        [.text(.init(text: input.text))]
    }
]
import XCTest

enum ToolOutput {
    case text(String)
}

struct Tool {
    let name: String
    let action: (RepeatToolInput) -> [ToolOutput]
    
    init(name: String, action: @escaping (RepeatToolInput) -> [ToolOutput]) {
        self.name = name
        self.action = action
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
    },
]


// Unit test class
class ToolTests: XCTestCase {
    
    func testToolRepeatReturnsCorrectToolOutput() {
        // Define input for the tool
        let input = RepeatToolInput(text: "Hello, world!", y: 10.0)
        
        // Access the repeat tool
        let repeatTool = tools.first { $0.name == "repeat" }
        
        // Ensure the tool was found
        XCTAssertNotNil(repeatTool, "Repeat tool should be found.")
        
        // Call the tool's action
        let result = repeatTool?.action(input)
        
        // Verify that the result is of type [ToolOutput] and contains the expected text
        XCTAssertEqual(result?.count, 1, "Tool output should contain exactly one item.")
        if let firstOutput = result?.first {
            switch firstOutput {
            case .text(let text):
                XCTAssertEqual(text, input.text, "Text should match the input.")
            }
        }
    }
}

// To run the test, use the following command in the terminal:
// swift test

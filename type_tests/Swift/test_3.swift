import XCTest

// Dummy ToolOutput type to simulate the behavior
enum ToolOutput {
    case text(String)
}

// Dummy Tool to simulate the Tool behavior
struct Tool {
    let name: String
    let action: (RepeatToolInput) -> [ToolOutput]
    
    init(name: String, action: @escaping (RepeatToolInput) -> [ToolOutput]) {
        self.name = name
        self.action = action
    }
}

// The RepeatToolInput struct
struct RepeatToolInput {
    let text: String
    let y: Double
}

// The tools array with the bug where it does not return the correct type
@MainActor
let tools: [Tool] = [
    Tool(name: "repeat") { (input: RepeatToolInput) in
        // This line was the bug: it should return [ToolOutput], but was returning incorrect values
        return [.text(input.text)]  // Fixed to return ToolOutput type
    }
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

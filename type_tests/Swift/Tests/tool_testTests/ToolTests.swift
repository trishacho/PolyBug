import XCTest
@testable import tool_test

@MainActor
final class ToolTests: XCTestCase {
    func testToolRepeatReturnsCorrectToolOutput() {
        let input = RepeatToolInput(text: "Hello, world!", y: 10.0)
        let repeatTool = tools.first { $0.name == "repeat" }
        
        XCTAssertNotNil(repeatTool, "Repeat tool should be found.")
        
        let result = repeatTool?.action(input)
        
        // This will now FAIL because of the nested .init(text:)
        if case .text(let text) = result?.first {
            XCTAssertEqual(text, input.text, "Text should match the input.")
        } else {
            XCTFail("Expected .text output")
        }
    }
}
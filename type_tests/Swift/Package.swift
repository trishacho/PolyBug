// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "tool_test",
    platforms: [
        .macOS(.v12), // Adjust based on your needs (e.g., iOS, macOS version)
    ],
    products: [
        .library(
            name: "tool_test",
            targets: ["tool_test"]
        ),
    ],
    targets: [
        // Main target (production code)
        .target(
            name: "tool_test",
            path: "Sources/tool_test"  // Explicit path to source files
        ),
        
        // Test target
        .testTarget(
            name: "tool_testTests",
            dependencies: ["tool_test"],  // Depends on the main target
            path: "Tests/tool_testTests"   // Explicit path to test files
        )
    ]
)
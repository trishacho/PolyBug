# Buggy Files

Here, you will find what to use as the LLM input for each test. You can also refer to our [Collected Bugs](https://docs.google.com/spreadsheets/d/1NFlDCCZ07WrNCaY2s5dHaMxYz9uJYhFlrrQHPb3YiNw/edit?gid=0#gid=0) spreadsheet for each code snippet we used and the corresponding GitHub repositories we sourced them from.

## Type Errors

### C++
type_tests/C++/reg.h (entire file)

### PHP
type_tests/PHP/src/Venue.php (entire file)

### Python
There are 7 test files (test_X.py) and 7 source code files. Each source code file corresponds to a certain test—use the entire file as the buggy code input. The files corresponding to each test are as follows:
* Test 1: type_tests/Python/view.py
* Test 2: type_tests/Python/slugify.py
* Test 4: type_tests/Python/apply_quadratic_attention.py
* Test 6: type_tests/Python/tag.py
* Test 7: type_tests/Python/reverse_tensor.py
* Test 8: type_tests/Python/process_retention_param.py
* Test 9: type_tests/Python/notebook.py

### Swift
The source file is Swift/Sources/tool_test/Tool.swift— use the entire file as input to the LLM.

## Logic Errors
### C/
logic_tests/C/bt_rpa_functions.c (entire file)

### C#
logic_tests/C#/EnemySpawnerTests/EnemySpawner.cs (entire file)

### C++
logic_tests/C++/numValDigits.h (entire file)

### Java
logic_tests/Java/src/main/java/TimeConverter.java (entire file)

### JavaScript
There are 4 tests, each with 1 corresponding source code file. Each source code file corresponds to a certain test—use the entire file as the buggy code input. The files corresponding to each test are as follows:
* Test 2: /logic_tests/JavaScript/helpers/registerUser.js
* Test 3: /logic_tests/JavaScript/helpers/getParentIndex.js
* Test 8: /logic_tests/JavaScript/helpers/createUser.js
* Test 10: /logic_tests/JavaScript/helpers/resolvePath.js

### PHP
/logic_tests/PHP/src/IncludeValidator.php (entire file)

### Python
/logic_tests/Python/isclose.py (entire file)

## API Misuse Errors
### C++
phy_configure_link.cpp: include/zephyr/net/phy.h (lines 198-219)

phy_get_link_state.cpp: include/zephyr/net/phy.h (lines 221-243)

### Java
FileReader.java: src/main/java/net/coobird/thumbnailator/Thumbnails.java (lines 2668-2685)

BuggyDialog.java: src/main/java/dialogs/SetAnimationStyle.java (lines 87-90)

### Python
message_handler.py: bot/handlers.py (import statements and lines 45-62)

read_file.py: utils/read_file.py (lines 33-36)

### Rust
src/models.rs (lines 441-462)

## Off-By-One Errors
### C
src/libvterm/src/pen.c (lines 275-282)

### Java
org.eclipse.jdt.debug.ui/ui/org/eclipse/jdt/internal/debug/ui/console/JavaStackTraceHyperlink.java (lines 246-299)

### Python
evaluate_stop_loop.py: src/backend/base/langflow/components/logic/loop.py (lines 53-57)

pad_to_polygon.py: vercye_ops/lai/3_analysis_LAI.py (import statements and lines 17-39)

### Rust
src/diagnostic.rs (lines 41-60)

### TypeScript
components/recipe-gallery/gallery-pagination.client.tsx (lines 79-90)

## Memory Leak Errors
### C
service/profiles/audio_interface/audio_control.c (lines 248-264)

### Java
FileReader.java: src/main/java/net/coobird/thumbnailator/Thumbnails.java (lines 2668-2685)

ListClear.java: src/main/java/utils/ListClear.java (lines 3824-3827)

### Python
message_handler.py: bot/handlers.py (import statements and lines 45-62)

read_file.py: utils/read_file.py (lines 33-36)

### TypeScript
packages/serialization/json/src/jsonParseNode.ts (lines 48-66)

## Race Condition Errors
Note: Each file is also located in the `race_condition/` directory.

### Dockerfile1
beats/libbeat/publisher/queue/memqueue/runloop.go

### Dockerfile2
utp-go/utp_utils.go

## Null Reference Errors
Each buggy code snippet can be found in the JSON file located in the `null_reference/` directory.

## Condition Errors
Note: For each test, use the **entire** source file under the `condition/` directory.

### TypeScript
assignRecipeToDate: condition/TypeScript/assignRecipeToDate.ts

deleteStudent: condition/TypeScript2/deleteStudent.ts

### C++
condition/C++/main.cpp

### PHP 
Strong-password generator: condition/PHP/strong-password-generator.php

License-bundle: condition/PHP2/onKernelResponse.php

ES-Indexing-Magento: condition/PHP3/IncludeValidator.php

### Julia
condition/Julia/run_sim_all.jl

### Rust
condition/Rust/lib.rs

### Dart
condition/Dart/movies_list_assessment.dart

### JavaScript
condition/Javascript/initSiteConfig.js

## Faulty Index Errors
Note: For each test, use the **entire** source file under the `faulty_index/` directory.

### TypeScript
deleteStudent: faulty_index/TypeScript/deleteStudent.ts

assignRecipeToDate: faulty_index/TypeScript2/assignRecipeToDate.ts

### PHP (Strong-Password Generator)
Strong-password generator: faulty_index/PHP/strong-password-generator.php

License-bundle: faulty_index/PHP2/onKernelResponse.php

ES-Indexing-Magento: faulty_index/PHP3/IncludeValidator.php

### C++
faulty_index/C++/main.cpp

### Julia
faulty_index/Julia/run_sim_all.jl

### Rust
faulty_index/Rust/lib.rs

### Dart
faulty_index/Dart/movies_list_assessment.dart
  
### JavaScript
faulty_index/Javascript/initSiteConfig.js
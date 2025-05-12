# Buggy Files

Here, you will find what to use as the LLM input for each test.

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

## Off-by-one Errors
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

## Null Reference Errors
### Dockerfile1
beats/libbeat/publisher/queue/memqueue/runloop.go

### Dockerfile2
utp-go/utp_utils.go


## Buggy Files for Condition Errors

## Below is the list of files to use as your LLM input for each “Condition errors” test. For each entry, use the **entire** source file under the `Condition errors/` directory.
---
### TypeScript

- **assignRecipeToDate mutation**  
  `Condition errors/TypeScript/assignRecipeToDate.ts`

### C++
- **Main CLI program**  
  `Condition errors/C++/main.cpp`

### PHP (Strong-Password Generator)

- **Password generator logic**  
  `Condition errors/PHP/strong-password-generator.php`

### TypeScript (deleteStudent)

- **deleteStudent utility**  
  `Condition errors/TypeScript2/deleteStudent.ts`


### Julia

- **run_sim_all simulation driver**  
  `Condition errors/Julia/run_sim_all.jl`

### PHP (License-Bundle)

- **onKernelResponse listener**  
  `Condition errors/PHP2/onKernelResponse.php`

### PHP (ES-Indexing-Magento)

- **IncludeValidator class**  
  `Condition errors/PHP3/IncludeValidator.php`

### Rust

- **passive_sync_one_subscribe_source**  
  `Condition errors/Rust/lib.rs`

### Dart

- **Empty‐history widget**  
  `Condition errors/Dart/movies_list_assessment.dart`

### JavaScript

- **initSiteConfig setup**  
  `Condition errors/Javascript/initSiteConfig.js`


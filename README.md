# PolyBug 🐛

We propose **PolyBug**, a new benchmark for evaluating Large Language Models (LLMs) on real-world debugging tasks across multiple programming languages.

We have curated 7–10 real bugs from open-source projects across a variety of bug categories—from off-by-one errors to null references—in languages such as **Python, Java, TypeScript, C/C++,** and more, for a total of 79 bugs and 3,111 lines of code.

These bugs were collected using the GitHub API from ~70 repositories and each comes with:
- A **buggy code snippet**
- The **corrected version** from the real bug-fix commit
- A **manually written unit test** that captures the bug and validates the fix

If the repository a bug comes from has developer-written tests, we have also included a **Dockerfile** that can be used to create a container that clones the repository, installs the appropriate dependencies, and runs the relevant test(s).

## Running Our Unit Tests
To run our manually written unit tests, you may follow the steps below for each type of bug after navigating to the appropriate directory using `cd` (for example, if you want to run Java tests for logic errors, run `cd logic/Java`).

### Off-By-One, API Misuse, Memory Leak, Type, and Logic Errors
#### C/C++
Note: You must have `gcc` installed.
```console 
gcc <name_of_file>.c -o <name_of_file>

./<name_of_file>
```

#### Example Usage:
```console
gcc vterm_state_set_palette_color.c -o vterm_state_set_palette_color

./vterm_state_set_palette_color
```

#### C#
Note: You must have `dotnet` installed.

```console
dotnet build
dotnet test
```

#### Swift
Note: You must have `swift` installed.

```console
swift test
```

#### Java
Note: You must have the JDK and Maven installed.

```console
mvn test
```

#### Python
Note: Creating a virtual environment is suggested, as the code requires certain dependencies. These dependencies can then be installed with `pip`.

For off-by-one errors:
```console
python -m unittest discover test
```

For API misuse, memory leak errors, logic tests, and type tests:
```console
pytest
```

#### PHP
Note: You must have PHPUnit installed.

```console
phpunit tests/<TestFile>.php
```

#### Example Usage:
```console
phpunit tests/IncludeValidatorTest.php
```

#### Rust
Note: You must have `cargo` installed.

```console
cargo test
```

#### TypeScript and JavaScript
Note: You must have Node.js installed and should run `npm install` to get all required dependencies.

```console
npm test
```

## Using a Dockerfile
To use a Dockerfile to run developer-written tests, you may follow the steps below for each type of bug.

### Off-By-One and Memory Leak Errors
To build the image:
```console
docker build -t <name_of_image> .
```

If you simply want to create a container with your image and run it (along with the tests):
```console
docker run <name_of_image>
```

Otherwise, to create a running container with the image:
```console
docker run -d --name <name_of_container> <name_of_image> tail -f /dev/null
```

To use the running container:
```console
docker exec -it <name_of_container> /bin/bash
```

Finally, if you want to edit a file in the repository (say, to replace a code snippet with some LLM-generated code that you would like to test):
```console
cd path/to/your/folder

nano <your_file> // vim <your_file> also works
```

### API Misuse Errors
Follow the same steps as off-by-one and memory leak errors to build the image, start a running container, and use the container. Then, run this command:
```console
scripts/twister -T tests/drivers -p qemu_x86 --inline-logs —verbose
```
### Race Condition Errors
Navigate to the directory containing your Dockerfile:
```console
cd <path_to_folder_containing_docker_file>
```
Build the Docker image:
```console
docker build -f <docker_file_name> -t <test_name> .
```
Finally, replace the buggy file with your fixed version:
```console
docker run --rm -v $(pwd)/<path_to_fixed_file>:/<path_to_buggy_file_in_git_repo> <test_name>
```

#### Example Usage:
For Dockerfile1:
```console
docker build -f Dockerfile1 -t beats-test .
docker run --rm -v $(pwd)/runloop.go:/app/beats/libbeat/publisher/queue/memqueue/runloop.go beats-test
```
For Dockerfile2:
```console
docker build -f Dockerfile2 -t utp-go-test .
docker run --rm -v $(pwd)/utp_utils.go:/app/utp-go/utp_utils.go utp-go-test
```

## Running the Scrapers
To run the basic scraper that obtains closed GitHub issues with fix commits in a certain category:
```console
python scraper.py <bug_type> <number_of_issues>
```

To run the scraper that obtains closed GitHub issues with fix commits to both code and test files in a certain category:
```console
python scraper_with_tests.py <bug_type> <number_of_issues>
```
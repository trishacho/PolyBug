import os
import json
import tempfile
import subprocess
import os

def run_test_from_json(json_path, fixed_function):
    with open(json_path, "r") as f:
        data = json.load(f)
    for i in range(1,11):
        test_entry = data[f"null_reference{i}"]
        buggy_code = test_entry["buggy_code"]
        raw_supporting = test_entry["supporting_classes"]
        escaped_supporting = raw_supporting.replace("{", "{{").replace("}", "}}")
        escaped_supporting = escaped_supporting.replace("{{buggy_code}}", "{buggy_code}")
        supporting_classes = escaped_supporting.format(buggy_code=fixed_function)
        test_logic = test_entry["test_logic"]

        script = f"{supporting_classes}\n\n{test_logic}"

        os.environ["PATH"] += os.pathsep + os.path.expanduser("~/.dotnet/tools")

        if(test_entry["language"] == "csharp"):
            with tempfile.NamedTemporaryFile(mode="w", suffix=".csx", delete=False) as tmp_file:
                tmp_file.write(script)
                tmp_path = tmp_file.name

            result = subprocess.run(["dotnet-script", tmp_path], capture_output=True, text=True)
        elif(test_entry["language"] == "php"):
            result = subprocess.run(
                ["php", "-r", script],
                capture_output=True,
                text=True
            )
        elif test_entry["language"] == "javascript":
            with tempfile.NamedTemporaryFile(mode="w", suffix=".js", delete=False) as tmp_file:
                tmp_file.write(script)
                tmp_path = tmp_file.name

            result = subprocess.run(["node", tmp_path], capture_output=True, text=True)

        elif test_entry["language"] == "typescript":
            with tempfile.NamedTemporaryFile(mode="w", suffix=".ts", delete=False) as tmp_file:
                tmp_file.write(script)
                tmp_path = tmp_file.name
            subprocess.run(["tsc",tmp_path])
            result = subprocess.run(["node", tmp_path.replace(".ts", ".js")], capture_output=True, text=True)
        elif test_entry["language"] == "java":
            with tempfile.TemporaryDirectory() as tmp_dir:
                java_file_path = os.path.join(tmp_dir, "TestMain.java")
                with open(java_file_path, "w") as f:
                    f.write(script)

                compile_result = subprocess.run(
                    ["javac", java_file_path],
                    capture_output=True,
                    text=True,
                    cwd=tmp_dir
                )

                if compile_result.returncode != 0:
                    print("Compilation failed.")
                    print("STDERR:")
                    print(compile_result.stderr)
                    return

                result = subprocess.run(
                    ["java", "TestMain"],
                    capture_output=True,
                    text=True,
                    cwd=tmp_dir
            )

        print("Test output:")
        print(result.stdout)
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        if result.returncode == 0:
            print("Script executed successfully.")
        else:
            print("Script failed.")



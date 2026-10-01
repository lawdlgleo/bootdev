from functions.run_python_file import run_python_file

# print(run_python_file(working_directory="calculator", file_path="main.py", args=["fart", "shitted"]))

print(run_python_file(working_directory="calculator", file_path="tests.py"))

print(run_python_file(working_directory="calculator", file_path="main.py", args=["3 + 5"]))
# print(run_python_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

print(run_python_file("calculator", "main.py"))

print(run_python_file("calculator", "../main.py"))

print(run_python_file("calculator", "nonexistent.py"))

print(run_python_file("calculator", "lorem.txt"))
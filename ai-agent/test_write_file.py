from functions.write_file import write_file

print(write_file(working_directory="calculator", file_path="lorem.txt", content="wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

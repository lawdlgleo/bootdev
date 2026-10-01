from functions.get_file_content import get_file_content


# print(get_files_info(working_directory="calculator", directory="./test_dir"))

# print(get_file_content("calculator", "./test_dir/fart_script.py"))

result_lorem: str | None = get_file_content(working_directory="calculator", file_path="./lorem.txt")




print(f"lorem.txt length: {len(result_lorem)}")
print(f"lorem.txt truncated: {'truncated' in result_lorem}")


print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))





# print(get_file_content("calculator", "./test_dir"))

# print(get_file_content("calculator", "../"))

# print(get_files_info("calculator", "pkg"))

# print(get_files_info("calculator", "/bin"))

# print(get_files_info("calculator", "../"))


# print(get_files_info(working_directory="calculator", directory="."))
# print(get_files_info(working_directory="calculator", directory="/bin"))
# print(get_files_info(working_directory="calculator", directory="../"))
# print(get_files_info(working_directory="calculator", directory="main.py"))

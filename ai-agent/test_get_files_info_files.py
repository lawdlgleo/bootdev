from functions.get_files_info import get_files_info

# print(get_files_info(working_directory="calculator", directory="./test_dir"))

print(get_files_info("calculator", "."))

print(get_files_info("calculator", "pkg"))

print(get_files_info("calculator", "/bin"))

print(get_files_info("calculator", "../"))


# print(get_files_info(working_directory="calculator", directory="."))
# print(get_files_info(working_directory="calculator", directory="/bin"))
# print(get_files_info(working_directory="calculator", directory="../"))
# print(get_files_info(working_directory="calculator", directory="main.py"))

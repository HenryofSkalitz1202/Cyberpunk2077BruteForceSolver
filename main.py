from solver import main_solver_txt, main_solver_cli, save_string_to_file
from reader import main_reader_txt

print("==================================================")
print("CYBERPUNK 2077 BREACH PROTOCOL BRUTE FORCE SOLVER")
print("==================================================")
print("Available input method")
print("1. TXT File")
print("2. Command Line Interface")
input_mode = input("Select your preferred input method: ")

str = ""
if input_mode == "1":
    file_path = input("File path: ")
    file_content = main_reader_txt(file_path)
    str += main_solver_txt(file_content[0], file_content[1], file_content[2])
elif input_mode == "2":
    str += main_solver_cli()

save_stat = input("Would you like to save the solution? (Y/N) ")
if save_stat.upper() == "Y":
    file_name = input("Input file name: ")
    print("Saving...")
    save_string_to_file(str, file_name)
    print("Solution saved. Have fun!")

elif save_stat.upper() == "N":
    print("Solution not saved. Have fun!")
    exit()


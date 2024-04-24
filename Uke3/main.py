"""
            Globally scoped imports

--------------------------------------------
Author: JorgenM
Copyright: https://github.com/JorgenMJobloop

param:
    none

return:
    main()
"""
import TextFileManagement




def main():
    file_manager = TextFileManagement.TextFileManagement("test.txt")

    print(f"Now writing new content to the file: {file_manager.filename}")

    data = "\n"
    file_manager.append_to_file(data)
    print("Content written to file!")

    print("Now writing more text, using the list type!")

    data_list = ["Current software", "File management in Python 3.12"]


    print(f"List content: {data_list}")

    file_manager.write_as_list(data_list)

    # read from the text file!
    file_content = file_manager.read_file()
    print(f"Current content in the file: {file_manager.filename}")
    print(file_content)




if __name__ == "__main__":
    main()
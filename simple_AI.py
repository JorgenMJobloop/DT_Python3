import string
import random
import time

"""
Simple "password" or text generator
"""

def main():

    RANDOM_VALUES = string.ascii_lowercase + string.ascii_uppercase + string.digits + "~@#&^_"  


    def generate_new_file():
        user_input = str(input("Do you want to create a new password text file? Y/n? ").lower())
        if user_input == "y":
            print("File created password.txt in C:/users/~ or /home/~")
            new_file = open("password.txt", "x")
            return generate_new_password()
        else:
            print("The file already exists!")
            return generate_new_password()

    def generate_new_password():
        print("\n")
        print("Generating new password...")
        print(time.ctime)

    for i in range(0, len(RANDOM_VALUES)):
        print(random.choice(RANDOM_VALUES))
        new_file = open("password.txt", "a")
        new_file.write(random.choice(RANDOM_VALUES + "\n"))

    generate_new_file()

if __name__ == "__main__":
    main()

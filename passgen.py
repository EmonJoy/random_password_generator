import secrets
import string

class string:
    pass_string = string.ascii_letters
    pass_digit = string.digits
    other = "+_*&%$#@!"

def main():
    main_func = string.pass_string + string.pass_digit + string.other
    length = input("Enter the len >>> ")
    password = ""
    for i in range(int(length)):
        a = secrets.choice(main_func)
        password +="".join(a)
    print(f"heres the password: {password}\n")
    with open("passowrd.txt", "a") as f:
        f.write(password + "\n")
    print("NOTE: The password will save as password.txt file in the current path")
if __name__ == '__main__':
    main()
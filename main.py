while(True):
    password=input("Enter your password")
    alpha=0
    digit=0
    special=0
    ln=len(password)


    for count in password:
        if count.isalpha():
            alpha=alpha+1
        elif count.isdigit():
            digit=digit+1
        else:
            special=special+1
    if (alpha>1 and digit>1 and ln>6 and special>1):
        print("Password is strong")
        break
    else:
        print("Password must contain 2 alphabets, 2 numbers,2 special characters and 8 length long")
import random

special_characters = list("!@#$%^&*()_+{}[]|;:'\",.<>?/~`")
lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

sp_input = input("how many special characters do you want: ")
lw_input = input("how many lower case letters do you want: ")
up_input = input("how many upper case letters do you want: ")

sp_password = random.choices(special_characters, k=int(sp_input))
lw_password = random.choices(lowercase_letters, k=int(lw_input))
up_password = random.choices(uppercase_letters, k=int(up_input))

sp_password_string = "".join(sp_password)
lw_password_string = "".join(lw_password)
up_password_string = "".join(up_password)

password = sp_password_string + lw_password_string + up_password_string

ls_password = list(password)
counter = 1
while counter <= 5:
    random.shuffle(ls_password)
    c = 0
    final_password = "".join(ls_password)

    print(f"{counter} = {final_password}")
    counter += 1

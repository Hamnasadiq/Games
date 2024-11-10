# Password generator code
print("Welcome to the PyPassword Generator! \nHow many letters would you like in your password?")
import string
import random
#import input number 0f alphabets
all_alphabets=string.ascii_letters
user_letters=int(input(""))
random_letters=random.sample(all_alphabets,user_letters)
#convert list into string
convert_string="".join(random_letters)
#import input number of symbols
print("How many symbols would you like? ")
user_symbol=int(input(''))
symbols=string.punctuation
random_symbol=random.sample(symbols,user_symbol)
#convert into string
convert_sym="".join(random_symbol)
#import input number of digits
print("How many numbers would you like?")
random_num=range(0,9)
user_num=int(input(""))
number_1=random.sample(random_num,user_num)
#convert into string
convert_num="".join(map(str,number_1))
#add
final_password_list = list(convert_string + convert_sym + convert_num)
# shuffle
random.shuffle(final_password_list)
final_password = "".join(final_password_list)
print(f"Your password is: {final_password}")
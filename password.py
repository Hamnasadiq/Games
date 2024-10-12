print("Welcome to the PyPassword Generator! \nHow many letters would you like in your password?")
import string
import random
all_alphabets=string.ascii_letters
user_letters=int(input(""))
random_letters=random.sample(all_alphabets,user_letters)
convert_string="".join(random_letters)
print("How many symbols would you like? ")
user_symbol=int(input(''))
symbols=string.punctuation
random_symbol=random.sample(symbols,user_symbol)
convert_sym="".join(random_symbol)
print("How many numbers would you like?")
random_num=range(0,9)
user_num=int(input(""))
number_1=random.sample(random_num,user_num)
convert_num="".join(map(str,number_1))
print(f"Your password is: {convert_string}{convert_sym}{convert_num}")
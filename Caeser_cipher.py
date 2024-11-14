print("""       
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88    """) 
print("    <---------Welcome to Caeser Cipher------->    ")
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']     
while True:
    #user inputs
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    user_real = input("Type your message:\n ").lower()
    shift_no = int(input("Type the shift number:\n "))

    #Encrypt function
    if user_input == "encode":
        encrypted_text = []
        def encrypt(real, shift):
            for letter in real:
                if letter in alphabets:
                    replace = (alphabets.index(letter) + shift) % len(alphabets)
                    encrypted_text.append(alphabets[replace])
                else:
                    encrypted_text.append(letter)  
            print("Encrypted text:\n", ''.join(encrypted_text))
        encrypt(user_real, shift_no)

    #Decrypt function
    elif user_input == "decode":
        decrypted_text = []
        def decrypt(real_2, shift_2):
            for letter in real_2:
                if letter in alphabets:
                    replace_2 = (alphabets.index(letter) - shift_2) % len(alphabets)
                    decrypted_text.append(alphabets[replace_2])
                else:
                    decrypted_text.append(letter) 
            print("Decrypted text:\n", ''.join(decrypted_text))
        decrypt(user_real, shift_no)

    # if the user wants to play again
    play_again = input("Do you want to play again? Type 'yes' or 'no':\n ").lower()
    if play_again != "yes":
        print("Goodbye! Thanks for playing.")
        break  




    


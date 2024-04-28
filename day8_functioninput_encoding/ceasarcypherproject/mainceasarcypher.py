alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from logocaesar import logo



# def encrypt(enc_text,inp_shift):
#     cipher_text = ""
#     for letter in enc_text:
#         position = alphabet.index(letter) # ini angka semua (index itu nyari urutan dari string yang ada di list)
#         new_position = position + inp_shift # ini angka semua
#         cipher_text += alphabet[new_position] # ini ubah ke string di list
#     print(f"The encoded text is {cipher_text}")

# def decrypt(dec_text,dec_shift):
#     blanktext = ""
#     for letter in dec_text:
#         position = alphabet.index(letter)
#         new_position = position - dec_shift
#         blanktext += alphabet[new_position]
#     print(f"The decoded text is {blanktext}")

# if direction == "encode":
#     encrypt(enc_text = text,inp_shift = shift)
# elif direction == "decode":
#     decrypt(dec_text = text, dec_shift = shift)

# combining and simplifying
def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + (shift_amount % 26)
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"your {cipher_direction}d text is {end_text}")

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text = text , shift_amount = shift, cipher_direction = direction)

    againorno = input("Do you want to encode/decode again? Type 'yes' or 'no'\n")
    if againorno == "no":
        should_continue = False
        print("Goodbye")

    
     


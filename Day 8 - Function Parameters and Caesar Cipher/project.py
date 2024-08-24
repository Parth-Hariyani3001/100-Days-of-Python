from logo import logo

print(logo)
isProgramRunning = True

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    cipher_text = ''
    for i in original_text:
        if i not in alphabet_list:
            cipher_text += i
            continue
        else:
            shifted_position = alphabet_list.index(i) + shift_amount
            shifted_position %= len(alphabet_list)
            cipher_text += alphabet_list[shifted_position]

    return cipher_text


def decrypt(cipher_text, shift_amount):
    original_text = ''
    for i in cipher_text:
        if i not in alphabet_list:
            original_text += i
            continue
        else:
            shifted_position = alphabet_list.index(i) - shift_amount
            original_text += alphabet_list[shifted_position]

    return original_text


# operation = input("type 'encode' to encrypt, type 'decode' to decrypt : ")
text = input("Type your message : ").lower()
shift = int(input("Type the shift number : "))


cipher_text = encrypt(text, shift)
print(cipher_text)
original_text = decrypt(cipher_text, shift)
print(original_text)

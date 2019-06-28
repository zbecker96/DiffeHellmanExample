## Diffie-Hellman-Merkle key exchange
def apply_shift(plaintext, key):
    cipher = ""
    for c in range(len(plaintext)):
        number = ord(plaintext[c])
        number += key
        cipher += chr(number)
    return cipher






def remove_shift(ciphertext, key):
    message = ""
    for c in range(len(ciphertext)):
        number = ord(ciphertext[c])
        number -= key
        message += chr(number)
    return message


def find_shared_key(private_key, public_key):
    #alice_shared_key = find_shared_key(alice_private_key, bob_public_key)

    shared_key = public_key ** private_key % public_modulus
    return shared_key


def encryptXorNumkey(message, key):
    #message = input("Enter the cipher text or plain text: ")
    #key = int(input("Enter the key for encryption or decryption: "))

    output_str = ""

    for i in range(len(message)):
        current = message[i]

        output_str += chr(ord(current) ^ key)

    print("Here's the output:" + output_str)
    return output_str

# Private Information
alice_private_key = 15
bob_private_key = 13
alice_message = "Hello Bob"

# Public Information
public_base = 3
public_modulus = 17
alice_public_key = public_base ** alice_private_key % public_modulus
bob_public_key = public_base ** bob_private_key % public_modulus


# Alice sends Bob an encrypted message
alice_shared_key = find_shared_key(alice_private_key, bob_public_key)
print(alice_shared_key)


alice_cipher = encryptXorNumkey(alice_message, alice_shared_key)

# Bob receives message and decrypts using shared key
bob_shared_key = find_shared_key(bob_private_key, alice_public_key)
print(bob_shared_key)
alice_plaintext = encryptXorNumkey(alice_cipher, bob_shared_key)

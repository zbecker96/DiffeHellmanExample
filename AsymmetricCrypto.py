## Diffie-Hellman-Merkle key exchange

def find_shared_key(private_key, public_key, public_modulus):
    #alice_shared_key = find_shared_key(alice_private_key, bob_public_key) is called
    #it goes in here and takes the public key to the power of the private key and takes a mod of that value

    shared_key = public_key ** private_key % public_modulus
    return shared_key

#modified xor stream cipher to xor message with a key
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

#alice takes the public base and raises it to her private key and then takes the mod of that value
#small values were used for explaining on the white board
alice_public_key = public_base ** alice_private_key % public_modulus

#bob then does the same thing with his private key
bob_public_key = public_base ** bob_private_key % public_modulus


# Alice sends Bob an encrypted message
alice_shared_key = find_shared_key(alice_private_key, bob_public_key, public_modulus)
print(alice_shared_key)
bob_shared_key = find_shared_key(bob_private_key, alice_public_key)
print(bob_shared_key)


alice_cipher = encryptXorNumkey(alice_message, alice_shared_key)

# Bob receives message and decrypts using shared key
decrypted_alice_to_bob_msg = encryptXorNumkey(alice_cipher, bob_shared_key)

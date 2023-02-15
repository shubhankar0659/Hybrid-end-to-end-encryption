import rsa_tools
import json


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord((char)), key, n) for char in str(plaintext)]
    # Return the array of bytes
    return cipher



def rsa_encr_main():
    '''
    Detect if the script is being run directly by the user
    '''

    # p = 17
    # q = 19
    p = int(input("Enter a random prime number: "))
    q = int(input("Enter another prime number: "))
    # print(" - Generating your RSA public / private key-pairs now . . .")

    public, private = rsa_tools.generate_key_pair(p, q)


    message = ''

    # Opening JSON file
    with open('key.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
        message = str(json_object['aes_key'])

    # print(" -  Encrypting your AES key")
    encrypted_msg = encrypt(public, message)


    ####### WRITING THE ENCRYPTED AES KEY ########
    # Data to be written
    dictionary = {
        "encr_aes_key": encrypted_msg,
        "public_rsa_key": public,
        "private_rsa_key": private
    }
    print("RSA Public Key: "+ str(public))
    
    print("RSA Private Key: "+ str(private))

    print("Encrypted AES Key: "+ str(encrypted_msg))

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("key.json", "w") as outfile:
        outfile.write(json_object)    






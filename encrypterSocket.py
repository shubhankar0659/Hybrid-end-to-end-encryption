import aes_encr
import aes_decr
import aes_tools
import rsa_main_encr
import rsa_main_decr
import json

# driver code :
def encrypter(plain_text):

    # cipher_key = '1234567890123456'
    cipher_key = input("Enter 16bit AES Key: ")
    # print("Encrypting the string using AES: ")    
    cipher_text = aes_encr.aesEncrypt(plain_text,cipher_key)
    print("The encrypted text is : {}".format(cipher_text))
    print(" ")
    print("AES Key: " + cipher_key)
    ##    sending the AES key to RSA  ############################
     
    # Data to be written
    dictionary = {
        "aes_key": cipher_key,
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("key.json", "w") as outfile:
        outfile.write(json_object)    

    rsa_main_encr.rsa_encr_main()

    # Data to be written
    dictionary = {
        "ENCR_MSG": cipher_text,
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("encr_msg.json", "w") as outfile:
        outfile.write(json_object) 

    return cipher_text




def decrypter(cipher_text):
    rsa_main_decr.rsa_decr()
    # Opening JSON file
    with open('key.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
        processed_cipher_key = str(json_object['decr_aes_key'])
    
    with open('encr_msg.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
        cipher_text = str(json_object['ENCR_MSG'])
    

    # print("Decrypting : ")
    decrypted_text = aes_decr.aesDecrypt(cipher_text,processed_cipher_key)
    print("The decrpyted text is : {}".format(decrypted_text))


    return decrypted_text
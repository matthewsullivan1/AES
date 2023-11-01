from Block import Block
from Aes import Aes
from utils import Sbox, InvSbox, Rcon, KeyExpansion, display

if __name__ == '__main__':
    key = [0x2B,0x7E,0x15,0x16,
           0x28,0xAE,0xD2,0xA6,
           0xAB,0xF7,0x15,0x88,
           0x09,0xCF,0x4F,0x3C]
    
    
    state = [[0x32, 0x88, 0x31, 0xE0],
             [0x43, 0x5A, 0x31, 0x37],
             [0xF6, 0x30, 0x98, 0x07],
             [0xA8, 0x8D, 0xA2, 0x34]]

    #expanded_key = KeyExpansion(key)

    
    
    #test = Aes("C:/Users/18163/Desktop/Github AES/AES/data.txt", "C:/Users/18163/Desktop/Github AES/AES/output.txt", key)
    

    '''
    with open("C:/Users/18163/Desktop/Github AES/AES/data.txt", "rb") as file:
        byte = file.read(1)
        print(byte)
    
    test.Encrypt()
    for word in test.state:
        for byte in word:
            print(hex(byte))
        print("\n")

    for i in range(1,10):
        print(i)
    '''

    # Initialize an empty 4x4 state matrix filled with zeros
    state = [[0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00]]

    with open('C:/Users/18163/Desktop/Github AES/AES/data.txt', 'r') as fp:
        hex_list = ["{:02x}".format(ord(c)) for c in fp.read()]

    print(hex_list)

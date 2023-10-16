import binascii
from Block import Block



if __name__ == '__main__':


    block_size = 16

    with open("data.txt", 'rb') as file:
        plaintext = file.read()

    # Break the plaintext into 16-byte blocks
    blocks = [plaintext[i:i+block_size] for i in range(0, len(plaintext), block_size)]

    test_block = Block(blocks)
    print(test_block.getData())
    print(test_block.getPadAmount())
    print(test_block.getWord0())

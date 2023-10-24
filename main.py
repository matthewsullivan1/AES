import binascii
from Block import Block
from Aes import Aes
from utils import Sbox, InvSbox, Rcon

def KeyExpansion(key, Nk=4, Nb=4, Nr=10) -> list:
        #Generates 4*(Nr + 1) words
        #Linear array of words, denoted w[i], 0 <= i <= 4*(Nr + 1)

        # 44 words for 128 bit key
    w = [0] * (4 * (Nr + 1))

        # Copying initial key to first four words of expanded key
    w[0] = key[0:4]
    w[1] = key[4:8]
    w[2] = key[8:12]
    w[3] = key[12:16]

    i = Nk
    while(i < Nb*(Nr+1)):
        temp = w[i-1]     
        if i % Nk == 0:
            temp = SubWord(RotWord(temp))
            temp[0] ^= Rcon[(i//Nk)]

        #for larger keys
        #elif(Nk > 6 and i % Nk == 4):
            #temp = self.SubWord(temp)

        w[i] = [w[i-Nk][j] ^ temp[j] for j in range(4)]
        i += 1
    return w

def RotWord(word):
    #[a0,a1,a2,a3] -> [a1,a2,a3,a0]
    return word[1:] + word[:1]

def SubWord(word):
    return [Sbox[word[0]], Sbox[word[1]], Sbox[word[2]], Sbox[word[3]]]





if __name__ == '__main__':
    key = [0x2b,0x7e,0x15,0x16,
           0x28,0xae,0xd2,0xa6,
           0xab,0xf7,0x15,0x88,
           0x09,0xcf,0x4f,0x3c]
    
    
    state = [[0x32, 0x88, 0x31, 0xe0],
             [0x43, 0x5a, 0x31, 0x37],
             [0xf6, 0x30, 0x98, 0x07],
             [0xa8, 0x8d, 0xa2, 0x34]]

    expanded_key = KeyExpansion(key)

    test = Aes(state, expanded_key)
    test.Encrypt()
    #print(test.state)

    ss = [[0]*4]*4
    print(ss)

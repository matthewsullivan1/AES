from Block import Block
from utils import Sbox, InvSbox, Rcon, GMul
import binascii

class Aes:
    def __init__(self, state, expanded_key):
        self.state = state
        self.key = expanded_key #44 words

    def Encrypt(self):
        self._Encrypt()

    def _Encrypt(self) -> list:
        
        round = 0
        self.AddRoundKey(round)
        round += 1
        for i in range(9):
            #print(self.state)
            self.SubBytes()
            self.ShiftRows()
            self.MixColumns()
            self.AddRoundKey(round)
            round += 1
        self.SubBytes()
        self.ShiftRows()
        self.AddRoundKey(round)
            
    def AddRoundKey(self, round):
        for i in range(4):
            for j in range(4):
                self.state[i][j] ^= self.key[(round * 4)+ i][j]
    def SubBytes(self):
        for i in range(4):
            for j in range(4):
                self.state[i][j] = Sbox[self.state[i][j]]

    def ShiftRows(self):
        self.state[1] = self.state[1][1:] + self.state[1][:1]
        self.state[2] = self.state[2][2:] + self.state[2][:2]
        self.state[3] = self.state[3][3:] + self.state[3][:3]

    def MixColumns(self):
        return
        ss = [[0]*4]*4

        for i in range(4):
            ss[0][i] = (GMul(0x02, self.state[0][i]) ^ GMul(0x03, self.state[1][i]) ^ self.state[2][i] ^ self.state[3][i])
            ss[1][i] = (self.state[0][i] ^ GMul(0x02, self.state[1][i]) ^ GMul(0x03, self.state[2][i]) ^ self.state[3][i])
            ss[2][i] = (self.state[0][i] ^ self.state[1][i] ^ GMul(0x02, self.state[2][i]) ^ GMul(0x03, self.state[3][i]))
            ss[3][i] = (GMul(0x03, self.state[0][i]) ^ self.state[1][i] ^ self.state[2][i] ^ GMul(0x02, self.state[3][i]))

        print(ss)
        print(self.state)
        for i in range(4):
            for j in range(4):
                self.state[i][j] = ss[i][j]

    def mix_column(self, column):
        pass


    def Decrypt():
        pass


    
    '''
    test = Aes(key, "test.txt")

    #rk = test.GetRoundKey(0)
    for word in test.expanded_key:
        for byte in word:
            print(hex(byte))
        print("\n")
    
# Iterate through the 44 lists in the expanded key
    for i, key_list in enumerate(test.expanded_key):
        print(f"Word {i}:")
    
        # Iterate through the words in each list and print them in hex format
        for word in key_list:
            print(f"{hex(word)}", end=' ')
    
        print("\n")  # Move to the next line for the next key

    '''

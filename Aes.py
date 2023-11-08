from utils import Sbox, InvSbox, Rcon, galois_mult, KeyExpansion, toMatrix, display, writeToFile, pad

class Aes:
    def __init__(self, input_file, output_file, key, mode=None, Nk=4, Nb=4, Nr=10):
        self.key = KeyExpansion(key)
        
        if not mode:
            while (mode != 'd') and (mode != 'e'):
                mode = str(input("Enter mode (e -> encrypt, d -> decrypt): "))
        if mode == 'd':
            temp = input_file
            input_file = output_file
            output_file = temp

        '''
        Reads 16 bytes at a time from input file, pads with 0x23 if the length is less than 16 
        bytes, calls Encrypt() / Decrypt() based on the mode until the entire file is read
        '''
        with open(input_file, "rb") as file:
            while True:
                byte_array = list(file.read(16))

                if not byte_array:
                    break                    
                pad(byte_array)

                state = [[0 for _ in range(4)] for _ in range(4)]
                toMatrix(byte_array, state)
                    
                self.state = state
                if mode == 'e':  
                    self.Encrypt()
                else: 
                    self.Decrypt()
                
                writeToFile(state, output_file)

    def Encrypt(self):
        # Initial round
        self.AddRoundKey(0)

        # Intermediate rounds
        for i in range(1,10):
            self.SubBytes()
            self.ShiftRows()
            self.MixColumns()
            self.AddRoundKey(i)
        
        # Final round
        self.SubBytes()
        self.ShiftRows()
        self.AddRoundKey(10)
                
    def AddRoundKey(self, round):
        for i in range(4):
            for j in range(4):
                self.state[i][j] ^= self.key[(round * 4)+ j][i]
    def SubBytes(self):
        for i in range(4):
            for j in range(4):
                self.state[i][j] = Sbox[self.state[i][j]]
    def InvSubBytes(self):
        for i in range(4):
            for j in range(4):
                self.state[i][j] = InvSbox[self.state[i][j]]

    def ShiftRows(self):
        self.state[1] = self.state[1][1:] + self.state[1][:1]
        self.state[2] = self.state[2][2:] + self.state[2][:2]
        self.state[3] = self.state[3][3:] + self.state[3][:3]

    def MixColumns(self):
        # Transpose state so that each column is a row
        # Can then pass self.state[i] -> MixColumn instead of extracting the column first
        # Transpose again after to restore 
        self.state = list(map(list, zip(*self.state)))
        
        for i in range(4):
            temp = self.MixColumn(self.state[i])
            self.state[i] = temp
        
        self.state = list(map(list, zip(*self.state)))

    def MixColumn(self, column):
        temp = column # Temp column for operations
        column = [0x00] * 4 # Set old column data back to 0 

        column[0] = galois_mult(temp[0], 2) ^ galois_mult(temp[1], 3) ^ \
                galois_mult(temp[2], 1) ^ galois_mult(temp[3], 1)
        column[1] = galois_mult(temp[0], 1) ^ galois_mult(temp[1], 2) ^ \
                galois_mult(temp[2], 3) ^ galois_mult(temp[3], 1)
        column[2] = galois_mult(temp[0], 1) ^ galois_mult(temp[1], 1) ^ \
                galois_mult(temp[2], 2) ^ galois_mult(temp[3], 3)
        column[3] = galois_mult(temp[0], 3) ^ galois_mult(temp[1], 1) ^ \
                galois_mult(temp[2], 1) ^ galois_mult(temp[3], 2)
        
        return column

    def Decrypt(self):
        # Initial round
        self.AddRoundKey(10)
        self.InvShiftRows()
        self.InvSubBytes()

        # Intermediate rounds
        for i in range(9, 0, -1):
            self.AddRoundKey(i)
            self.InvMixColumns()
            self.InvShiftRows()
            self.InvSubBytes()

        # Final round
        self.AddRoundKey(0)

    def InvShiftRows(self):
        self.state[1] = self.state[1][-1:] + self.state[1][:-1]
        self.state[2] = self.state[2][-2:] + self.state[2][:-2]
        self.state[3] = self.state[3][-3:] + self.state[3][:-3]

    def InvMixColumns(self):
        self.state = list(map(list, zip(*self.state)))
        
        for i in range(4):
            temp = self.InvMixColumn(self.state[i])
            self.state[i] = temp
        
        self.state = list(map(list, zip(*self.state)))

    def InvMixColumn(self, column):
        temp = column # Temp column for operations
        column = [0x00] * 4 # Set old data back to 0 

        column[0] = galois_mult(temp[0], 14) ^ galois_mult(temp[1], 11) ^ \
                galois_mult(temp[2], 13) ^ galois_mult(temp[3], 9)
        column[1] = galois_mult(temp[0], 9) ^ galois_mult(temp[1], 14) ^ \
                galois_mult(temp[2], 11) ^ galois_mult(temp[3], 13)
        column[2] = galois_mult(temp[0], 13) ^ galois_mult(temp[1], 9) ^ \
                galois_mult(temp[2], 14) ^ galois_mult(temp[3], 11)
        column[3] = galois_mult(temp[0], 11) ^ galois_mult(temp[1], 13) ^ \
                galois_mult(temp[2], 9) ^ galois_mult(temp[3], 14)
        
        return column

from utils import Sbox, InvSbox, Rcon, galois_mult, KeyExpansion, toMatrix, display

class Aes:
    def __init__(self, input, output, key, Nk=4, Nb=4, Nr=10):
        self.key = KeyExpansion(key)

        '''
        with open(input, 'r') as f:
            with open(output, 'wb') as output_f:
                plaintext = f.read(16)
                state = toMatrix(plaintext)  
                self.Encrypt(state)              
        '''

                #test = Block(state)
        # Reading from the input text file in text mode
        '''
        with open(input, "r") as input_file:
            text_data = input_file.read(16)

        # Encoding the text to bytes using UTF-8
            byte_data = text_data.encode('utf-8')
            state = toMatrix(byte_data)
        '''

        # assume this is coming from the input file
        '''
        state = [[0x32, 0x88, 0x31, 0xE0],
            [0x43, 0x5A, 0x31, 0x37],
            [0xF6, 0x30, 0x98, 0x07],
            [0xA8, 0x8D, 0xA2, 0x34]]
        '''













        
        self.state = state
        self.Encrypt()


        #toMatrix(byte_data)

        # Perform AES encryption on 'byte_data'

        # Decoding the byte data back to text using UTF-8 after decryption
        #decrypted_text = byte_data.decode('utf-8')

        # Writing the decrypted text to the output text file
        #with open(output, "w") as output_file:
            #output_file.write(decrypted_text)


    def Encrypt(self):
        self.AddRoundKey(0)
        for i in range(1,10):
            self.SubBytes()
            self.ShiftRows()
            self.MixColumns()
            self.AddRoundKey(i)
        self.SubBytes()
        self.ShiftRows()
        self.AddRoundKey(10)
        
        display(self.state)
        
    def AddRoundKey(self, round):
        for i in range(4):
            for j in range(4):
                self.state[i][j] ^= self.key[(round * 4)+ j][i]

    def SubBytes(self):
        for i in range(4):
            for j in range(4):
                self.state[i][j] = Sbox[self.state[i][j]]

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
        temp = column # Store temporary column for operations
        column = [0x00] * 4 #not sure why this fixed MixColumns() but im glad i thought to try it 

        column[0] = galois_mult(temp[0], 2) ^ galois_mult(temp[1], 3) ^ \
                galois_mult(temp[2], 1) ^ galois_mult(temp[3], 1)
        column[1] = galois_mult(temp[0], 1) ^ galois_mult(temp[1], 2) ^ \
                galois_mult(temp[2], 3) ^ galois_mult(temp[3], 1)
        column[2] = galois_mult(temp[0], 1) ^ galois_mult(temp[1], 1) ^ \
                galois_mult(temp[2], 2) ^ galois_mult(temp[3], 3)
        column[3] = galois_mult(temp[0], 3) ^ galois_mult(temp[1], 1) ^ \
                galois_mult(temp[2], 1) ^ galois_mult(temp[3], 2)
        
        return column


    def Decrypt():
        pass

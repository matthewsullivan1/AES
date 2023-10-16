class Block:
    def __init__(self, data):
        self.__pad_amount = 16-len(data[0])
        self.__data = []
        self.w0 = []
        self.w1 = []
        self.w2 = []
        self.w3 = []
        test = []


        for byte in data[0]:
            self.__data.append(byte)
        for zero in range(self.__pad_amount):
            self.__data.append(48)
        for byte in self.__data:
            print(byte)

        print(self.__data[0])
        '''
               w0    w1    w2      w3
              d[0], d[4], d[8],  d[12]
              d[1], d[5], d[9],  d[13]
              d[2], d[6], d[10], d[14]
              d[3], d[7], d[11], d[15]
        '''

        for i in range(4):
            self.w0.append(self.__data[i])
            self.w1.append(self.__data[i + 4])
            self.w2.append(self.__data[i + 8])
            self.w3.append(self.__data[i + 12])
   
        
        

    def getData(self):
        return self.__data
    def getPadAmount(self):
        return self.__pad_amount
    def getWord0(self):
        return self.w0
    def getWord1(self):
        return self.w1
    def getWord2(self):
        return self.w2
    def getWord3(self):
        return self.w3
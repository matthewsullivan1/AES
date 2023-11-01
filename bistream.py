def toMatrix(byte_array, state):
    for i in range(4):
        state[i][0] = byte_array[i]
        state[i][1] = byte_array[i + 4]
        state[i][2] = byte_array[i + 8]
        state[i][3] = byte_array[i + 12]

def write_matrix_to_file(matrix, output_file_path):
    transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
    byte_list = [byte for row in transposed_matrix for byte in row]
    byte_data = bytes(byte_list)

    print(byte_data)
    # utf8_string = byte_data.encode('utf-8')
    # print(utf8_string)


    with open(output_file_path, "ab") as output_file:
        output_file.write(byte_data)
    
def pad(byte_array):
    while len(byte_array) < 16:
        byte_array.append(0x23)

if __name__ == '__main__':
    with open("data.txt", "rb") as file:
        while True:
            byte_array = list(file.read(16))

            if not byte_array:
                break

            # Pad the byte array to 16 bytes if needed
            pad(byte_array)

            state = [[0 for _ in range(4)] for _ in range(4)]
            toMatrix(byte_array, state)

            # Process the state matrix as needed

            # Define the output file path based on your requirements
            output_file_path = "output.txt"

            write_matrix_to_file(state, output_file_path)

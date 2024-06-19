import sys

def binary_to_hex(bin):
    bin_to_hex = {
            "0000" : "0",
            "0001" : "1",
            "0010" : "2",
            "0011" : "3",
            "0100" : "4",
            "0101" : "5",
            "0110" : "6",
            "0111" : "7",
            "1000" : "8",
            "1001" : "9",
            "1010" : "A",
            "1011" : "B",
            "1100" : "C",
            "1101" : "D",
            "1110" : "E",
            "1111" : "F"
            }

    hex = bin_to_hex[bin[0:4]] + bin_to_hex[bin[4:8]] + bin_to_hex[bin[8:12]] + bin_to_hex[bin[12:16]] 

    return hex



input_file = open(sys.argv[1], "r")

for instruction in input_file.readlines():
    instruction_splitted = instruction.split(" ")

    instruction_splitted = [elem for elem in instruction_splitted if elem != ""]
    instruction_splitted = [elem.upper() for elem in instruction_splitted]

    dec_to_hex = ["000", "001", "010", "011", "100", "101", "110", "111"]

    instruction_decoded = ""

    decoded = False

    match (instruction_splitted[0]):
        case "MVRV":
            instruction_decoded += "1111" + dec_to_hex[int(instruction_splitted[1][1])] + dec_to_hex[int(instruction_splitted[2][1])] + "011" + dec_to_hex[int(instruction_splitted[3])]
            decoded = True
        case "MVVR":
            instruction_decoded += "1111" + dec_to_hex[int(instruction_splitted[1][1])] + dec_to_hex[int(instruction_splitted[2][1])] + "010" + dec_to_hex[int(instruction_splitted[3])]
            decoded = True
        case "MULV":
            instruction_decoded += "1010" + dec_to_hex[int(instruction_splitted[1][1])] + dec_to_hex[int(instruction_splitted[2][1])] + "001" + dec_to_hex[int(instruction_splitted[3][1])]
            decoded = True
        case "MULHV":
            instruction_decoded += "1010" + dec_to_hex[int(instruction_splitted[1][1])] + dec_to_hex[int(instruction_splitted[2][1])] + "010" + dec_to_hex[int(instruction_splitted[3][1])]
            decoded = True
        case "MULHUV":
            instruction_decoded += "1010" + dec_to_hex[int(instruction_splitted[1][1])] + dec_to_hex[int(instruction_splitted[2][1])] + "011" + dec_to_hex[int(instruction_splitted[3][1])]
            decoded = True
        case "ADDV":
            instruction_decoded += "1010" + dec_to_hex[int(instruction_splitted[1][1])] + dec_to_hex[int(instruction_splitted[2][1])] + "100" + dec_to_hex[int(instruction_splitted[3][1])]
            decoded = True
        case "SUBV":
            instruction_decoded += "1010" + dec_to_hex[int(instruction_splitted[1][1])] + dec_to_hex[int(instruction_splitted[2][1])] + "101" + dec_to_hex[int(instruction_splitted[3][1])]
            decoded = True
        case "SHAV":
            instruction_decoded += "1010" + dec_to_hex[int(instruction_splitted[1][1])] + dec_to_hex[int(instruction_splitted[2][1])] + "110" + dec_to_hex[int(instruction_splitted[3][1])]
            decoded = True
        case "SHLV":
            instruction_decoded += "1010" + dec_to_hex[int(instruction_splitted[1][1])] + dec_to_hex[int(instruction_splitted[2][1])] + "111" + dec_to_hex[int(instruction_splitted[3][1])]
            decoded = True
        case "STV":
            instruction_decoded += "1111" + dec_to_hex[int(instruction_splitted[2][1])] + dec_to_hex[int(instruction_splitted[1][3])] + "001" + dec_to_hex[int(instruction_splitted[1][0])]
            decoded = True
        case "LDV":
            instruction_decoded += "1111" + dec_to_hex[int(instruction_splitted[1][1])] + dec_to_hex[int(instruction_splitted[2][3])] + "010" + dec_to_hex[int(instruction_splitted[2][0])]
            decoded = True

    if decoded:
        print(".word 0x" + str(binary_to_hex(instruction_decoded)))
    else:
        if instruction[:-1] != "":
            print(instruction[:-1])

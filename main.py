#A1Z26 Encoder/Decoder

originalAlph = "abcdefghijklmnopqrstuvwxyz"
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]

def encode(input):
    result = ""
    for letter in input:
        if letter in originalAlph:
            result += str(originalAlph.index(letter)+1) + " "
        elif letter == " ":
            result += " "
        else:
            result += letter
    print(result)

def decode(input):
    result = ""
    input = str(input)
    input = input.split(" ")
    for string in input:
        if string in num:
            result += str(originalAlph[int(string) - 1])
        elif string == "":
            result += " "
        else:
            result += string
    print(result)

print("Welcome to A1Z26 Encoder/Decoder by Kamp")
choice = input("Do you want to encode or decode?\n")
if choice == "encode":
    rawInput = input("Enter your word\n")
    encode(rawInput)
elif choice == "decode":
    rawInput = input("Enter your numbers\n")
    decode(rawInput)

import encryption
import decryption
inputfile = input("Введіть назву вхідного файлу: ")
outputfile = input("Введіть назву вихідного файлу: ")
inputfilename = inputfile + ".txt"
outputfilename = outputfile + ".txt"
with open(inputfilename, "r") as inputfile1:
    inputtext = inputfile1.read()
choice1 = input("Введіть операцію (шифрування - парне число; дешифрування - непарне): ")
if int(choice1) % 2 == 0:
    with open(outputfilename, "w") as outputfile1:
        outputfile1.write(encryption.lab6encryption(inputtext))
else:
    with open(outputfilename, "w") as outputfile1:
        outputfile1.write(decryption.lab6decryption(inputtext))
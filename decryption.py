def lab6decryption(Text):
    polynomiallength = input(f"Введіть довжину (не більше 64):\n")
    if int(polynomiallength) >= 64:
        print("PolynomialLengthError!")
        exit()
    polynomial = []
    print(f"Введіть поліном (кожне значення не більше 63):")
    for i in range (int(polynomiallength)):
        polynomial.append(input())
    Keyreg = input(f"Введіть ключ:\n")
    if int(Keyreg) >= 18446744073709551616:
        print("KeyregError!")
        exit()
    resultbin = ""
    #converting polynomial array
    for i in range (len(polynomial)):
        polynomial[i] = int(polynomial[i])
    polynomial = sorted(polynomial)
    print(f"polynomial array  = {polynomial}")
    truepolynomial = []
    for i in range (len(polynomial)):
        truepolynomial.append(63 - polynomial[i])
    #checking key for compatibility
    if len(bin(int(Keyreg))[2:]) < 64:
        m = 64 - len(bin(int(Keyreg))[2:])
        n = ""
        for i in range(m):
            n += "0"
        n += bin(int(Keyreg))[2:]
        fullbinkeyreg = n
    else:
        fullbinkeyreg = bin(int(Keyreg))[2:]
    print(f"bin keyreg = {fullbinkeyreg}")
    #converting text from hex to bin
    fraction = int(len(Text) / 3)
    bintext = ""
    fullbit = ""
    for i in range (fraction):
        hex1 = Text[i * 3] + Text[i * 3 + 1]
        print(f"hex = {hex1}")
        bit = bin(int(hex1, 16))[2:]
        if len(bit) < 8:
            m = 8 - len(bit)
            n = ""
            for i in range(m):
                n += "0"
            n += bit
            fullbit = n
        else:
            fullbit = bit
        bintext += fullbit
    print(f"bintext\n{bintext}")
    print(len(bintext))
    #actual encryption
    for i in range (len(bintext)):
        resultbin += bin(int(bintext[i], 2) ^ int(fullbinkeyreg[63], 2))[2:]
        newregvalue = ""
        for j in range (len(truepolynomial)):
            if j == 0:
                newregvalue = fullbinkeyreg[truepolynomial[j]]
            else:
                newregvalue = bin(int(newregvalue, 2) ^ int(fullbinkeyreg[truepolynomial[j]], 2))[2:]
        fullbinkeyreg = newregvalue + fullbinkeyreg[:63]
    print(f"resultbin\n{resultbin}")
    #converting text from bin to ascii
    decryptedtext = ""
    fraction = int(len(resultbin) / 8)
    for i in range (fraction):
        letter = ""
        for j in range (8):
            letter += resultbin[i * 8 + j]
        decryptedtext += chr(int(letter, 2))
    print(f"decrypted text is \n{decryptedtext}")
    return(decryptedtext)
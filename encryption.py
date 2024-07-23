def lab6encryption(Text):
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
    #converting text from ascii to bin
    bintext = ""
    for i in range (len(Text)):
        binletter = bin(ord(Text[i]))[2:]
        fullbinletter = ""
        if len(binletter) < 8:
            m = 8 - len(binletter)
            n = ""
            for j in range(m):
                n += "0"
            n += binletter
            fullbinletter = n
        else:
            fullbinletter = binletter
        bintext += fullbinletter
    print(f"bintext\n{bintext}")
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
    #converting text form bin to hex
    amount = int(len(resultbin) / 8)
    hexresulttext = ""
    for i in range (amount):
        binhex = ""
        for j in range (8):
            binhex += resultbin[i * 8 + j]
        print(binhex)
        hexoutputtext = hex(int(binhex, 2))[2:]
        fullhex1 = ""
        if len(hexoutputtext) < 2:
            m = 2 - len(hexoutputtext)
            n = ""
            for i in range(m):
                n += "0"
            n += hexoutputtext
            fullhex1 = n
        else:
            fullhex1 = hexoutputtext
        print(fullhex1)
        hexresulttext += fullhex1 + " "
    print(hexresulttext)
    return (hexresulttext)
def inputALF():
    s = input("Выбери язык (RU, ru, EN, en):")
    if s == "RU" or s == "ru":
        with open("Alphabets/Rus.txt", "r", encoding="utf-8") as file:
            if s == "ru":
                return list(file.readline()[:-1])
            else:
                file.readline()
                return list(file.readline())
    else:
        with open("Alphabets/En.txt", "r", encoding="utf-8") as file:
            if s == "en":
                return list(file.readline()[:-1])
            else:
                file.readline()
                return list(file.readline())


def PrimaryKey(ciphertext, alf):
    freq = dict()
    for i in range(len(alf)):
        freq[alf[i]] = 0
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        if letter in alf:
            freq[letter] = freq[letter] + 1
    freq = {a: b for a, b in sorted(freq.items(), key=lambda item: item[1])}
    key = list(reversed(freq.keys()))
    return key


def Encrypt(ciphertext, key, alf):
    result = []
    for i in ciphertext:
        if i in alf:
            ind = key.index(i)
            result.append(alf[ind])
        else:
            result.append(' ')
    return result


def inputFreqBi(alf):
    refBi = dict()
    if alf[0].upper()=='А':

        with open("ReferenceFrequencies/RefFreqRusВigrams3.txt", "r", encoding="utf-8") as file:
            for line in file:
                str = line.split(':')
                if alf[0].isupper():
                    refBi[str[0].upper()] = float(str[1][:-1])
                else:
                    refBi[str[0]] = float(str[1][:-1])
    if alf[0].upper()=='A':
        with open("ReferenceFrequencies/RefFreqEngBigrams.txt", "r", encoding="utf-8") as file:
            for line in file:
                str = line.split(':')
                if alf[0].isupper():
                    refBi[str[0].upper()] = float(str[1][:-1])
                else:
                    refBi[str[0]] = float(str[1][:-1])
    return refBi


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def freqBiText(ciphertext, alf):
    bi = dict()
    sum = 0
    for i in range(len(ciphertext) - 1):
        a = ciphertext[i]
        b = ciphertext[i + 1]
        if a in alf and b in alf:
            x = a + b
            bi[x] = bi.setdefault(x, 0) + 1
            sum += 1
    for i in bi.keys():
        bi[i] = float(toFixed(bi[i] / sum * 100, 5))
    bi = {a: b for a, b in sorted(bi.items(), key=lambda item: item[1])}
    return bi


def calcCoef(BigramsCipherText, freqBigrams):
    coef = 0
    for i in BigramsCipherText.keys():
        coef += BigramsCipherText[i] * freqBigrams[i]
    return coef


def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        ciphertext = file.read()
        alf = inputALF()
        freqBigrams = inputFreqBi(alf)
        BigramsCipherText = freqBiText(ciphertext, alf)
        key = PrimaryKey(ciphertext, alf)
        coef = calcCoef(BigramsCipherText, freqBigrams)
        step = 1
        ans = dict()
        while True:
            fl = False
            for i in range(len(alf)):
                if i + step >= len(alf):
                    break
                key[i], key[i + step] = key[i + step], key[i]
                new_ciphertext = Encrypt(ciphertext, key, alf)
                new_BigramsCipherText = freqBiText(new_ciphertext, alf)
                new_coef = calcCoef(new_BigramsCipherText, freqBigrams)
                if new_coef > coef:
                    fl = True
                    coef = new_coef
                    ans[coef] = ''.join(new_ciphertext)
                    step = 1
                    break
                else:
                    key[i], key[i + step] = key[i + step], key[i]
            if fl == False:
                step += 1
                if step >= len(alf) - 1:
                    break
        ans = {a: b for a, b in sorted(ans.items(), key=lambda item: item[0])}
        print(f"{max(ans)}:{ans[max(ans)]}")


main()

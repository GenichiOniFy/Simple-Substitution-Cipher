
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


with open("harry_potter1.txt", "r", encoding="windows-1251") as file1:

                alf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                bi = dict()
                sum = 0
                for line in file1:
                    for i in range(len(line) - 1):
                        a = line[i]
                        b = line[i + 1]
                        if a in alf and b in alf:
                            x = a.lower() + b.lower()
                            bi[x] = bi.setdefault(x, 0) + 1
                            sum += 1



                print(sum)
                l = len(bi)
                a = 0
                alf = "abcdefghijklmnopqrstuvwxyz"
                for i in range(len(alf)):
                    for j in range(len(alf)):
                        x = alf[i] + alf[j]
                        bi[x] = bi.setdefault(x, 0) / sum * 100
                bi = {a: b for a, b in sorted(bi.items(), key=lambda item: item[1])}
                k=bi.keys()
                with open("output.txt", "w", encoding="utf-8") as f:
                    for i in k:
                        f.write(f"{i}:{toFixed(bi[i],5)}\n")

                print(a)
                print(bi)

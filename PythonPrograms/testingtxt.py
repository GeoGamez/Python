
with open ("C:/Users/yoyo5/Desktop/IMS.txt", 'r+') as IMSR:
    lines = [line.rstrip('\n') for line in IMSR]
    ids = [lines[x] for x in range(0, len(lines), 4)]
    desc = [lines[x] for x in range(1, len(lines), 4)]
    stock = [lines[x] for x in range(2, len(lines), 4)]
    price = [lines[x] for x in range(3, len(lines), 4)]
    boom = input("Hi")
    IMSR.write(boom+"\n")
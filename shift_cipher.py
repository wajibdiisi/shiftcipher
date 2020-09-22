import sys

def shift_algorithm(inpString,key):
    result = ""
    if choice == 1 :
        print("Hasil Enkripsi : ", end="")
        for i in range(0, len(inpString)):
            char = inpString[i]
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + key - 97) % 26 + 97)
            elif char == " ":
                result += char
        print(result, end="")
    if choice == 2 :
        print("Hasil Dekripsi : ", end="")
        for i in range(0, len(inpString)):
            char = inpString[i]
            if char.isupper():
                result += chr((ord(char) - key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - key - 97) % 26 + 97)
            elif char == " ":
                result += char
        print(result, end="")

c= 0
while c < 1 :
    try: 
        print("1.Enkripsi")
        print("2.Dekripsi")
        print("3.Exit")
        choice = int(input("Masukkan Pilihan : "))
        if choice > 3 or choice < 1 :
            continue
        elif choice == 3 :
            sys.exit()
        else:
            while True:
                inpString = str(input("Masukkan Teks : "))
                if inpString.isalpha():
                    break
                else :
                    print("Input harus huruf")
                    inpString = None
            key = int(input("Masukkan Key: "))
            shift_algorithm(inpString,key)
            c = 1
    except ValueError:
        print("Input harus angka")
        continue
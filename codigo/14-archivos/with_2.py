try:
    with open("archivo.txt") as f:
        print(f.read())
except:
    print("Error")
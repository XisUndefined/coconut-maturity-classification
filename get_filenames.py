import os

dir = input("Enter Directory\t\t\t: ")
name = input("Enter Filename for txt file\t: ")
os.chdir(rf"{dir}")
listname = os.listdir()
os.chdir("..")

def writefile(filename: str):
    with open(f'{filename}.txt', 'w') as f:
        for name in listname:
            f.write(f"{name[12:-4].replace('_', ' ')}\n")

writefile(filename=name)
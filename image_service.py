import os

def main() -> str:
    with open('handler.txt', 'r') as pipe:
        command =  pipe.readline()
        if command == "RUN\n":
            img_num = int(pipe.readline())
        else:
            return -1
    pipe.close()

    dirlist = os.listdir(path='./archive/pokemon/pokemon')

    return dirlist[img_num]

if __name__ == "__main__":
    print(main())
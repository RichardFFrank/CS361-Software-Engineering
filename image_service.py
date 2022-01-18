import os, os.path
from time import sleep

def main() -> str:
    while True:
        # check if the prng-service file exists.
        if os.path.exists('image-service.txt'):
        # open handler file check for the RUN command. If it is there, read the integer on the next line.
            with open('image-service.txt', 'r+') as pipe:
                command =  pipe.readline()
                if command == "RUN\n":
                    img_num = int(pipe.readline())
                    pipe.truncate(0)
                    pipe.close()
                    # using the path to the image folder, get the path of the image at the i-th position in the directory list.
                    img_path = './archive/pokemon/pokemon/'
                    dirlist = os.listdir(path=img_path)
                    if img_num > 100:
                        img_num = img_num % 100
                    # write the path to the file to the img_handler file.
                    with open('image-service.txt', 'w') as pipe:
                        pipe.write(img_path[1:]+dirlist[img_num])
                    pipe.close()  
            pipe.close()
            sleep(2)
        else:
            sleep(2)

if __name__ == "__main__":
    main()
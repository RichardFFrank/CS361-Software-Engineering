import random, os, os.path
from time import sleep

def main() -> int:
    # seed the random value, default uses current time.
    random.seed()


    while True:
        if os.path.exists('prng-service.txt'):
            with open('prng-service.txt', 'r+') as start:
                command =  start.readline()
                if command == 'RUN\n':
                    sleep(2)
                    start.truncate(0)
                    start.close()
                    with open('prng-service.txt', 'w') as start:
                        return_value = random.randrange(1000)
                        start.write(str(return_value))
                        start.close()
                else:
                    sleep(5)
        else:
            sleep(2)


    
if __name__ == "__main__":
    main()


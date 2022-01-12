import random, os, os.path, time

def main() -> int:
    # seed the random value, default uses current time.
    random.seed()


    while True:
        if os.path.exists('ui_start_command.txt'):
            with open('ui_start_command.txt', 'r') as start:
                command =  start.readline()
                if command == "RUN\n":
                    return_value = random.randrange(1000)
                    with open('prng-service.txt', 'w') as pipe:
                        pipe.write("RUN\n")
                        pipe.write(str(return_value))
                    pipe.close()
                    start.close()
                    os.remove('ui_start_command.txt')
                else:
                    os.remove('ui_start_command.txt')
        else:
            time.sleep(2)


    
if __name__ == "__main__":
    main()


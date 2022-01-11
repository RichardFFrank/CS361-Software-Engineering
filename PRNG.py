import random, os

def main() -> int:
    random.seed()
    return_value = random.randrange(100)
    with open('handler.txt', 'w') as pipe:
        pipe.write("RUN\n")
        pipe.write(str(return_value))
        
    pipe.close()

    
if __name__ == "__main__":
    main()


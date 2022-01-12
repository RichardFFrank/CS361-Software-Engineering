import random, os

def main() -> int:
    # seed the random value, default uses current time.
    random.seed()
    return_value = random.randrange(1000)
    if return_value > 818:
        return_value = return_value % 818
    with open('prng-service.txt', 'w') as pipe:
        pipe.write("RUN\n")
        pipe.write(str(return_value))
    pipe.close()

    
if __name__ == "__main__":
    main()


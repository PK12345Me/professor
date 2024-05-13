import random

def get_level():
    num = 0
    try:
        num = int(input(""))
        if str(num) in ['1','2','3']:
            return num
        else:
            return get_level()

    except ValueError as f:
        print("Error:", f)
        return get_level()


def main():
    funVar = get_level()
    k = 0
    for i in range(10):

        n, m = generate_integer(funVar)

        prof = input(f"{n} + {m} =")
        a = n + m

        if int(a) == int(prof):
            k += 1
            i += 1
        else:
            print("EEE")
            i += 1
            g = 0
            while g < 3:
                prof = input(f"{n} + {m} =")
                g += 1
                if g == 2: #not g==3, since 0,1,2 is three times
                    #print(f"{n} + {m} = {a}")
                    print(f"{a}")
                    break
                elif int(a) == int(prof):

                    break
                else:
                    continue


    #print(f"user’s score: {k}/10")
    print(f"{k}")


def generate_integer(level):
    if level == 1:
        n = (random.randint(0,9))
        m = (random.randint(0,9))
        return n,m
    elif level == 2:
        n = (random.randint(10,99))
        m = (random.randint(10,99))
        return n,m
    elif level == 3:
        n = (random.randint(100,999))
        m = (random.randint(100,999))
        return n,m



if __name__ == "__main__":
    main()


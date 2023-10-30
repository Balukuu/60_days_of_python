#For Loops
#For loops are used for iterating over a sequence (e.g., a list, tuple, string, or range) or other iterable objects.

def main():
    number = get_number()
    meow(number)
def get_number():
    while True:
        n = int(input("whats n? "))
        if n > 0:
            break
    return n    


def meow(n):
    for _ in range(n):   
        print ("baluku")
main()        
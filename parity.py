def main():
    x =int(input("whats x?"))

    if is_evenFUN(x):
       print("Even")
    else:
       print("Odd")

def is_evenFUN(n):
    return True if n%2 ==0 else False  
   
main()   
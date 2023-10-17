def main():
    x =int(input("whats x?"))

    if is_evenFUN(x):
       print("Even")
    else:
       print("Odd")

def is_evenFUN(n):
   if n%2 == 0:
      return True
   else:
      return False       
   
main()   


def main():
    x = int(input("What's x? "))
    if x_iseven(x):
        print("Even")
    else:
        print("Odd")  
            
def x_iseven(n):
    return n % 2 == 0

main()
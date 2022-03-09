


x = int(input("enter some numbers: "))  

def reverse_loop(x):
    n = []
    while x != "":
        y = int(x)
        n.append(y)
        x = input("enter numbers: ")
        n.reverse()
        print(n)
reverse_loop(x)
 

def facto(n):
    f = 1
    
    for i in range(1, n+1):
        f = f * i
        
    return f

def main():
    n = int(input("Enter a number: "))
    print(facto(n))
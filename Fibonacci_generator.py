def fibonacci_generate(n):
    a,b=0,1
    sequence=[]
    for _ in range(n):
        sequence.append(a)
        a,b=b,a+b 
    return sequence
n=int(input("Enter the Number of terms: "))
print("Fibonacci sequence:", fibonacci_generate(n))
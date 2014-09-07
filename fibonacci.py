"""Find the sum of all the numbers less than 1 billion
which appear in the Fibonacci sequence and are divisible by 3."""
f1=1
f2=1
s=0
for i in range(100):
    f3=f1+f2
    f1=f2
    f2=f3
    if f3<1000000000:
            if f3%3==0:
                s=s+f3

    print s
import numpy

def T1(n):
    return 0.007*n**3
def T2(n):
    return (0.36*n**2) + (0.15*n)
n=numpy.linspace(1,1000, 1000)
for i in n:
    if T2(i) < T1(i):
        break
print("From 1 to 1000, T2 becomes more efficient at", i)
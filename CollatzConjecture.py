import random
import sys
import matplotlib.pyplot as plt

arrX=[]
arrY=[]
#n = random.randint(1, sys.maxsize)
inputN = input("Enter a number: ")
n = int(inputN)
arrY.append(n)
x = 0
arrX.append(x)

print ('Start of program ' + str(n))
while n != 1:
    if n % 2 == 0:
        n = n / 2
        arrY.append(n)
        x = x + 1
        arrX.append(x)
    elif n % 2 == 1:
        n = 3 * n + 1
        arrY.append(n)
        x = x + 1
        arrX.append(x)
plt.plot(arrX, arrY)
plt.xlabel('Number of iterations')
plt.ylabel('Number')
plt.title('Collatz Conjecture')
plt.show()    
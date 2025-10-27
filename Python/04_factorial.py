# This code requests a number from the user and returns its factorial,
# printing each iteration of the multiplication.
from matplotlib.pylab import insert


a = input("insert a number: "); y = 1

for i in range(int(a)):
    y = y*(i+1)
    print(y)
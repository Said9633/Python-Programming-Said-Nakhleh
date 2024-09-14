

lst = {i for i in range (1, 11)}
lst.add (1)
print(lst)


import matplotlib.pyplot as plt 
x = list(range(10))
k = 2
m = 2
y = [k*x+m for x in x]

plt.plot(x,y)
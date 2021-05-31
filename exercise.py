import matplotlib.pyplot as plt

x = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
y = [220, 330, 190, 340, 410, 445, 415]

plt.xlabel("Temperature(degrees)")
plt.ylabel("Soup Sales(in Rands)")
plt.title("Soup Sales vs Temperature")
plt.scatter(x, y)
plt.show()

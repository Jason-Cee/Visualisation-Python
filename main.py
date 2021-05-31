"""import matplotlib.pyplot as plt

xs = [1,2,3,4,5]
ys = [x**2 for x in xs]

plt.plot(xs, ys)
plt.show()"""

"""import matplotlib.pyplot as plt

xs = range(-100, 100, 10)
x2 = [x ** 2 for x in xs]
negx2 = [-x ** 2 for x in xs]

plt.plot(xs, x2)
plt.plot(xs, negx2)
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-2000, 2000)
plt.axhline(0)  # horiz line
plt.axvline(0)  # vert line
plt.show()"""

"""import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y)
plt.show()"""

import matplotlib.pyplot as plt

a = [1.3, 3.4, 2.3, 9.8]
b = [3.5, 4.9, 1.3, 2.2]
c = [9.7, 1.5, 4.3, 0.9, 11.2]
data1 = [a, b, c]
plt.subplot(121)
plt.boxplot(data1)
plt.xlabel("Colleges")
plt.ylabel("Scores")
plt.title("Boxplot for colleges")
plt.subplot(122)
plt.hist(data1, bins=5)
plt.show()

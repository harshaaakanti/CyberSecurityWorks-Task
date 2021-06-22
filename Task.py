from matplotlib import pyplot as plt


axis_x = []
axis_y = []

n = int(input("Enter no.of Elements as input:"))

print("Enter Elements one by one:")
for i in range(0, n):
    ele = int(input())

    axis_y.append(ele)



for i in range(0, n):
    axis_x.append(i)


plt.plot(axis_x, axis_y)

plt.show()

#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig = plt.figure(figsize=(7, 7))
fig.suptitle("All in One")
grid = plt.GridSpec(3, 2, wspace=0.4, hspace=0.5)

plt0 = fig.add_subplot(grid[0,0])
plt.xlim(0,10)
plt.plot(y0,'r')

plt1 = fig.add_subplot(grid[0,1])
plt.xlabel('Height (in)' ,size="x-small")
plt.ylabel('Weight (lbs)' ,size="x-small")
plt.scatter(x1,y1)

plt2 = fig.add_subplot(grid[1,0])
plt.suptitle("Exponential Decay of C-14")
plt.xlabel('Time (years)',size="x-small")
plt.ylabel('Fraction Remaining',size="x-small")
plt.xlim(0,28650)
plt.yscale('log')
plt.plot(x2,y2)

plt3 = fig.add_subplot(grid[1,1])
plt.suptitle("Exponential Decay of Radioactive Elements")
plt.xlabel("Time (years)",size="x-small")
plt.ylabel("Fraction Remaining",size="x-small")
plt.xlim(0,20000)
plt.ylim(0,1)
plt.plot(x3, y31, '--r', label='C-14')
plt.plot(x3, y32, '-g', label='Ra-226')
plt.legend();

plt4 = fig.add_subplot(grid[2, :2])
plt.suptitle("Project A")
plt.xlabel("Grades",size="x-small")
plt.ylabel("Number of Students",size="x-small")
plt.hist(student_grades,bins=10, range=(0,100), edgecolor='black')
plt.xticks(np.arange(0, 110,10))


plt.show()
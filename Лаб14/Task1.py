import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 8, 161)

y = 5*np.sin(10*x)*np.sin(3*x)/(x**x)

plt.plot(x, y, label='y(x)=5*sin(10*x)*sin(3*x)/(x^x)', color = "red", linewidth = 2)

plt.title('My plot', fontsize=15)

plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.show()
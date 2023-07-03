import numpy as np #数值计算
import scipy.signal as ss
import matplotlib.pyplot as plt
rng = np.random.default_rng()
t = np.linspace(-1, 1, 201)
PI = 2*np.pi
x = (np.sin(PI*0.75*t*(1-t) + 2.1) +
     0.1*np.sin(PI*1.25*t + 1) +
     0.18*np.cos(PI*3.85*t))
# 原始数据添加噪声
xn = x + rng.standard_normal(len(t)) * 0.08
b, a = ss.butter(3, 0.05)

z = ss.lfilter(b, a, xn)
z2 = ss.lfilter(b, a, z)

plt.plot(t, z, 'r--', t, z2, 'r')
plt.scatter(t, xn, marker='.', alpha=0.75)
plt.legend(('lfilter, once', 'lfilter, twice', 'noisy signal'), loc='best')
plt.show()

# https://blog.51cto.com/u_13527/6366049
from scipy import signal # type: ignore

import matplotlib.pyplot as plt
import numpy as np

#生成要过滤的噪声信号
t = np.linspace(-1, 1, 201)
x = (np.sin(2*np.pi*0.75*t*(1-t) + 2.1) +
     0.1*np.sin(2*np.pi*1.25*t + 1) +
     0.18*np.cos(2*np.pi*3.85*t))
xn = x + np.random.randn(len(t)) * 0.08

#创建order3低通道butterworth过滤器：
b, a = signal.butter(3, 0.05)
#将过滤器应用于xn。使用lfilter_zi选择过滤器的初始条件：
zi = signal.lfilter_zi(b, a)
z, _ = signal.lfilter(b, a, xn, zi=zi*xn[0])
#再次应用过滤器，以与filtfilt相同的顺序过滤结果：
z2, _ = signal.lfilter(b, a, z, zi=zi*z[0])
#使用filtfilt应用过滤器：
y = signal.filtfilt(b, a, xn)
#绘制原始信号和各种过滤版本：
plt.figure
plt.plot(t, xn, 'b', alpha=0.75)
plt.plot(t, z, 'r--', t, z2, 'r', t, y, 'k')
plt.legend(('noisy signal', 'lfilter, once', 'lfilter, twice',
            'filtfilt'), loc='best')
plt.grid(True)
plt.show()


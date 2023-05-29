import numpy as np
import matplotlib.pyplot as plt

# 生成信号
t = np.linspace(0, 1, 1000, endpoint=False)  # 时间从0到1，共取1000个点
f1 = 10  # 第一个频率成分
f2 = 20  # 第二个频率成分
signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# 进行快速傅里叶变换
fft_result = np.fft.fft(signal)

# 计算频率轴
freq = np.fft.fftfreq(len(t), t[1]-t[0])


# 绘制结果
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original Signal')

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fft_result))
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Fourier Transform')

plt.tight_layout()
plt.show()

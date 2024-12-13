import numpy as np
import matplotlib.pyplot as plt
from math import log, ceil, pi
from scipy.signal import freqz, windows

#matplotlib设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

"""
wp 通带截止频率
ws 阻带截止频率
dp 通带波纹
ds 阻带波纹
"""
def 设计滤波器(wp: float, ws: float, dp: float, ds: float):
    # 阻带衰减
    a_s = -20 * np.log10(ds)

    # 计算滤波器长度
    M: float = 3.11 * pi / (ws - wp)
    N: int = ceil(2. * M + 1)

    # 截止频率
    wc = (ws + wp) / 2

    # 理想低通滤波器脉冲响应
    fRange: np.ndarray = np.arange(-M, M + 1)
    idealLPF = wc / pi * np.sinc(wc / pi * fRange)

    # 应用Hann窗
    hann_window = windows.hann(len(idealLPF))
    fNum = idealLPF * hann_window

    # 计算频率响应
    w, h = freqz(fNum, worN=512)  #注意fNum是非因果的，而freqz要求因果序列，所以这里的频率响应的相位是不准确的，不过幅度是准确的

    # 绘制滤波器系数
    # plt.figure()
    # plt.stem(fRange, fNum)
    # plt.title("滤波器系数")
    # plt.xlabel("n")
    # plt.ylabel("Amplitude")
    # plt.grid()

    # 绘制频率响应
    plt.figure()
    # plt.plot(w / pi, 20 * np.log10(np.abs(h)))
    plt.plot(w / pi, np.abs(h))
    plt.title("频率响应")
    plt.xlabel(r"$\omega/\pi$")
    plt.ylabel("增益 (dB)")
    plt.grid()

    #用对数图重新画一下频率响应
    plt.figure()
    plt.plot(w / pi, 20 * np.log10(np.abs(h)))
    plt.title("频率响应")
    plt.xlabel(r"$\omega/\pi$")
    plt.ylabel("增益 (dB)")
    plt.grid()
    plt.show()



    # 打印滤波器长度
    print(f"滤波器长度 N: {N}")

# 调用函数设计滤波器
设计滤波器(.42 * pi, .58 * pi, .002, .008)

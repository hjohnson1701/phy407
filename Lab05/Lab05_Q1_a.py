#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 16:25:26 2018

@author: Hayden
"""

import numpy as np
import matplotlib.pyplot as plt

month, spots = np.loadtxt('../data/sunspots.txt', unpack=True)

plt.figure(0)
plt.plot(month, spots, '.')
plt.xlabel('Time (months after 1759)')
plt.ylabel('Number of sunspots')
plt.title('Sunspots over time')
plt.savefig('../images/1a_timeseries.png')

plt.figure(1)
plt.plot(month, spots, '.')
plt.xlabel('Time (months after 1759)')
plt.ylabel('Number of sunspots')
plt.title('Sunspots over time (zoomed in)')
plt.xlim([2500,3000])
plt.savefig('../images/1a_timeseries_zoomed.png')

spots_fft = np.fft.rfft(spots)
k = np.arange(0,len(spots_fft))

plt.figure(2)
plt.plot(k, np.abs(spots_fft)**2)
plt.ylabel('$|c_k|^2$')
plt.xlabel('Fourier coefficient numer (k)')
plt.title('Fourier transform of sunspot data')
plt.savefig('../images/1a_fourier.png')

plt.figure(3)
plt.plot(k, np.abs(spots_fft)**2)
plt.xlim([0,50])
plt.ylim([0.0,5e9])
plt.ylabel('$|c_k|^2$')
plt.xlabel('Fourier coefficient numer (k)')
plt.title('Fourier transform of sunspot data (zoomed in)')
plt.savefig('../images/1a_fourier_zoomed.png')
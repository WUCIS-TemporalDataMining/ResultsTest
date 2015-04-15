# coding: utf-8
import pywt
import matplotlib.pyplot as plt

myw=pywt.Wavelet('db2')
phi,psi,wx = myw.wavefun()
plt.plot(wx,phi,'r')
plt.savefig('/tmp/Scale_Fun.PNG')
plt.plot(wx,psi,'b')
plt.savefig('/tmp/Basis_Fun.PNG')

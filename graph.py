# coding: utf-8
import pywt
import matplotlib.pyplot as plt

myw=pywt.Wavelet('db2')
phi,psi,wx = myw.wavefun()
plt.plot(wx,phi,'r')
plt.savefig('/tmp/DB_Scale_Fun.PNG')
plt.clf()
plt.plot(wx,psi,'b')
plt.savefig('/tmp/DB_Basis_Fun.PNG')
plt.clf()

myw=pywt.Wavelet('haar')
phi,psi,wx = myw.wavefun()
plt.plot(wx,phi,'r')
plt.savefig('/tmp/HR_Scale_Fun.PNG')
plt.clf()
plt.plot(wx,psi,'b')
plt.savefig('/tmp/HR_Basis_Fun.PNG')
plt.clf()

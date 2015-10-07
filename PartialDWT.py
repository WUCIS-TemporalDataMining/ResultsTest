
# coding: utf-8

# In[11]:

forex=[1.3347,
1.3198,
1.3174,
1.3094,
1.3244,
1.31,
1.2946,
1.287,
1.2955,
1.2849,
1.3123,
1.3159,
1.3244,
1.2988,
1.2804,
1.2808,
1.301,
1.2857,
1.2838,
1.2874,
1.3064,
1.2966,
1.2893,
1.2822,
1.2879,
1.26,
1.2571,
1.2547,
1.2675,
1.269,
1.2747,
1.2742,
1.2731,
1.2764,
1.2662,
1.258,
1.2549,
1.2607,
1.2565,
1.2674,
1.2636,
1.2752,
1.2774,
1.2799,
1.2891,
1.2997,
1.2972,
1.311,
1.373,
1.3566,
1.3569,
1.3524,
1.3539,
1.356,
1.3306,
1.3146,
1.3261,
1.3223,
1.3458,
1.3447,
1.3363,
1.3282,
1.3288,
1.3149,
1.3143]


# In[31]:

#!/usr/bin/env python


import pylab

import pywt

data1 = pylab.array(range(1, 400) + range(398, 600) + range(601, 1024))
x = pylab.arange(612 - 80, 20, -0.5) / 250.
data2 = pylab.sin(40 * pylab.log(x)) * pylab.sign((pylab.log(x)))

data3 = forex 

mode = pywt.MODES.sp1


def plot(data, w, title):
    print title
    w = pywt.Wavelet(w)
    a = data
    ca = []
    cd = []
    for i in xrange(5):
        (a, d) = pywt.dwt(a, w, mode)
        ca.append(a)
        cd.append(d)

    rec_a = []
    rec_d = []

    for i, coeff in enumerate(ca):
        coeff_list = [coeff, None] + [None] * i
        rec_a.append(pywt.waverec(coeff_list, w))

    for i, coeff in enumerate(cd):
        coeff_list = [None, coeff] + [None] * i
        rec_d.append(pywt.waverec(coeff_list, w))

    pylab.figure()
    ax_main = pylab.subplot(len(rec_a) + 1, 1, 1)
    pylab.title(title)
    ax_main.plot(data)
    pylab.xlim(0, len(data) - 1)
    pylab.locator_params(axis = 'y', nbins = 5)
    pylab.subplots_adjust(hspace=.5)

    for i, y in enumerate(rec_a):
        #print len(data), len(x), len(data) / (2**(i+1))
        ax = pylab.subplot(len(rec_a) + 1, 2, 3 + i * 2)
        ax.plot(y, 'r')
        pylab.xlim(0, 65)
        pylab.ylabel("Coef%d" % (i + 1))
        pylab.locator_params(axis = 'y', nbins = 5)


    for i, y in enumerate(rec_d):
        ax = pylab.subplot(len(rec_d) + 1, 2, 4 + i * 2)
        ax.plot(y, 'g')
        pylab.xlim(0, 65)
        #pylab.ylim(min(0,1.4*min(x)), max(0,1.4*max(x)))
        pylab.ylabel("D%d" % (i + 1))
        pylab.locator_params(axis = 'y', nbins = 5)

print "Signal decomposition (S = An + Dn + Dn-1 + ... + D1)"
plot(data3, 'db2', "DWT: Daubechies 4 (db2)")
plot(data3, 'haar', "DWT: Haar")
pylab.show()


# In[ ]:




# In[ ]:




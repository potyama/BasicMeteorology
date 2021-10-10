
def align_digit(f, digit=None,shift=3):
    if digit==None:
        digit = int("{:e}".format(f).split("e")[1])-shift
    if digit<=0: s = str("{:."+str(-digit)+"f}").format(f)
    else: s = str("{:.3e}").format(f)
    return s, digit


import numpy as np

c = 299792456
h = 6.62607* 10**-34
k = 1.38065* 10 **(-23)

sigma = (2*k**4*np.pi**3)/(15*h**3 *c**2)

print(align_digit(sigma))

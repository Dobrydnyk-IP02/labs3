a = int (input ("Введіть число: "))
if a<=0:
    print ("Введіть додатнє число")
else:
    l=1
    y=(1+a)/2
    from math import fabs
    while fabs (y-l)>0.0001: 
           l=y
           y=(l+a/l)/2
           print (y)


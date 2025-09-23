Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from collections import Counter
counter_l1=Counter({1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31})
counter_l2=Counter({1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31})
s=2
q=[]
def leap(i):
    if i%4==0 and i%100!=0:
        return 'Yes'
    elif i%400==0:
        return 'Yes'
...     else:
...         return 'No'
... 
...     
>>> for j in range(1901,2001):
...     if leap(j)=='Yes':
...         l=counter_l2
...     else:
...         l=counter_l1
...     p=list(map(mod,l.values()))
...     for i in p:
...         s=s+i
...         if s>7:
...             s=s-7
...         q.append(s)
... 
...         
Traceback (most recent call last):
  File "<pyshell#8>", line 6, in <module>
    p=list(map(mod,l.values()))
NameError: name 'mod' is not defined
>>> def mod(i):
...     return i%7
... 
>>> for j in range(1901,2001):
...     if leap(j)=='Yes':
...         l=counter_l2
...     else:
...         l=counter_l1
...     p=list(map(mod,l.values()))
...     for i in p:
...         s=s+i
...         if s>7:
...             s=s-7
...         q.append(s)
... 
...         
>>> q.count(7)
171

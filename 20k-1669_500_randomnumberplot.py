#!/usr/bin/env python
# coding: utf-8

# In[4]:


from matplotlib import pyplot as plt
x = range(6)# range is for 6 algorithms applied eg,0 for insertion,1 for merge,2 for quicksort with middle pivot ,3 for random 
y = [0.55,0.54,0.69,0.67,0.70,0.53]# 4 for median pivot,5 for updated median pivot

plt.title('Analysis for 500 random numbers')
plt.xlabel('Algorithms')
plt.ylabel('Compilation Time')
plt.plot(x, y,color='purple',marker='s',linestyle='--')
plt.show()


# In[ ]:





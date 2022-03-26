#!/usr/bin/env python
# coding: utf-8

# In[5]:


from matplotlib import pyplot as plt
x = range(6)# range is for 6 algorithms applied eg,0 for insertion,1 for merge,2 for quicksort with middle pivot ,3 for random 
y = [0.56,0.59,0.55,0.53,0.61,0.55]# 4 for median pivot,5 for updated median pivot

plt.title('Analysis for 200 random numbers')
plt.xlabel('Algorithms')
plt.ylabel('Compilation Time')
plt.plot(x, y,color='green',marker='s',linestyle='--')
plt.show()


# In[ ]:





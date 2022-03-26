#!/usr/bin/env python
# coding: utf-8

# In[10]:


from matplotlib import pyplot as plt
x = range(6)# range is for 6 algorithms applied eg,1 for insertion,2 for merge,3 for quicksort with middle pivot ,4 for random 
y = [0.44,0.45,0.42,0.44,0.57,0.47]# 5 for median pivot,6 for updated median pivot

plt.title('Analysis for 50 random numbers')
plt.xlabel('Algorithms')
plt.ylabel('Compilation Time')
plt.plot(x, y,color='blue',marker='s',linestyle='--')
plt.show()


# In[ ]:





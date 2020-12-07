#!/usr/bin/env python
# coding: utf-8

# ARRAYS WITH NUMPY

# In[1]:


import numpy as np


# In[2]:


id_list = [1,2,3,4,5,6]


# In[3]:


id_list


# In[6]:


array_idList = np.array(id_list)


# OUTPUT SHALL BE A VECTOR

# In[7]:


array_idList


# In[8]:


d2_list = [[1,2,3],[4,5,6],[7,8,9]]


# In[9]:


array_2d_list = np.array(d2_list)


# OUTPUT SHALL BE A MATRICE

# In[10]:


array_2d_list


# CREATE EASY AND FAST ARRAYS USING THE ARRANGE METHOD (RANGE)

# In[15]:


np.arange(0 , 6)


# .arange(begin ,last, step)

# In[18]:


i = 0
j = 10
step = 2


# In[21]:


np.arange(i, j, step)


# ARRAYS OF ZEROS WITH .zeros((rows, columns))

# In[22]:


np.zeros(5)


# In[23]:


np.zeros((4,5))


# ARRAYS OF ONES WITH .ones((rows, columns))

# In[24]:


np.ones(5)


# In[25]:


np.ones((4,5))


# ARRAYS OF LINSPACE WITH .linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0) Return evenly spaced numbers over a specified interval.

# In[34]:


np.linspace(0,10 , 200)


# EYE   .eye returns a matrices diagonal of ones and rest of zeros

# In[35]:


np.eye(5)


# random Method 

# In[36]:


np.random.rand(3)


# In[37]:


np.random.rand(3 , 3)


# randn Return a sample (or samples) from the “standard normal” distribution.
# 

# In[42]:


np.random.randn(5)


# In[44]:


np.random.randn(2,3)


# randint (included , excluded , range)

# In[45]:


np.random.randint(1, 559, 15)


#     .reshape Gives a new shape to an array without changing its data.

# In[47]:


my_array = np.arange(0, 35)


# In[48]:


my_array


# In[49]:


my_array.reshape(5, 7)


# In[50]:


my_array.reshape(7, 5)


# min() , max(), argmin() => return index of the min value , argmax()

# In[51]:


my_array.min()


# In[52]:


my_array.argmin()


# In[53]:


my_array.max()


# In[54]:


my_array.argmax()


# shape,  get the current shape of an array whether it's a matrice or a vector

# In[60]:


my_arr = np.random.randint(0 , 100 , 15)


# In[61]:


my_arr.shape


# In[65]:


my_arr = my_arr.reshape(5, 3)


# In[66]:


my_arr


# In[67]:


my_arr.shape


# Data type with dtype

# In[70]:


my_arr.dtype


# In[ ]:





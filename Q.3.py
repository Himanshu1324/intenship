#!/usr/bin/env python
# coding: utf-8

# # 3. Provide a program to calculate the time and distance based on below problem.

# In[1]:


t = c1 = c2 = 0

while c1+c2<=100:

   c1 += 1
   if t%10==0:
      c1-=2
        
   c2 += 2
   if t%5==0:
        c2-=1

   t+=1

print(t, c1, c2)


# In[ ]:





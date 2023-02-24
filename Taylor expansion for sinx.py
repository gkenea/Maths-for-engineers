#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp
from scipy.special import factorial


# In[8]:


x = np.linspace(-10, 10, 2000)
y = np.sin(x)
plt.plot(x, y,'k', linewidth =2)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)


# Frist order taylor expansion

# In[ ]:





# In[31]:


P = [1, 0]  # x+0
yT1 = np.polyval(P, x)
plt.plot(x, yT1, 'b--', linewidth = 2)


# Third order taylor expansion

# In[30]:


P = [-1/factorial(3), 0, 1, 0]  # x+0
yT3 = np.polyval(P, x)
plt.plot(x, yT3, 'r--', linewidth = 2)


# Fivth order taylor expansion

# In[29]:


P = [1/factorial(5), 0, -1/factorial(3), 0, 1, 0]  # x+0
yT5 = np.polyval(P, x)
plt.plot(x, yT5, 'g--', linewidth = 2)


# Seventh order taylor expansion

# In[28]:


P = [-1/factorial(7), 0, 1/factorial(5), 0, -1/factorial(3), 0, 1, 0]  # x+0
yT7 = np.polyval(P, x)
plt.plot(x, yT7, 'm--', linewidth = 2)


# ninth order taylor expansion

# In[26]:


P = [1/factorial(9), 0, -1/factorial(7), 0, 1/factorial(5), 0, -1/factorial(3), 0, 1, 0]  # x+0
yT9 = np.polyval(P, x)
plt.plot(x, yT9, 'c--', linewidth = 2)


# In[32]:


plt.legend(['sinx', '1st order', '3rd order','5th order','7th order','9th order'])
plt.show()


# In[33]:


x = np.linspace(-10, 10, 2000)
y = np.sin(x)
plt.plot(x, y,'k', linewidth =2)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)

#Frist order taylor expansion
P = [1, 0]  # x+0
yT1 = np.polyval(P, x)
plt.plot(x, yT1, 'b--', linewidth = 2)

#Third order taylor expansion
P = [-1/factorial(3), 0, 1, 0]  # x+0
yT3 = np.polyval(P, x)
plt.plot(x, yT3, 'r--', linewidth = 2)

#fivth order taylor expansion
P = [1/factorial(5), 0, -1/factorial(3), 0, 1, 0]  # x+0
yT5 = np.polyval(P, x)
plt.plot(x, yT5, 'g--', linewidth = 2)


#seventh order taylor expansion
P = [-1/factorial(7), 0, 1/factorial(5), 0, -1/factorial(3), 0, 1, 0]  # x+0
yT7 = np.polyval(P, x)
plt.plot(x, yT7, 'm--', linewidth = 2)

#ninth order taylor expansion
P = [1/factorial(9), 0, -1/factorial(7), 0, 1/factorial(5), 0, -1/factorial(3), 0, 1, 0]  # x+0
yT9 = np.polyval(Q, x)
plt.plot(x, yT9, 'c--', linewidth = 2)
plt.legend(['sinx', '1st order', '3rd order','5th order','7th order','9th order'])
plt.show()


# In[ ]:





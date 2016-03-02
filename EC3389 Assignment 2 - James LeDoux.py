
# coding: utf-8

# # <center> EC3389 - Assignment 2 - James LeDoux </center>

# In[9]:

import numpy as np
import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt


# In[10]:

def create_data(n_obs):
    x_1 = np.random.uniform(0, 10, n_obs)
    x_2 = np.random.uniform(-5, 5, n_obs)
    e = np.random.normal(0, 1, n_obs)
    y = 2 + 3*x_1 + 5*x_2 + e
    dat ={'x1': x_1, 'x2': x_2, 'y': y}
    df = pd.DataFrame(dat)
    return df
    


# In[11]:

df = create_data(100)
df.head()


# In[12]:

# beta = [b0, b1, b2]
def get_sum_squared_residuals(beta, df):
    sqResid = (df['y'] - (beta[0] + (beta[1]*df['x1']) + (beta[2]*df['x2'])))**2
    sumSquared = np.sum(sqResid)
    return sumSquared
    
#get_sum_squared_residuals([ 1.77057033,  3.02077384,  5.04497825],df)


# In[13]:

def estimate_beta(df):
    return optimize.minimize(get_sum_squared_residuals, [2.0,3.0,5.0], args=(df)).x


# In[14]:

estimate_beta(df)


# In[15]:

def monte_carlo(n_sims, n_obs):
    #init betahats
    betahats = np.zeros((n_sims, 3))
    for i in range(n_sims):
        data = create_data(n_obs)
        beta = estimate_beta(data)
        for j in range(3):
            betahats[i, j] = beta[j]
    return(betahats)        
    


# In[16]:

betahats = monte_carlo(500, 50)
#np.zeros((10, 10))
print(betahats)
betahats.shape


# def print_simulation(betahats):
#     plt.hist(betahats)
# 

# In[ ]:

fig, ax = plt.subplots(1,3, figsize = (12,5))
fig.suptitle("Distributions of Estimators within Yhat", fontsize = 20)
ax[0].hist(betahats[:,0], bins=80, normed = 1, color="red")
ax[0].set_title("Distribution of the sample Intercept", fontsize = 14)
ax[1].hist(betahats[:,1], bins = 80, normed=1, color="blue")
ax[1].set_title("Distribution of the sample B1", fontsize = 14)
ax[2].hist(betahats[:,2], bins = 80, normed=1, color="yellow")
ax[2].set_title("Distribution of the sample B2", fontsize = 14)
plt.show()


# In[ ]:




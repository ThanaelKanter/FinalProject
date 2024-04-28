#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import astropy.io as ast


# In[12]:


exoplanets = ast.ascii.read('exoplanets.csv')
exoplanets


# In[13]:


filtered_columns = exoplanets['pl_name', 'sy_snum', 'pl_orbper', 'pl_orbsmax', 'pl_masse', 'pl_rade', 'pl_eqt', 'sy_dist']
filtered_columns


# In[14]:


from astropy.table import Table
complete_rows = [row for row in filtered_columns if all(val != "--" for val in row)]
complete_data = Table(rows=complete_rows, names=filtered_columns.colnames)
complete_data


# In[20]:


for row in complete_data:
    if (row['sy_snum'] > 0) and (row['sy_snum'] < 2) and (row['pl_rade'] >= 0.5) and (row['pl_rade'] <= 10) and (row['pl_eqt'] >= 175) and (row['pl_eqt'] <= 270):
        print(row)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





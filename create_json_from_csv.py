#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
import json

df            = pd.read_csv('work/material_properties.csv', index_col=0).fillna('')
df_categories = df['category'].unique()
dict_from_df  = {}

for category in df_categories:
    d = df.query('category == @category').drop('category', axis=1).to_dict(orient='index')
    dict_from_df[category] = d

with open('material_properties.json', mode='w') as f:
    json.dump(dict_from_df, f)


# In[ ]:





import pandas as pd
import json

df            = pd.read_csv('material_properties.csv', index_col=0).fillna('')
dict_from_df  = {}

for category in df['category'].unique():
    df_materials = df.query('category == @category').drop('category', axis=1)
    notes        = df_materials.loc[:, ['notes']].to_dict(orient='index')
    density      = df_materials.filter(like='density').rename(columns={'density min': 'min', "density max": 'max'}).to_dict(orient='index')
    youngx       = df_materials.filter(like='young-x').rename(columns={'young-x min': 'min', "young-x max": 'max'}).to_dict(orient='index')
    youngy       = df_materials.filter(like='young-y').rename(columns={'young-y min': 'min', "young-y max": 'max'}).to_dict(orient='index')
    youngz       = df_materials.filter(like='young-z').rename(columns={'young-z min': 'min', "young-z max": 'max'}).to_dict(orient='index')
    poisson      = df_materials.filter(like='poisson').rename(columns={'poisson min': 'min', "poisson max": 'max'}).to_dict(orient='index')
    freqloss     = df_materials.filter(like='freq-loss').rename(columns={'freq-loss min': 'min', "freq-loss max": 'max'}).to_dict(orient='index')
    constloss    = df_materials.filter(like='const-loss').rename(columns={'const-loss min': 'min', "const-loss max": 'max'}).to_dict(orient='index')
    
    tmp = notes.copy()
    
    for k, v in notes.items():
        tmp[k]['density']   = density[k]
        tmp[k]['young-x']   = youngx[k]
        tmp[k]['young-y']   = youngy[k]
        tmp[k]['young-z']   = youngz[k]
        tmp[k]['poisson']   = poisson[k]
        tmp[k]['freq-loss']  = freqloss[k]
        tmp[k]['const-loss'] = constloss[k]
        
    dict_from_df[category] = tmp
    
with open('material_properties.json', mode='w') as f:
    json.dump(dict_from_df, f)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['BMI'] = df['weight']/(df['height']/100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3
df['cholesterol'] = df['cholesterol'].replace({1: 0, 2: 1, 3:1})
df['gluc'] = df['gluc'].replace({1: 0, 2:1, 3:1})

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])

    # 6
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name = 'total')
    
    # 7
    fig = sns.catplot(x='variable',y='total',hue='value',col='cardio',data=df_cat,kind='bar').fig

    # 8

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975)) 
    ]
     
    df_heat = df_heat.drop(columns=['BMI'])

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # 14
    fig, ax = plt.subplots(figsize=(12,8))

    # 15
    ax = sns.heatmap(corr, center=0, vmax=0.25, annot=True, mask=mask, cmap='coolwarm', fmt='.1f', square=True)

    # 16
    fig.savefig('heatmap.png')
    return fig


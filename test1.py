import pandas as pd

series = pd.Series([100,200,300])
print(series)
gl = pd.read_csv('Pre_Saber_2019-2.csv')
# gl.info(memory_usage='deep')
print(type(gl))
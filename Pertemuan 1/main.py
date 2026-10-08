import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = sns.load_dataset('titanic')
print(df.head(5))
df.info()
df.describe()


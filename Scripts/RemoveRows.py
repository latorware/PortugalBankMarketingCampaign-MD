
import pandas as pd
import numpy as np
np.random.seed(10)



df = pd.read_csv(r'..\RawDatasets\bank-additional-full.csv')
remove_n = len(df.index) - 10000
drop_indices = np.random.choice(df.index, remove_n, replace=False)
df_subset = df.drop(drop_indices)
print(len(df_subset.index))
df_subset.to_csv(r'..\RawDatasets\bank-additional-10000.csv')
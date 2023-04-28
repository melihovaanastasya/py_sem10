import pandas as pd
import numpy as np
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
encoding_dict = {value: [1 if data.loc[idx, 'whoAmI'] == value else 0 for idx in range(len(data))] for value in data['whoAmI'].unique()}
encoding_df = pd.DataFrame(encoding_dict)
print(encoding_df)
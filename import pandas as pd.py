import pandas as pd
import numpy as np
  
df = pd.Series(['The neighbourhood', 'Arctic Monkeys', 'The kooks', 'The strokes',
                'Indie', np.nan, 'Rock Indie'], dtype=pd.StringDtype())
  
print(df.str.lower(),'\n')
print(df.str.upper(),'\n')
print(df.str.strip())
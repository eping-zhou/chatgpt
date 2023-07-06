import pandas as pd
df1 = pd.read_csv('https://query.data.world/s/rirbpq66zlwljyymwawfdeanvzyswd?dws=00000')
df2 = pd.read_csv('https://query.data.world/s/pynwnu66hvj42l7a7ez7t22l2lgx45?dws=00000')

print(df2.head())
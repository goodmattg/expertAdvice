import pandas as pd

filename = 'RGDP.csv'

dat = pd.read_csv(filename)

years = dat.groupby('YEAR')

# for q in years.groups
yfocus = dat[dat['YEAR']==2011]
qfocus = yfocus[yfocus['QUARTER']==1]

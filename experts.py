import pandas as pd
import numpy as np

dat = pd.read_csv('HOUSING.csv')

aggErrors = set()

for person in dat['ID'].unique():

    ud = dat[dat['ID']==person]
    ud = ud[ud['OUTCOME']>0]
    errors = ud.apply(lambda x: abs(x['NGDP1'] - x['OUTCOME']), axis=1)
    aggErrors.add(errors.mean())

aggErrors = {el for el in aggErrors if not np.isnan(el)}
plotable = np.array(list(aggErrors))


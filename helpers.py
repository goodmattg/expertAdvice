import pandas as pd
import numpy as np
import re
import sys

'''
Takes in CSV filename, outputPath. Sorts out the correct columns under a
'''

def gatherOutcomeColumns(file, pathTo, pathOut):

    dat = pd.read_csv(pathTo + file)

    rdat = dat.copy()
    rdat.columns = map(str.upper, rdat.columns)

    # get the base indicator from filename
    indic = re.search('^[^\.]*', file).group(0) + '1'
    print(indic)

    # create new "OUTCOME" column
    rdat['OUTCOME'] = pd.Series(-1 * np.ones(len(rdat['YEAR'])))

    yRange = rdat['YEAR'].unique()       # should be 2010-2016
    qRange = rdat['QUARTER'].unique()    # should be 1-4

    # rdat.loc[rdat['YEAR']==2010, 'OUTCOME'] = 2

    for y in yRange:
        for q in qRange:

            if (q==4):
                outcomesPHI = rdat.loc[(rdat['YEAR']==(y+1)) & (rdat['QUARTER']==1), \
                indic].copy()
            else:
            # try and get rdata for the next quarter -- > wrong indicator name
                outcomesPHI = rdat.loc[(rdat['YEAR']==y) & (rdat['QUARTER']==q+1), \
                indic].copy()

            # append the column
            if (outcomesPHI.size != 0):

                # find the first numerical value
                for o in outcomesPHI:
                    if (not(np.isnan(o))):
                        outcomesDET = o

                print(o)
                rdat.loc[(rdat['YEAR']==y) & (rdat['QUARTER']==q), 'OUTCOME'] = outcomesDET


    rdat.to_csv(pathOut + file)

# Run from command line
if __name__ == "__main__":
    gatherOutcomeColumns(sys.argv[1], sys.argv[2], sys.argv[3])

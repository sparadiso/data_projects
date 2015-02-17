import sklearn as sk
import numpy as np
import pylab as py
import pandas as pd
import cPickle as pickle

def LoadData(fname):
    data = pd.read_csv(fname, delimiter=',')
    data.columns = [u'cement', u'slag', u'ash', u'water', u'plasticizer', u'coarse aggregate', u'fine aggregate', u'age', u'strength']
    return data

import pandas as pd
import numpy as np
import pdb
from sklearn.cross_validation import train_test_split
from sklearn import base, ensemble, pipeline

class Transformer(base.BaseEstimator, base.TransformerMixin):

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_transf = X[[u'GeoLat', u'GeoLon']]
        return X_transf



import pandas as pd
import numpy as np
import pdb
from sklearn.cross_validation import train_test_split
from sklearn import base, ensemble, pipeline


class Transformer(base.BaseEstimator, base.TransformerMixin):

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # similar numbers, so without normalization
        X_transf = X[[u'NumBedrooms', u'NumBaths', u'ExteriorStories']]
        return X_transf



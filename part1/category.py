import pandas as pd
import numpy as np
import pdb
from sklearn.cross_validation import train_test_split
from sklearn import base, ensemble, pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import linear_model

class Transformer(base.BaseEstimator, base.TransformerMixin):

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        cols_cat = [u'Pool', u'DwellingType']
        X_cat = X[cols_cat]
        X_transf = X_cat.T.to_dict().values()
        return X_transf


est_new = pipeline.Pipeline([('trans', Transformer()),
                             ('trans_vec', DictVectorizer(sparse=True)),
                             ('trans_tfidf', TfidfTransformer()),
                             ("est", linear_model.Ridge())])


import pandas as pd
import numpy as np
import pdb
from sklearn.cross_validation import train_test_split
from sklearn import base, ensemble, pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import linear_model


df = pd.read_csv("data_sci_snippet.csv")

#removing data with none ClosePrice
df = df[np.isfinite(df['ClosePrice'])]
df = df[df['ClosePrice'] > 1000]

#removin data GeoLat and LivingArea (just a few rows)
df = df[np.isfinite(df[u'GeoLat'])]
df = df[np.isfinite(df['LivingArea'])]
df = df[df['LivingArea']>200]

# splitting for testing and training data
X_train, X_test = train_test_split(df, test_size = 0.2)


# importing smaller models and creating a pipeline
import num_bed_bath as num
import latlon as lat
import category as cat
import listprice as prc
import livarea as liv

est_new = pipeline.Pipeline([
        ('features', pipeline.FeatureUnion([
            ('num_trans', num.Transformer()),
            ('lat_trans', lat.Transformer()),
            ('prc_trans', prc.Transformer()),
            ('liv_trans', liv.Transformer()),
#            ('cat_trans', pipeline.Pipeline([
#                ('trans', cat.Transformer()),
#                ('trans_vec', DictVectorizer(sparse=True)),
#                ('trans_tfidf', TfidfTransformer())])),
        ])),
    ('est', linear_model.Ridge())
])

# training the model
y_train = X_train[u'ClosePrice']
est_new.fit(X_train, y_train)

# testing the model
y_test = X_test[u'ClosePrice']
print "score", est_new.score(X_train, y_train)

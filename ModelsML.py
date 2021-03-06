# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:13:57 2019

@author: alanq
"""

import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from scipy.stats import linregress
import pandas as pd

tb = pd.read_excel (r'C:\Users\alanq\.spyder-py3\tb_gene_data.xlsx') 
print(tb.shape)

#Linear Regression Modeling
tb.cov()
tb.groupby('dst').cov()>0.2
array = tb.values
X = array[:,:-1]
print(X)
Y = array[:,:1]
print(Y)
X=X.astype('int')
Y=Y.astype('int')
linregress(X,Y)
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


from sklearn.svm import SVC
from cvxopt import matrix as cvxopt_matrix
from cvxopt import solvers as cvxopt_solvers

df=pd.read_excel('proj2dataset.xlsx')

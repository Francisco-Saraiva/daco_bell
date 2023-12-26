#Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Importing the dataset
dataset = pd.read_csv('star_classification.csv')
print(dataset.info())

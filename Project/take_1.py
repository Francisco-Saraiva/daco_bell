#Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Importing the dataset
dataset = pd.read_csv('./Project/star_classification.csv')
print(dataset.info())

# Changing class from string to int
dataset['class'] = [1 if i == "GALAXY" else 2 if i == "STAR" else 3 for i in dataset["class"]]
print(dataset.info())

# Count of each class
print(dataset["class"].value_counts())

# Plot the count
sns.countplot(dataset["class"])
plt.title("Class ", fontsize=10)
plt.show()


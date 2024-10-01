
import pandas as pd
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from check import DataChecker
from loader import DataLoader
from graph import graph


        
file_path = "G:/projects/PythonApplication2/UltimateClassicRock.csv"  
loader = DataLoader(file_path)
data = loader.loadcsv()

print (data.head(10))
checker=DataChecker(data)
checker.count_missing_values()
checker.replace()

graph=graph(data)
graph.histogramm(columns=['Year','Tempo','Duration'], bins=100)
graph.linnear(x_columns=['Year'],y_columns=['Tempo','Popularity'])
graph.box(columns=['Year','Duration','Loudness'])
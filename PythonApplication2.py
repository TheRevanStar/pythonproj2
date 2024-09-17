import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class graph:
   def __init__ (self,data:pd.DataFrame):
         self.data=data
         


def plot_histogram(data, column_name, bins=10):
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column_name], bins=bins, kde=False, color='blue')
    plt.title(f'Гистограмма для {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Частота')
    plt.show()

def plot_boxplot(data, column_name):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data, x=column_name, color='lightblue')
    plt.title(f'Ящик с усами для {column_name}')
    plt.xlabel(column_name)
    plt.show()
    
def plot_scatter(data, x_column, y_column):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data[x_column], y=data[y_column], color='green')
    plt.title(f'Диаграмма рассеяния {y_column} от {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
    

def plot_pie(data, column_name):
    plt.figure(figsize=(8, 6))
    data[column_name].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.title(f'Круговая диаграмма для {column_name}')
    plt.ylabel('')  
    plt.show()
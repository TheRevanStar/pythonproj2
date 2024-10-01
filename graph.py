import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
class graph:
   def __init__(self, data):
       
        if isinstance(data, str):
        else:
            self.data = pd.DataFrame(data)
   def histogramm(self,columns,bins):
     plt.figure(figsize=(10,6))
     for column in columns:
        if column in self.data:
            self.data[column].hist(alpha=1,label=column,bins=bins)
     plt.title(f'hist for column{columns}',fontsize=16)  
     plt.xlabel(columns)
     plt.ylabel('freq')
     plt.legend
     plt.grid()
     plt.tight_layout()
     plt.show()   
   def linnear(self,x_columns,y_columns):
     plt.figure(figsize=(10,6))
     for column in y_columns:
        if column in self.data:
          plt.plot(self.data[x_columns],self.data[column], label=column , marker='o')
     plt.title(f'linnear for column{x_columns,y_columns}',fontsize=16) 
     plt.xlabel(x_columns)
     plt.ylabel('freq')
     plt.legend
     plt.grid()
     plt.tight_layout()
     plt.show() 
   def box(self,columns):
     sns.set(style="whitegrid")   
     for column in columns:
        plt.figure(figsize=(10,6))
        sns.boxplot(x=self.data[column])
        plt.title(f'Boxplot for column{column}',fontsize=16)
        plt.show()
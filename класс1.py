import pandas as pd
class my_class:
      
      def __init__(self, data=pd.data):
        self.data=data
        
def checker(self,data):
    return data.isnul().sum()

def replace (self,data):
    
    othercol=  self.data.select_dtypes(include=['object', 'category']).columns 
    numcol= self.data.select_dtypes(include=['number']).columns 
    for col in numcol:
           self.data[col]= self.data[col].fillna(self.data[col].median())

    for col in othercol:
        self.data[col]= self.data[col].fillna(self.data[col].mode()[0])

def report_missing_values(self):
        
        missing_values = self.count_missing_values()
        print(missing_values)
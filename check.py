import pandas as pd

class DataChecker:
      
      def __init__(self, data):
        self.data=pd.DataFrame(data)

      def replace (self):
    
        othercol=  self.data.select_dtypes(include=['object', 'category']).columns 
        numcol= self.data.select_dtypes(include=['number']).columns 
        for col in numcol:
               self.data[col]= self.data[col].fillna(self.data[col].median())

        for col in othercol:
            self.data[col]= self.data[col].fillna(self.data[col].mode()[0])


      def count_missing_values(self):
        print(self.data.isnull().sum())
        return self.data.isnull().sum()

   
    
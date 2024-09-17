
import pandas as pd

class DataLoader:
      
      def __init__(self, file_path):
        self.file_path = file_path
      
def loadcsv(self):
    if self.file_path.endswith('.csv'):
        data = pd.read_csv(self.file_path)
        return data
    elif self.file_path.endswith('.xlsx'):  
        data = pd.read_excel(self.file_path)  
        return data
    elif self.file_path.endswith('.json'):
        data = pd.read_json(self.file_path)
        return data
    
 
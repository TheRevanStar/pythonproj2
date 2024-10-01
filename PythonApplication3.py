
import pandas as pd
import chardet
import sqlite3
import matplotlib.pyplot as plt
def linnear_games_vs_value(data, x_column, y_column):
    plt.figure(figsize=(12, 6))
    
 
    grouped_data = data.groupby(x_column)[y_column].sum().reset_index()
    
 
    grouped_data = grouped_data.sort_values(by=y_column, ascending=False)
    
 
    plt.plot(grouped_data[x_column], grouped_data[y_column], label=y_column, marker='o', linestyle='-', color='b')

    plt.title(f'Games vs {y_column}', fontsize=16)
    plt.xlabel(x_column.capitalize())
    plt.ylabel(y_column.capitalize())
    
   
    plt.xticks(rotation=90)
    
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


df = pd.read_csv("G:\projects\PythonApplication3\steam-200k.csv")

print(df.head(5))

df.columns = ['user_id', 'game', 'action', 'value', 'unknown']

df_clean = df[['user_id', 'game', 'action', 'value']]

conn = sqlite3.connect('steam_data.db')
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS steam_data (
    user_id INTEGER,
    game TEXT,
    action TEXT,
    value REAL
);
'''
cursor.execute(create_table_query)


df_clean.to_sql('steam_data', conn, if_exists='append', index=False)
cur = conn.cursor()
cur.execute("SELECT * FROM steam_data")
rows = cur.fetchmany(20)

        
for row in rows:
 
      print(row)

conn.commit()
conn.close()

print(conn)

most_common_game = df_clean['game'].value_counts().idxmax()
most_common_action = df_clean['action'].value_counts().idxmax()
most_common_value = df_clean['value'].value_counts().idxmax()

total_records = df_clean['value'].count()
total_sum_value = df_clean['value'].sum()
average_value = df_clean['value'].mean()

print(most_common_game , most_common_action, most_common_value, total_records, total_sum_value, average_value)

linnear_games_vs_value(data=df_clean, x_column='game', y_column='value')
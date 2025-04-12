import pandas as pd
import psycopg2

# Configuration 
excel_file_path=r'C:\Users\Ei Kay Khine Mon\Downloads\GBS\PowerBI\normalized\01\2016_01_customer' \
'.xlsx';
table_name='monthlysales.d_customer';
db_config={
    'host':'localhost',
    'port':'5432',
    'dbname':'monthlysales',
    'user':'postgres',
    'password':'admin'
}

# load data
# njkjhj
df=pd.read_excel(excel_file_path);

# connect to pgsql
conn=psycopg2.connect(**db_config);
cur=conn.cursor();

# Insert data
for i,row in df.iterrows():
    columns=','.join(df.columns)
    values=','.join(['%s']*len(row))
    insert_query=f'INSERT INTO {table_name}({columns}) VALUES({values})'
    cur.execute(insert_query,tuple(row))

# commit and close
conn.commit();
cur.close();
conn.close();

print("data loaded successfully")
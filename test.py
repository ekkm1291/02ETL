import os

folder_path = "D://02ETL//monthly_sales_version2"

files = os.listdir(folder_path)

for file in files:
    print(folder_path + '//' + file)
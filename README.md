# JSON Staff Data Assignment

## 📌 Project Overview
This project demonstrates how to fetch employee data from a public GitHub URL using Python, convert the JSON data into a pandas DataFrame, display the first 100 records, and export the cleaned data into a CSV file.

---

# Step-by-Step Process

## Step 1: Generate the Dataset
I began by visiting Mockaroo and generating a synthetic staff dataset in JSON format.

The dataset contained:
- First Name
- Last Name
- Department
- Salary
- Employee ID

The dataset had:
- 1000 rows
- 5 columns

After generating the dataset, I downloaded the file and renamed it as Staff_Datapracitce.json

## Step 2: Upload Dataset to GitHub
I created a new GitHub repository called, 'Introduction-to-Python-Assignment'

I then uploaded the renamed JSON dataset into the repository and committed the changes.

The raw GitHub URL used in the Python script was:
https://raw.githubusercontent.com/reinhard237/Introduction-to-Python-Assignment/refs/heads/main/Staff_Datapracitce.json

## Step 3: Create the Python Script
I created a Python file called: Json_assignment.py
Inside the script, I imported the required libraries:
import requests
import pandas as pd

## Step 4: Fetch Data from GitHub
Using the requests library, I fetched the JSON data from GitHub:
staff_url = "https://raw.githubusercontent.com/reinhard237/Introduction-to-Python-Assignment/refs/heads/main/Staff_Datapracitce.json"

staff_content = requests.get(staff_url)

I then checked the response status code:
print(staff_content.status_code)

## Step 5: Convert JSON Data
I converted the JSON response into Python data using the .json() method:
staff_data = staff_content.json()

I also checked the data type:
print(type(staff_data))

## Step 6: Create a Pandas DataFrame
Using pandas, I converted the JSON data into a DataFrame:
staff_df = pd.DataFrame(staff_data)

## Step 7: Display the First 100 Records
To display only the first 100 rows, I used: 
print(staff_df.head(100))

I then stored the first 100 records in a new DataFrame:
sample_df_100 = staff_df.head(100)

## Step 8: Export Data to CSV
Finally, I exported the first 100 records into a CSV file:
sample_df_100.to_csv("sample_data.csv", index=False)

The index=False parameter was used to prevent pandas from adding row numbers as an extra column in the CSV file.

## Tools Used included;
-Python
-Pandas
-Requests Library
-VS Code
-GitHub
-Mockaroo.com

## Project Files
json_assignment.py - Python script
Staff_Datapracitce.json - Raw JSON dataset
sample_data.csv - Exported CSV file
README.md - Project documentation

## Project Outcome
Successfully:
-fetched JSON data from GitHub.
-converted the data into a pandas DataFrame.
-displayed the first 100 records.
-exported the processed data into a CSV file.
-documented the complete workflow using GitHub and VS Code.

# DummyJSON API Data Project

## Overview
This project demonstrates how to extract data from a public API using Python.

## Tools Used
- Python
- Requests library
- Pandas

## APIs Used
- Products: https://dummyjson.com/products
- Carts: https://dummyjson.com/carts

## Process
Step 1. Sent API requests using `requests.get()`
Step 2. Extracted JSON data
Step 3. Converted data into Pandas DataFrames
Step 4. Exported results to CSV files

## Output Files
- products_data.csv
- carts_data.csv

## Skills Demonstrated
- API integration
- JSON parsing
- Data transformation
- Data export using Pandas
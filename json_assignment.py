print("=== JSON ASSIGNMENT ===")
import requests
#1). Fetch data from a publc API and display it in a readable format.
import pandas as pd

staff_url = "https://raw.githubusercontent.com/reinhard237/Introduction-to-Python-Assignment/refs/heads/main/Staff_Datapracitce.json"
staff_content = requests.get(staff_url)
print(staff_content.status_code)

#To get data, I used .json() method
staff_data = staff_content.json()
print(staff_data)
type(staff_data)
print(type(staff_data))

#To slice the data, I used pandas library; I want to slice the first 100 records and display the records.
staff_df = pd.DataFrame(staff_data)
print(staff_df.head(100))
sample_df_100 = staff_df.head(100)
# Converting the data to a csv file
sample_df_100.to_csv("sample_data.csv", index=False)
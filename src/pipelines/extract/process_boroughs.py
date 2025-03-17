import requests
import os

# Directory path you want to check and create
data_raw_directory = r'..\..\..\data\open-intro\raw'
data_raw_path = fr'{data_raw_directory}\london_boroughs.csv'
download_link = 'https://data.london.gov.uk/download/ordnance-survey-code-point/7c07780f-0532-4259-9e92-7e861d5b93c3/CodePointOpen_London_201709.csv'

# Check if the directory exists
if not os.path.exists(data_raw_directory):
    os.makedirs(data_raw_directory)

headers = {
    'Accept': 'text/csv'  # Specify CSV as the desired content type
}

response = requests.get(download_link, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Open a file in write-binary mode and save the content
    with open(data_raw_path, 'wb') as file:
        file.write(response.content)
    print("CSV file has been saved successfully.")
else:
    print(f"Failed to download the file. HTTP Status code: {response.status_code}")

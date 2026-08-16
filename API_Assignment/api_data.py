import requests
import pandas as pd

# Public API URL
url = "https://jsonplaceholder.typicode.com/users"

# Send GET request
response = requests.get(url)

# Check whether request was successful
if response.status_code == 200:
    data = response.json()
    print("JSON Response:")
    print(data)

    # Convert JSON data into DataFrame
    df = pd.DataFrame(data)

    # Save data as CSV
    df.to_csv("api_data.csv", index=False)

    print("API data successfully extracted.")
    print(df)
    print("\nCSV file created successfully.")
else:
    print("API request failed.")
    print("Status code:", response.status_code)
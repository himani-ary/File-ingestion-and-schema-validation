import pandas as pd
import yaml

# Load the config file
with open('config.yaml', 'r') as config_file:
    config_data = yaml.safe_load(config_file)

try:
    # Read the CSV file based on the config settings
    file_type = config_data['file_type']
    source_file = "./" + config_data['file_name'] + f'.{file_type}'
    df = pd.read_csv(source_file, config_data['inbound_delimiter'])

    # Validation of header columns
    expected_columns = config_data.get('expected_columns', [])
    actual_columns = df.columns.tolist()

    if set(expected_columns) == set(actual_columns):
        print("Header validation passed!")
    else:
        print("Header validation failed. Missing or incorrect columns.")
        print("Expected Columns:", expected_columns)
        print("Actual Columns:", actual_columns)

    # Display the first few rows of the DataFrame
    print(df.head())
except FileNotFoundError:
    print(f"Error: File '{source_file}' not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty or contains no data.")
except pd.errors.ParserError:
    print("Error: There was an issue parsing the CSV file. Check the format and delimiter.")
except Exception as e:
    print("An unexpected error occurred:", str(e))


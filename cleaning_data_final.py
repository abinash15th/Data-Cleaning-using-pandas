import pandas as pd

if __name__ == '__main__':
    # Override default pandas configuration
    pd.options.display.width = 0
    pd.options.display.max_rows = 10000
    pd.options.display.max_info_columns = 10000

    # Open example data.
    df = pd.read_csv('employee_data.csv')

    # Cast types to save memory.
    df['gender'] = df['gender'].astype('category')
    df['employment_status'] = df['employment_status'].astype('category')
    df['birth_date'] = df['birth_date'].astype('datetime64')

    # Rename columns
    df.rename(columns={'number': 'staff_id'}, inplace=True)

    # Print some initial information about the DataFrame
    print(df.info())
    print(df.describe(include='all', datetime_is_numeric=True))

    # Show how many null values for each column
    print(df.isnull().sum())

    # Calculate the percentage of missing values as a whole.
    rows, columns = df.shape
    cell_count = rows * columns
    number_of_nulls = df.isnull().sum().sum()
    percentage_of_missing = (number_of_nulls / cell_count) * 100
    print(f'Percentage of missing values: {percentage_of_missing}%')

    # Drop any columns that contain only null values.
    df.dropna(axis='columns', how='all', inplace=True)
    print(df.info())

    # Check to see if any rows have less than 2 elements.
    under_threshold_removed = df.dropna(axis='index', thresh=2, inplace=False)
    under_threshold_rows = df[~df.index.isin(under_threshold_removed.index)]
    print(under_threshold_rows)

    # Drop rows with less than two elements.
    df.dropna(axis='index', thresh=2, inplace=True)
    print(df.info())

    # Set a default category for missing genders.
    df['gender'].cat.add_categories(new_categories=['U'], inplace=True)
    df.fillna(value={'gender': 'U'}, inplace=True)
    print(df['gender'].value_counts())
    df.reset_index(inplace=True)

    # Renaming DataFrame categories.
    df['gender'].cat.rename_categories(new_categories={'M': 'Male', 'F': 'Female', 'U': 'Unknown'},
                                       inplace=True)
    print(df['gender'].value_counts())

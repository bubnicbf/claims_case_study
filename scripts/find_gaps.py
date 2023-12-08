"""
A Python script is designed to analyze medical claims data to identify significant gaps in claim dates. A gap is defined as a signifiant period where no claims were made by a provider. The code allows users to set a threshold for what constitutes a significant gap (e.g., 30 days or more). The script pulls data from an AWS S3 bucket, processes it, and outputs a report of these gaps.

Assumptions:
- Downloads claims data directly from an S3 bucket
- S3 connection info is housed in separate config
- Significant gap threshold is hard-coded value below

Output:
- Provider identifier
- End date of the previous claim
- Start date of the next claim
- Length of the gap in days

"""    

import pandas as pd
import boto3
import configparser

def load_aws_config(filepath):
    """
    Loads AWS configuration from a properties file.

    :param filepath: Path to the configuration file.
    :return: Dictionary with AWS credentials and S3 details.
    """
    creds = configparser.ConfigParser()
    creds.read(filepath)
    return {
        'access_key': creds.get('AWS', 'AccessKey'),
        'secret_access_key': creds.get('AWS', 'SecretAccessKey'),
        'bucket_name': creds.get('AWS', 'BucketName'),
        'file_name': creds.get('AWS', 'FileName')
    }

def download_from_s3(bucket, file, local_path, s3_client):
    """
    Downloads a file from S3 to a local path.

    :param bucket: Name of the S3 bucket.
    :param file: Name of the file to download.
    :param local_path: Local path to save the file.
    :param s3_client: Initialized boto3 S3 client.
    """
    try:
        s3_client.download_file(bucket, file, local_path)
    except Exception as e:
        print(f"Error downloading file from S3: {e}")

def find_gaps(data, threshold):
    # Finds gaps in medical claims data based on a number of days threshold.
    gaps = []
    for provider in data['Provider'].unique():
        provider_data = data[data['Provider'] == provider]
        for i in range(len(provider_data) - 1):
            end_date = provider_data.iloc[i]['EndDate']
            next_start_date = provider_data.iloc[i + 1]['StartDate']
            gap_length = (next_start_date - end_date).days
            if gap_length >= threshold:
                gaps.append((provider, end_date, next_start_date, gap_length))
    return gaps

# Load data from S3 using config file
config = load_aws_config('../aws_credentials.properties')
session = boto3.Session(
    aws_access_key_id=config['access_key'], 
    aws_secret_access_key=config['secret_access_key']
)
s3_client = session.client('s3')
download_from_s3(config['gaps_bucket_name'], config['gaps_file_name'], 'temp_file.csv', s3_client)

# Load into a DataFrame
try:
    df = pd.read_csv('temp_file.csv')
except Exception as e:
    print(f"Error reading the data file: {e}")
    exit()

# Convert dates to datetime and sort the DataFrame
df['StartDate'] = pd.to_datetime(df['StartDate'])
df['EndDate'] = pd.to_datetime(df['EndDate'])
df = df.sort_values(by=['Provider', 'StartDate'])

# Define a threshold for significance
gap_threshold = 30  # for example

# Find the significant gaps
gaps = find_gaps(df, gap_threshold)

# Move into DataFrame and print to console
gaps_df = pd.DataFrame(gaps, columns=['Provider', 'End of Previous Claim', 'Start of Next Claim', 'Gap Length (Days)'])
print(gaps_df)

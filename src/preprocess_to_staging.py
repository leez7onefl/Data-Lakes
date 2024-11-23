# Previous TP Code:

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
import tqdm
import joblib
from collections import OrderedDict


def preprocess_data(data_file, output_dir):
    """
    Preprocesses the raw data for model training and evaluation.

    Objectives:
    1. Load raw data from a CSV file.
    2. Clean the data (e.g., drop missing values).
    3. Encode categorical labels (`family_accession`) into integers.
    4. Split the data into train, dev, and test sets.
    5. Save preprocessed datasets and metadata.

    Steps:
    - Load the data with `pd.read_csv`.
    - Handle missing values using `dropna`.
    - Encode `family_accession` using `LabelEncoder`.
    - Split the data into train/dev/test using a manual approach.
    - Save the processed datasets (train.csv, dev.csv, test.csv) and class weights.

    Parameters:
    data_file (str): Path to the raw CSV file.
    output_dir (str): Directory to save the preprocessed files and metadata.
    """
    # Load the data
    print('Loading Data...')
    data = pd.read_csv(data_file)

    # Handle missing values
    data = data.dropna()

    # Encode the family_accession column
    label_encoder = LabelEncoder()
    data['class_encoded'] = label_encoder.fit_transform(data['family_accession'])

    # Save label encoder mapping
    joblib.dump(label_encoder, f"{output_dir}/label_encoder.joblib")

    # Prepare label mapping
    label_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
    with open(f"{output_dir}/label_mapping.txt", 'w') as f:
        for key, value in label_mapping.items():
            f.write(f"{key}: {value}\n")

    # Manual train/dev/test split logic
    print("Splitting data into train, dev, and test sets...")
    family_accession = data['family_accession'].values
    class_encoded = data['class_encoded'].values

    unique_classes, class_counts = np.unique(family_accession, return_counts=True)

    train_indices, dev_indices, test_indices = [], [], []

    for cls in tqdm.tqdm(unique_classes):
        class_data_indices = np.where(family_accession == cls)[0]
        count = len(class_data_indices)

        if count == 1:
            test_indices.extend(class_data_indices)
        elif count == 2:
            dev_indices.extend(class_data_indices[:1])
            test_indices.extend(class_data_indices[1:])
        elif count == 3:
            train_indices.extend(class_data_indices[:1])
            dev_indices.extend(class_data_indices[1:2])
            test_indices.extend(class_data_indices[2:])
        else:
            train_part, remaining = train_test_split(class_data_indices, test_size=2 / 3, random_state=42)
            dev_part, test_part = train_test_split(remaining, test_size=0.5, random_state=42)
            train_indices.extend(train_part)
            dev_indices.extend(dev_part)
            test_indices.extend(test_part)

    # Convert indices lists to numpy arrays
    train_indices = np.array(train_indices)
    dev_indices = np.array(dev_indices)
    test_indices = np.array(test_indices)

    # Create and save train, dev, and test DataFrames
    train_data = data.iloc[train_indices]
    dev_data = data.iloc[dev_indices]
    test_data = data.iloc[test_indices]

    train_data.to_csv(f"{output_dir}/train.csv", index=False)
    dev_data.to_csv(f"{output_dir}/dev.csv", index=False)
    test_data.to_csv(f"{output_dir}/test.csv", index=False)

    # Compute class weights and save them
    class_counts = train_data['class_encoded'].value_counts()
    class_weights = 1. / class_counts
    class_weights /= class_weights.sum()

    full_class_weights = {i: class_weights.get(i, 0.0) for i in range(max(class_counts.index) + 1)}
    with open(f"{output_dir}/class_weights.txt", 'w') as f:
        for key, value in full_class_weights.items():
            f.write(f"{key}: {value}\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Preprocess protein data")
    parser.add_argument("--data_file", type=str, required=True, help="Path to raw CSV file")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save preprocessed data")
    args = parser.parse_args()

    preprocess_data(args.data_file, args.output_dir)

#######################################################
# Task: Modify this code to achieve the following:
# 1. Instead of reading the raw data from a local CSV file, download it from the `raw` bucket in LocalStack using the `boto3` library.
# 2. Upload the processed train, dev, and test splits to the `staging` bucket in LocalStack instead of saving them locally.
# 3. Accelerate the manual train/dev/test split logic by making it numpy only and compiling the code with numba.
#    I suggest you isolate the train/dev/test split code into a function, and use the @njit decorator from numba to compile it and then call in
#    in the preprocess function
# 4. Update the command-line arguments to:
#    - Replace `--data_file` with `--bucket_raw` and `--input_file` for S3 integration.
#    - Replace `--output_dir` with `--bucket_staging` and `--output_prefix` for S3 integration.

# Hints:
# - Use `boto3` to download raw data:
#   ```python
#   s3 = boto3.client(find the right parameters)
#   response = s3.get_object(Bucket=bucket_raw, Key=input_file)
#   data = pd.read_csv(io.BytesIO(response['Body'].read())) # Use this to read the data from the remote bucket.
#   ```

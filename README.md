## Data Lakes & Data Integration 

This repository is designed to help students learn about data lakes and data integration pipelines using Python, Docker, LocalStack, and DVC. Follow the steps below to set up and run the pipeline.

---

## 1. Prerequisites

### Install Docker
Docker is required to run LocalStack, a tool simulating AWS services locally.

1. Install Docker:
```bash
sudo apt update
sudo apt install docker.io
```

2. Verify Docker installation:
```bash
docker --version
```

3. Install AWS CLI
AWS CLI is used to interact with LocalStack S3 buckets.

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

4. Verify that the installation worked

```bash
aws --version
```

5. Configure AWS CLI for LocalStack

```bash
aws configure
```

Enter the following values:
* AWS Access Key ID: root
* AWS Secret Access Key: root
* Default region name: us-east-1
* Default output format: json

6. Create LocalStack S3 buckets:

```bash
Copier le code
aws --endpoint-url=http://localhost:4566 s3 mb s3://raw
aws --endpoint-url=http://localhost:4566 s3 mb s3://staging
aws --endpoint-url=http://localhost:4566 s3 mb s3://curated
```

7. Install DVC
DVC is used for data version control and pipeline orchestration.

```bash
pip install dvc
```

```bash
dvc remote add -d localstack-s3 s3://
dvc remote modify localstack-s3 endpointurl http://localhost:4566
```

## 2. Repository Setup
Install Python Dependencies

```bash
pip install -r build/requirements.txt
```

Start LocalStack

```bash
bash scripts/start_localstack.sh
```

Download the Dataset

```bash
pip install kaggle 
kaggle datasets download googleai/pfam-seed-random-split
```

Move the dataset into a data/raw folder.

## 3. Running the Pipeline

Unpack the dataset into a single CSV file in the raw bucket:

```bash
python src/unpack_data.py --input_dir data/raw --bucket_name raw --output_file_name combined_raw.csv
```

Preprocess the data to clean, encode, split into train/dev/test, and compute class weights:

```bash
python src/preprocess_to_staging.py --bucket_raw raw --bucket_staging staging --input_file combined_raw.csv --output_prefix preprocessed
```

Prepare the data for model training by tokenizing sequences:

```bash
python src/process_to_curated.py --bucket_staging staging --bucket_curated curated --input_file preprocessed_train.csv --output_file tokenized_train.csv
```

## 4. Running the Entire Pipeline with DVC
The pipeline stages are defined in dvc.yaml. Run the pipeline using:

```bash
dvc repro
```

## 5. Notes
Ensure LocalStack is running before executing any pipeline stage.
This pipeline illustrates a basic ETL flow for a data lake, preparing data from raw to curated for AI model training.
If you encounter any issues, ensure Docker, AWS CLI, and DVC are correctly configured.


---
# WINDOWS INSTALLATION
---

## Data Lakes & Data Integration

This repository is designed to help students learn about data lakes and data integration pipelines using Python, Docker, LocalStack, and DVC. Follow the steps below to set up and run the pipeline on Windows.

---

## 1. Prerequisites

### Install Docker Desktop
Docker is required to run LocalStack, a tool simulating AWS services locally.

1. Install Docker Desktop for Windows from the [Docker website](https://www.docker.com/products/docker-desktop).
2. After installation, ensure Docker Desktop is running properly and has been configured to use WSL 2 (if applicable).

3. Verify Docker installation in Command Prompt or PowerShell:
   ```shell
   docker --version
   ```

### Install AWS CLI
AWS CLI is used to interact with LocalStack S3 buckets.

1. Download the AWS CLI MSI installer for Windows from the [AWS CLI website](https://aws.amazon.com/cli/).
2. Run the installer and follow the on-screen instructions.
3. Verify the AWS CLI installation:

   ```shell
   aws --version
   ```

4. Configure AWS CLI for LocalStack

   ```shell
   aws configure
   ```

   Enter the following values:
   * AWS Access Key ID: root
   * AWS Secret Access Key: root
   * Default region name: us-east-1
   * Default output format: json

5. Create LocalStack S3 buckets using the Command Prompt or PowerShell:

   ```shell
   aws --endpoint-url=http://localhost:4566 s3 mb s3://raw
   aws --endpoint-url=http://localhost:4566 s3 mb s3://staging
   aws --endpoint-url=http://localhost:4566 s3 mb s3://curated
   ```

### Install DVC
DVC is used for data version control and pipeline orchestration.

1. Install DVC via pip in Command Prompt or PowerShell:
   ```shell
   pip install dvc
   ```

2. Set up DVC remote for LocalStack S3:
   ```shell
   dvc remote add -d localstack-s3 s3://
   dvc remote modify localstack-s3 endpointurl http://localhost:4566
   ```

## 2. Repository Setup
Install Python Dependencies

1. Use Command Prompt or PowerShell to install dependencies:
   ```shell
   pip install -r build/requirements.txt
   ```

2. Start LocalStack
   - You might need to run a batch file or use Command Prompt/PowerShell directly to start LocalStack. Alternatively, if it's a bash script, you can use WSL or Git Bash to execute:

   ```bash
   # If you are using Git Bash or WSL
   bash scripts/start_localstack.sh
   ```

3. Download the Dataset

   - First, ensure you have your Kaggle API credentials set up according to Kaggle's instructions.
   - Then, install Kaggle and download the dataset:

   ```shell
   pip install kaggle
   kaggle datasets download googleai/pfam-seed-random-split
   ```

4. Move the dataset into a `data/raw` folder using File Explorer or Command Prompt.

## 3. Running the Pipeline

Unpack the dataset into a single CSV file in the raw bucket:

```shell
python src/unpack_data.py --input_dir data/raw --bucket_name raw --output_file_name combined_raw.csv
```

Preprocess the data to clean, encode, split into train/dev/test, and compute class weights:

```shell
python src/preprocess_to_staging.py --bucket_raw raw --bucket_staging staging --input_file combined_raw.csv --output_prefix preprocessed
```

Prepare the data for model training by tokenizing sequences:

```shell
python src/process_to_curated.py --bucket_staging staging --bucket_curated curated --input_file preprocessed_train.csv --output_file tokenized_train.csv
```

## 4. Running the Entire Pipeline with DVC
The pipeline stages are defined in `dvc.yaml`. Run the pipeline using:

```shell
dvc repro
```

## 5. Notes
Ensure LocalStack is running before executing any pipeline stage.
This pipeline illustrates a basic ETL flow for a data lake, preparing data from raw to curated for AI model training.
If you encounter any issues, ensure Docker, AWS CLI, and DVC are correctly configured.

---

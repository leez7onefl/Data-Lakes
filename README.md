# Data Lakes & Data Integration 

## 1. Build the Repo

### Install the Requirements
Install the necessary packages using the requirements file found in the `build` folder:
```bash
pip install -r build/requirements.txt
```

### Download the Data

Download the dataset from the following [link](https://www.kaggle.com/api/v1/datasets/download/googleai/pfam-seed-random-split).

***Note**: It is possible to download the dataset using the Kaggle API, but this requires you to be logged in, which may make the process longer. To use the Kaggle API, follow these steps:*

#### A - Ensure you have the Kaggle CLI installed:
```bash
pip install kaggle
```

#### B - Authenticate with Kaggle by placing your kaggle.json file (containing your API credentials) in the ~/.kaggle/ directory.


#### C - Use the following command to download the dataset:
```bash
kaggle datasets download googleai/pfam-seed-random-split
```

### Organize the Data
Move the contents of the dataset (train, dev, test, random_split) to a data/bronze/ folder.

### Unpack the Data
Unpack the data using the unpack_data.py script found in the build folder.
```bash
python build/unpack_data.py --input_dir data/bronze/ --output_file data/bronze/combined_data.csv
```

## 2. Data Analysis
A quick data analysis is at your disposal to help you understand the data in the *data_analysis.ipynb* notebook. Your goal should be to understand the data, and why the transformations suggested in src/preprocess.py need to be made.

## 3. Data Pre-processing
Data needs to be preprocessed to be stage from a bronze to a silver layer. Your preprocessing script should drop rows with missing values if they exist, encode labels, split data across train/dev/test sets, drop columns and save class weights for training.

```bash
python src/preprocess.py --data_file data/bronze/combined_data.csv --output_dir data/silver/
```

## 4. Train and Evaluate

The training script is train.py located at the root of the repo. The PyTorch Lightning implementation of each model can be found in *src/models/*. The Protein Dataset Lightning implementation can be found in *src/dataset.py*.

In *src/models/*, *transformers_module.py* is a Lightning wrapper for the Huggingface Transformers library to work with a PyTorch Lightning trainer.

### Available Models:
* baseline: Linear Classifier
* esm2: QLoRA fine-tuning of ESM-2-8M in 8-bit. *Targets only query/key/value layers and not dense layers to reduce compute load*.
* ropeformer: (Not fully implemented yet) My custom implementation of a Transformer with Rotary Position Embeddings

To train a model, go to the hydra config at *config/config.yaml*, and indicate the model you wish to train under model.name. Then, simply run the training script.
```bash
python train.py
```

## 5. Next steps

* Automate project build with Makefile

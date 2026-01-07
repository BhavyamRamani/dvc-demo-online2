# DVC Data Ingestion Demo

## Overview
This repository demonstrates a simple data ingestion workflow using **DVC (Data Version Control)**. The project focuses on downloading a remote dataset, applying basic preprocessing, and tracking the processed data using DVC for reproducibility and version control.

The goal of this project is to showcase how datasets can be versioned and managed independently of code using DVC.

---

## Project Structure
dvc-demo-online2-main/
│
├── .dvc/
│   ├── config
│   └── .gitignore

│
├── .dvcignore

│
├── data/
│   ├── customer.csv.dvc
│   └── .gitignore

│
├── src/
│   └── data_ingestion.py


---

## Data Ingestion
The data ingestion process is implemented in `src/data_ingestion.py` and performs the following steps:

1. Downloads a customer dataset from a remote GitHub source.
2. Loads the dataset into a Pandas DataFrame.
3. Applies basic preprocessing:
   - Removes the first three columns
   - Filters rows where `Length of Membership > 1`
   - Drops the `Avg. Session Length` column
4. Saves the processed dataset as `data/customer.csv`.

The resulting dataset is tracked using DVC.

---

## Dataset Tracking with DVC
- The processed dataset is tracked using DVC (`customer.csv.dvc`).
- The actual data file is ignored by Git and managed by DVC instead.
- This allows versioning of large datasets without storing them directly in the Git repository.

---

## How to Run

### Prerequisites
- Python
- DVC
- Pandas

### Run Data Ingestion
```bash
python src/data_ingestion.py

---
Purpose:
  This project serves as a minimal example of:
  Remote data ingestion
  Basic data preprocessing
  Dataset versioning using DVC

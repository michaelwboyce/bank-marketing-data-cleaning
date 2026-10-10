# Bank Marketing Campaign Data Cleaning

A reproducible **Python and pandas** data-cleaning pipeline that transforms a bank marketing dataset into three structured, analysis-ready CSV files. This project was completed as part of DataCamp's *Cleaning Bank Marketing Campaign Data* project.

## Project overview

The source data contains **41,188 campaign records**. The goal is to prepare the data for consistent downstream analysis and potential relational database ingestion by splitting it into three datasets and enforcing specific cleaning and type-conversion rules.

| Output file | Rows in the completed DataCamp run | Columns | Contents |
| --- | ---: | ---: | --- |
| `client.csv` | 41,188 | 7 | Client demographics, education, credit status, and mortgage status |
| `campaign.csv` | 41,188 | 7 | Contact activity, prior and current campaign outcomes, and last-contact date |
| `economics.csv` | 41,188 | 3 | Consumer price index and three-month Euribor |

All three outputs retain `client_id` so corresponding records can be joined later.

## Data transformations

- **Split** the original dataset into `client`, `campaign`, and `economics` DataFrames.
- **Standardize** `job` and `education` labels by replacing periods (`.`) with underscores (`_`).
- **Represent missing education** by converting `"unknown"` into `NaN`.
- **Encode Boolean columns** using explicit business rules:
  - `credit_default` and `mortgage`: `"yes"` → `True`; all other values → `False`.
  - `previous_outcome`: `"success"` → `True`; other recorded outcomes → `False`.
  - `campaign_outcome`: `"yes"` → `True`; `"no"` → `False`.
- **Construct** `last_contact_date` from a project-specified year of `2022` plus the source month and day, then parse into a pandas datetime.
- **Enforce** integer and floating-point types, validate the row counts, column counts, Boolean types, and datetime type, and **export** CSV files with `index=False`.

> **Data interpretation note:** The project explicitly treats `"unknown"` as `False` for credit-default and mortgage status. This is an assignment-specific rule, not a general recommendation for production financial analytics, where unknown status may warrant separate treatment.

## Project structure

```text
bank-marketing-data-cleaning/
├── bank_marketing_cleaning.py   # End-to-end cleaning pipeline
├── README.md                    # Documentation
├── requirements.txt             # Python dependencies
└── .gitignore                   # Excludes raw and generated data
```

## How to run

1. Use Python 3.9+ and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Download the `bank_marketing.csv` input from the corresponding DataCamp project environment and place it in this repository's working directory. The source dataset is **not included** here.
3. Execute:

   ```bash
   python bank_marketing_cleaning.py
   ```

4. After the validation checks pass, the script writes `client.csv`, `campaign.csv`, and `economics.csv` to the working directory. These generated outputs are also excluded from the repository.

## Tools and skills demonstrated

**Python · pandas · NumPy · Data cleaning · Missing-value handling · Type conversion · Datetime parsing · DataFrame validation · CSV export**

The completed DataCamp run reported successful validation and CSV creation. The row and column counts above describe that run, not a re-execution against the original dataset in this repository.

## Source and reproducibility

**Learning project:** DataCamp, *Cleaning Bank Marketing Campaign Data*.

The script is shared to demonstrate the transformation workflow. To reproduce the exact results, obtain the input dataset through DataCamp and follow the run instructions. No model training or predictive-performance claims are made for this project.

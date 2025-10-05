# SMS Phishing Detection (Toy Demo)

This repository is prepared as a deliverable for the Assignment-2 (Cyber Security, Chaitanya Bharathi Institute of Technology).
It demonstrates a small proof-of-concept SMS phishing detector (addresses the research gap: sparse research on SMS/Voice/Social phishing).

## Contents
- `data/sms_data.csv` : synthetic example SMS dataset (label,text)
- `data_prep.py` : simple preprocessing and dataset writer
- `train.py` : trains a TF-IDF + RandomForest pipeline and saves `models/sms_phish_pipeline.joblib`
- `predict.py` : simple CLI to predict on a custom message
- `results/eval_report.txt` : evaluation output (generated after running train.py)
- `report.md` : short report mapping to assignment requirements

## How to run (locally)
1. Create a Python virtual environment (recommended) and activate it.
2. `pip install -r requirements.txt`
3. `python data_prep.py`  # creates data/sms_data_prepped.csv
4. `python train.py`      # trains model and writes results/
5. `python predict.py "Your message here"`

## Notes
- This is a toy demo using a tiny synthetic dataset to demonstrate the approach. For the assignment, replace `data/sms_data.csv` with a real dataset (e.g., UCI SMS Spam Collection or a Kaggle phishing SMS dataset).
- Improve the model by: more data, hyperparameter tuning, class weighting, using more advanced text embeddings (BERT), adding metadata features (sender number pattern, presence of URL shorteners), and expanding to multimodal signals for social media.

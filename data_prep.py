import pandas as pd
import re
import os

def preprocess_text(s):
    s = s.lower()
    s = re.sub(r'http\S+', ' URL ', s)
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def load_and_prep(csv_path='data/sms_data.csv'):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=['text', 'label'])
    df['text_clean'] = df['text'].astype(str).apply(preprocess_text)
    return df[['label', 'text_clean']]

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    df = load_and_prep('data/sms_data.csv')
    df.to_csv('data/sms_data_prepped.csv', index=False)
    print('Wrote data/sms_data_prepped.csv with', len(df), 'rows')

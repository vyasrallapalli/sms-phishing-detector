import joblib
import os
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

os.makedirs('models', exist_ok=True)
os.makedirs('results', exist_ok=True)

df = pd.read_csv('data/sms_data_prepped.csv')
X = df['text_clean'].values
y = df['label'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2), min_df=1)),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

print('Training model...')
pipeline.fit(X_train, y_train)

print('Evaluating...')
y_pred = pipeline.predict(X_test)

report = classification_report(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print(report)
print('Confusion matrix:\n', cm)

# Save model and results
joblib.dump(pipeline, 'models/sms_phish_pipeline.joblib')
with open('results/eval_report.txt', 'w') as f:
    f.write('Classification report:\n')
    f.write(report)
    f.write('\nConfusion matrix:\n')
    f.write(str(cm))
print('Saved pipeline to models/sms_phish_pipeline.joblib and evaluation to results/eval_report.txt')

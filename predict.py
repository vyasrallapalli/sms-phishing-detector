import joblib
import sys

model_path = 'models/sms_phish_pipeline.joblib'
if len(sys.argv) < 2:
    print('Usage: python predict.py "message text here"')
    sys.exit(1)
text = sys.argv[1]
pipeline = joblib.load(model_path)
pred = pipeline.predict([text])
probs = pipeline.predict_proba([text]) if hasattr(pipeline, 'predict_proba') else None
print('Input:', text)
print('Predicted label:', pred[0])
if probs is not None:
    print('Probabilities:', probs[0])

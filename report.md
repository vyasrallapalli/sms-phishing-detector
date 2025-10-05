# Assignment-2 Report: SMS Phishing Detection (Toy Demo)

**Student:** [Your Name Here]
**Course:** Cyber Security (22CIE55)
**Faculty:** U Sairam
**Paper chosen:** Alkhalil et al., "Phishing Attacks: A Recent Comprehensive Study and a New Anatomy" (Frontiers in Computer Science, 2021)

## 1. Assignment requirements mapping
- Identify the research gap(s): See section 'Further investigations' in the chosen paper which lists: (1) study susceptibility, (2) research on social media/voice/SMS phishing, (3) laws and legislation, (4) source-determination. (See uploaded paper). 
- Provide your own analysis showing improvements: this repo implements a first-step SMS-phishing detection model (TF-IDF + RandomForest) as a demonstrator addressing gap (2).
- Keep code in GitHub: upload the repository root to your GitHub account (instructions in README).
- Submit a detailed report on methodology and results with screenshots: include evaluation outputs and screenshots of training/evaluation (placeholders in results/).

## 2. Identified Research Gap (from the paper)
The paper explicitly states that "Research on social media-based phishing, Voice Phishing, and SMS Phishing is sparse" and recommends this as an area for further research. (Cited in the provided paper.)

## 3. Proposed improvement (what I implemented)
- Implement a supervised machine-learning classifier to detect SMS phishing messages using textual features (TF-IDF).
- Rationale: SMS phishing (SMiShing) is rising but datasets and studies are fewer compared to email/web. An SMS-focused detector helps prevent user exposure on mobile devices.

## 4. Dataset
- For the demo: a tiny synthetic dataset (`data/sms_data.csv`) is included. For a real submission: use a larger labeled dataset (e.g., UCI SMS Spam Collection, PhishTank-derived SMS datasets, or collect labeled messages from OSINT sources).

## 5. Methodology
1. Preprocess SMS text (lowercase, remove URLs -> placeholder token `URL`, strip punctuation).
2. Convert to TF-IDF features (1-2 grams).
3. Train a RandomForest classifier.
4. Evaluate using hold-out test set; measure precision, recall, F1, and confusion matrix.

## 6. Results (demo)
- The repository contains `results/eval_report.txt` produced after running `train.py`.
- For your final submission, run training on a real dataset, capture screenshots of:
  - command-line outputs (training progress, evaluation metrics)
  - confusion matrix or plots
  - tables of precision/recall per class
  - code listing (repo view) and GitHub commit history

## 7. How this addresses the assignment & the research gap
- The paper calls for more research on SMS/social/voice phishing; this demo provides a reproducible starting point and code that can be expanded (more data, better features, deep learning).

## 8. Next steps / Suggestions to improve
- Collect a large labeled SMS phishing dataset.
- Use transfer learning / transformer models (BERT) for better semantics.
- Add metadata features (sender phone patterns, URL shortening detection, presence of OTP words).
- Evaluate on real-world SMS streams and measure false positive rate impact on usability.

## 9. Submission checklist
- [ ] Upload repository to your GitHub.
- [ ] Fill in the Google Form with GitHub link and attach this report as PDF.
- [ ] Include screenshots (training, evaluation) in your report before submission.

-- End of report --

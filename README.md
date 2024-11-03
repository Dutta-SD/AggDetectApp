---
title: AggDetectApp -- Detect Aggression and Misogyny
colorFrom: black
colorTo: blue
sdk: docker
app_file: app.py
pinned: false
python_version: 3.10.5
---

## Agression and Misogyny Detection App

Social media platforms have become hotspots for the proliferation of trolling, aggression, and hate speech. With an overwhelming volume of social media data being generated every day, manual inspection is simply impractical. In response to this pressing issue, we present an efficient and rapid method for detecting aggression and misogyny in online social media texts.

What sets our model apart is not only its high performance but also its significantly reduced training time, model size, and resource requirements. These advantages make our model highly practical for fast inference, ensuring prompt identification of aggression and misogyny in online social media texts.

> [Try it out here](https://huggingface.co/spaces/sdutta28/AggDetectApp)

_Since this is based on XGBoost + Tf-Idf, accuracy may not be so high. This can be improved by using LLMs_

### Features

- Detection of Aggression and Misogyny in texts
- LIME based prediction for explainability

### Tech Stack

- Python
- XgBoost
- Scikit-Learn
- HuggingFace Transformers
- LIME
- Docker

### Aggression Detection Results

| Metric   | Score |
| -------- | ----- |
| F1 Score | 0.735 |

### Misogyny Detection Results

| Metric   | Score |
| -------- | ----- |
| F1 Score | 0.852 |

## How to Run Locally

<!-- Installation and Running Steps -->

- Clone the repo
- Install python requirements using `$ pip install -r requirements.txt`
- Run the server using `$ python app.py`

## Additional Links

- [Try the App Here](https://huggingface.co/spaces/sdutta28/AggDetectApp)
- [[PDF] Paper published at ICON 2021](https://aclanthology.org/2021.icon-main.60.pdf)
- [Model training Repo](https://github.com/Dutta-SD/AggDetect)

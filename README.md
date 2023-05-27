---
title: AggDetectApp -- Detect Aggression and Misogyny
colorFrom: black
colorTo: blue
sdk: gradio
app_file: app.py
pinned: false
python_version: 3.7.0
---

# Agression and Misogyny Detection App
<!-- Intro and about the project -->
This app detects presence of Aggression and Misogyny in online social media texts. Try it out [here](https://huggingface.co/spaces/sdutta28/AggDetectApp)


## Technologies Used
<!-- Tech stack, libraries etc -->
`Python, Transformers, XgBoost, Scikit-Learn`


## Workflow
<!-- In some detail of how this works -->
- A text is given to the app
- It predicts aggression and misogyny in the application

## Results

### Aggression Detection Results
|Metric|Score|
|---|---|
|F1 Score|0.735|

### Misogyny Detection Results
|Metric|Score|
|---|---|
|F1 Score|0.852|


## How to Run
<!-- Installation and Running Steps -->
- Clone the repo
- Install python requirements using `$ pip install -r requirements.txt`
- Run the server using `$ python main.py`


## Additional Links
<!-- Kaggle model training links -->
- [[PDF] Paper published at ICON 2021](https://aclanthology.org/2021.icon-main.60.pdf)
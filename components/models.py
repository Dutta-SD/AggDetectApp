import joblib
from components.config import app_config
from lime.lime_text import LimeTextExplainer


# Takes in a string and outputs list
pipeline_task_A = joblib.load(app_config.TASK_A_MODEL_PATH)
pipeline_task_B = joblib.load(app_config.TASK_B_MODEL_PATH)

# LIME text explainer
explainer_task_A: LimeTextExplainer = LimeTextExplainer()
explainer_task_B: LimeTextExplainer = LimeTextExplainer()

import components.utils as utils
from components.config import app_config
from components.models import (
    pipeline_task_A,
    pipeline_task_B,
    explainer_task_A,
    explainer_task_B,
)
from lime.lime_text import LimeTextExplainer
from typing import Any
from matplotlib.figure import Figure


def predict_for_pipeline(
    model_pipeline: Any,
    explainer: LimeTextExplainer,
    cleaned_data: list[str],
    labels: list,
) -> tuple[int, Figure | None]:
    """Generates Prediction and Explanation given the cleaned text

    Args:
        model_pipeline (Any): Joblib imported model pipeline
        explainer (LimeTextExplainer): text explainer
        cleaned_data (list[str]): cleaned text
        labels(list): list of integers as labels

    Returns:
        tuple[int, Figure]: class prediction and LIME explanation as matplotlib figure
    """

    explanation = explainer.explain_instance(
        cleaned_data[0],
        model_pipeline.predict_proba,
        num_features=app_config.NUM_EXPLAINER_FEATURES,
        labels=labels,
    )

    class_prediction = model_pipeline.predict(cleaned_data)[0]
    return class_prediction, explanation.as_pyplot_figure(label=1)


def get_predictions(text: str) -> tuple:
    """Gets Predictions for the Texts

    Args:
        text (str): The input text to get predictions for

    Returns:
        tuple[str, Any]: Predictions for task A and task B
        along with Figures
    """

    cleaned_data = [utils.clean_one_text(text)]

    prediction_task_A = predict_for_pipeline(
        pipeline_task_A,
        explainer_task_A,
        cleaned_data,
        [0, 1, 2],
    )
    prediction_task_B = predict_for_pipeline(
        pipeline_task_B,
        explainer_task_B,
        cleaned_data,
        [0, 1],
    )

    print(prediction_task_A)
    print(prediction_task_B)

    return (
        app_config.TASK_A_MAP[prediction_task_A[0]],
        app_config.TASK_B_MAP[prediction_task_B[0]],
        prediction_task_A[1],
        prediction_task_B[1],
    )

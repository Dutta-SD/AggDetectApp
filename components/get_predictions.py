import components.utils as utils
from components.config import app_config
import joblib


def get_predictions(text: str) -> tuple[str, str]:
    """Gets Predictions for the Texts

    Args:
        text (str): The input text to get predictions for

    Returns:
        tuple[str, str]: Predictions for task A and task B
    """

    cleaned_data = [utils.clean_one_text(text)]

    # Load Models
    model_1 = joblib.load(app_config.TASK_A_MODEL_PATH)
    model_2 = joblib.load(app_config.TASK_B_MODEL_PATH)

    # Predictions
    pred_1 = model_1.predict(cleaned_data)[0]
    pred_2 = model_2.predict(cleaned_data)[0]

    return (
        app_config.TASK_A_MAP[pred_1],
        app_config.TASK_B_MAP[pred_2],
    )

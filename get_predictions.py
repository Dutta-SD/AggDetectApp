# Get predicitons from pre trained ML model
import utils
import joblib


def get_predictions(text: str) -> dict:
    """
    Returns predictions of aggressions and misogyny as per the model
    """
    cleaned_data = [utils.clean_one_text(text)]

    # Load Models
    model_1 = joblib.load(utils.TASK_1_MODEL)
    model_2 = joblib.load(utils.TASK_2_MODEL)

    # Predictions
    pred_1 = model_1.predict(cleaned_data)[0]
    pred_2 = model_2.predict(cleaned_data)[0]

    return {
        "task_1_pred": utils.TASK_1_MAP[pred_1],
        "task_2_pred": utils.TASK_2_MAP[pred_2],
    }


if __name__ == "__main__":
    print(get_predictions("Hello"))

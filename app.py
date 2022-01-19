# App
from get_predictions import get_predictions
import gradio


if __name__ == "__main__":
    interface = gradio.Interface(
        get_predictions,
        inputs="text",
        outputs="text",
    )
    interface.launch(title="Aggression and Misogyny Predictor")

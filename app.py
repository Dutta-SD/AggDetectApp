# App
from get_predictions import get_predictions
import gradio


if __name__ == "__main__":
    interface = gradio.Interface(
        get_predictions,
        inputs=gradio.inputs.Textbox(
            lines=2,
            placeholder="Enter The Text",
            default="",
            label="Text to Predict",
        ),
        outputs=["text", "text"],
        title="Aggression and Misogyny Predictor",
        theme="dark-huggingface",
        live=True,
    )
    interface.launch(
        share=False,
        debug=True,
    )

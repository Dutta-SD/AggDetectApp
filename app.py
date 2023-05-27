# App
from get_predictions import get_predictions
import gradio

"""
@todo refactor code + fix nltk download
@body change file directory, 
"""


if __name__ == "__main__":
    interface = gradio.Interface(
        get_predictions,
        inputs=gradio.inputs.Textbox(
            lines=2,
            placeholder="Enter The Text",
            default="",
            label="Text to Predict",
        ),
        outputs=[
            gradio.outputs.Textbox(type="text", label="Aggression Prediction"),
            gradio.outputs.Textbox(type="text", label="Misogyny Prediction"),
        ],
        title="Aggression and Misogyny Predictor",
        theme="dark-huggingface",
        live=True,
    )

    # Launch the interface
    interface.launch(
        share=False,
        debug=True,
    )

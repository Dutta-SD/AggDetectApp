from components.get_predictions import get_predictions
from gradio.components import Textbox
from gradio.interface import Interface
from gradio.themes import Monochrome


def get_input_fields() -> Textbox:
    """Get Input Fields

    Returns:
        Textbox: Input Field as gradio TextBox
    """
    return Textbox(
        lines=2,
        placeholder="Enter The Text",
        value="",
        label="Text to Predict",
    )


def get_output_fields() -> list[Textbox]:
    """Gets Output Fields

    Returns:
        list[Textbox...]: output fields as gradio textbox
    """

    return [
        Textbox(type="text", label="Aggression Prediction"),
        Textbox(type="text", label="Misogyny Prediction"),
    ]


def get_interface() -> Interface:
    """Gets the Interface with Input and Outputs

    Returns:
        Interface: gradio interface
    """

    interface = Interface(
        get_predictions,
        inputs=get_input_fields(),
        outputs=get_output_fields(),
        title="Aggression and Misogyny Predictor",
        theme=Monochrome(),
        live=False,
    )

    return interface


if __name__ == "__main__":
    interface = get_interface()

    # Launch the interface
    interface.launch(share=False, debug=True)

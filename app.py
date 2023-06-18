from components.get_predictions import get_predictions
from gradio.components import Textbox, IOComponent, Plot
from gradio.interface import Interface
from gradio.themes import Monochrome
from components.utils import initialize


def get_input_fields() -> Textbox:
    """Get Input Fields

    Returns:
        Textbox: Input Field as gradio TextBox
    """
    return Textbox(
        lines=10,
        placeholder="Enter The Text",
        value="",
        label="Text to Predict",
    )


def get_output_fields() -> list[str | IOComponent]:
    """Gets Output Fields

    Returns:
        list[str | IOComponent]: output fields as gradio textbox
    """

    return [
        Textbox(type="text", label="Aggression Prediction"),
        Textbox(type="text", label="Misogyny Prediction"),
        Plot(label="Explanation of Aggression", scale=1),
        Plot(label="Explanation of Misogyny", scale=1),
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
    initialize()
    interface = get_interface()

    # Launch the interface
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
    )

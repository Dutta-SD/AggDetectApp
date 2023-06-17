class Settings:
    """Configuration Settings"""

    TASK_A_MODEL_PATH = "static/weights/TASK_A_model_final.pkl"
    TASK_B_MODEL_PATH = "static/weights/TASK_B_model_final.pkl"
    TASK_A_MAP = {
        0: "NAG - Non Aggressive Content",
        1: "CAG - Covertly Aggressive Content",
        2: "OAG - Overtly Aggressive Content",
    }
    TASK_B_MAP = {
        0: "NGEN - Non Misogynistic Content",
        1: "GEN - Misogynistic Content",
    }
    NLTK_DATA_PATH = "/static/ntlk"


app_config = Settings()

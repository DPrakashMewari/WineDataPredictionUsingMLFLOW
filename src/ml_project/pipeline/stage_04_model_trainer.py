from src.ml_project.config.configuration import ConfigurationManger
from src.ml_project.components.model_trainer import ModelTrainer
from src.ml_project import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainerTrainingPipeline : 
    def __init__(self):
        pass

    def main(self):
        config =  ConfigurationManger()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

from src.ml_project.config.configuration import ConfigurationManger
from src.ml_project.components.data_validation import DataValiadtion
from src.ml_project import logger



STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()


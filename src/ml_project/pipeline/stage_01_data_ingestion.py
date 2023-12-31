from src.ml_project.config.configuration import ConfigurationManger
from src.ml_project.components.data_ingestion import DataIngestion
from src.ml_project import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    

# if __name__  == "__main__":
#     try:
#         logger.info(f"<<<<<{STAGE_NAME}>>>>>")
#         obj = DataIngestionTrainingPipeline()
#         obj.main()
#         logger.info(f"<<<<{STAGE_NAME} completed>>>")
#     except Exception as e:
#         logger.exception(e)
#         raise e

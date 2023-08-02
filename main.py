from src.ml_project import logger
from src.ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ml_project.pipeline.stage_02_data_validaton import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"<<<<<{STAGE_NAME}>>>>>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"<<<<{STAGE_NAME} completed>>>")
except Exception as e:
    logger.warning(f"Exception Occur{e}")
    raise e



try:
    logger.info(f"<<<<<{STAGE_NAME}>>>>>")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"<<<<{STAGE_NAME} completed>>>")
except Exception as e:
    logger.warning(f"Exception Occur{e}")
    raise e

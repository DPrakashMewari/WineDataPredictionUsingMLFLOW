from src.ml_project import logger
from src.ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ml_project.pipeline.stage_02_data_validaton import DataValidationTrainingPipeline
from src.ml_project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.ml_project.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME1 = "Data Ingestion Stage"
STAGE_NAME2 = "Data Validation Stage"
STAGE_NAME3 = "Data Transformation Stage"
STAGE_NAME4 = "Model Training Stage"

# Here data came from zip format from anywhere will try with db in our Next Example 
try:
    logger.info(f"<<<<<{STAGE_NAME1}>>>>>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"<<<<{STAGE_NAME1} completed>>>")
except Exception as e:
    logger.warning(f"Exception Occur{e}")
    raise e


# Data Validation : Validation Such as True,False while see the schema defined if missed True or False, Many Thing We can define
try:
    logger.info(f"<<<<<{STAGE_NAME2}>>>>>")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"<<<<{STAGE_NAME2} completed>>>")
except Exception as e:
    logger.warning(f"Exception Occur{e}")
    raise e


# Data Transformation
try:
    logger.info(f"<<<<<{STAGE_NAME3}>>>>>")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"<<<<{STAGE_NAME3} completed>>>")
except Exception as e:
    logger.warning(f"Exception Occur{e}")
    raise e


#  Model Trainer 
try:
    logger.info(f"<<<<<{STAGE_NAME4}>>>>>")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f"<<<<{STAGE_NAME4} completed>>>")
except Exception as e:
    logger.warning(f"Exception Occur{e}")
    raise e


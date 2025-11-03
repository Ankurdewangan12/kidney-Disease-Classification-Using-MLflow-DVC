from src.cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj=DataIngestionTraningPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e  
    

STAGE_NAME="Training"
try:
    logger.info(f"********************************")
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    model_trainer=ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
        logger.exception(e)
        raise e  


STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"********************************")
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    model_trainer=EvaluationPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e 
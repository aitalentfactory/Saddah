import logging
from datetime import datetime
from requests import Session

from src.dto.TrainingDTO import TrainingDTO
from src.mapper.TrainingMapper import trainingDTO_to_training, trainings_to_trainingDTOs, trainingDTO_list_to_json
from src.repository.TrainingRepository import TrainingRepository
from src.util.CommonUtil import get_uuid


class TrainingService:
    def __init__(self, db: Session):
        self.repository = TrainingRepository(db)


    def save_training(self, trainingDTO: TrainingDTO):
        trainingDTO.create_date_time = datetime.now()
        trainingDTO.status = "V"
        trainingDTO.uuid = get_uuid()
        logging.info("TrainingService.saveTraining {}".format(trainingDTO))
        training = trainingDTO_to_training(trainingDTO)
        self.repository.saveTraining(training)

    def get_last_10_training_by_userUuid(self, user_uuid):
        trainings = self.repository.get_latest_10_training_by_user_uuid(user_uuid)
        return trainings_to_trainingDTOs(trainings)


    def convert_trainingDTO_list_to_json(self,trainingDTOs):
        playerMetricsJson = trainingDTO_list_to_json(trainingDTOs)
        return playerMetricsJson
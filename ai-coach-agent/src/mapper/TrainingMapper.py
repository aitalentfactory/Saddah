import json
from typing import List

from src.dto.TrainingDTO import TrainingDTO
from src.model.Training import Training


def training_to_trainingDTO(training:Training) -> TrainingDTO:
    trainingDTO = TrainingDTO()
    trainingDTO.training = training.training
    trainingDTO.status = training.status
    trainingDTO.uuid = training.uuid
    trainingDTO.user_uuid = training.user_uuid
    trainingDTO.create_date_time = training.create_date_time
    return trainingDTO

def trainingDTO_to_training(trainingDTO:TrainingDTO) -> Training:
    training = Training()
    training.training = trainingDTO.training
    training.status = trainingDTO.status
    training.uuid = trainingDTO.uuid
    training.user_uuid = trainingDTO.user_uuid
    training.create_date_time = trainingDTO.create_date_time
    return training


def trainingDTOs_to_trainings(trainingDTOs:List[TrainingDTO]) -> List[Training]:
    trainings = []
    for trainingDTO in trainingDTOs:
        training = trainingDTO_to_training(trainingDTO)
        trainings.append(training)
    return trainings


def trainings_to_trainingDTOs(trainings:List[Training]) -> List[TrainingDTO]:
    trainingDTOs = []
    for training in trainings:
        trainingDTO = training_to_trainingDTO(training)
        trainingDTOs.append(trainingDTO)
    return trainingDTOs


def trainingDTO_list_to_json(training_dto_list: list[TrainingDTO]) -> str:
    return json.dumps({
        "trainings": [
            {
                "training": dto.training,
                "create_date_time": dto.create_date_time,
            } for dto in training_dto_list
        ]
    })
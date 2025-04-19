from typing import List

from src.dto.PlayerMetricDTO import PlayerMetricDTO
from src.dto.TrainingDTO import TrainingDTO
from src.dto.UserDTO import UserDTO

class UserWrapperDTO:
    user : UserDTO = UserDTO()
    playerMetrics: List[PlayerMetricDTO] = []
    trainings: List[TrainingDTO] = []

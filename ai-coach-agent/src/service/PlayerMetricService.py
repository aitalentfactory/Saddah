from datetime import datetime

from sqlalchemy.orm import Session

from src.mapper.PlayerMetricMapper import playerMetrics_to_playerMetricDTOs, player_metricDTO_list_to_json, \
    player_metricDTO_to_json, playerMetric_to_playerMetricDTO, player_metrics_to_response_dtos, \
    playerMetricDTO_to_playerMetric, player_metric_to_response_dto, playerMetricRequestDTO_to_playerMetricDTO
from src.repository.PlayerMetricRepository import PlayerMetricRepository
from src.requestDTO.PlayerMetricRequestDTO import PlayerMetricRequestDTO
from src.util.CommonUtil import get_uuid


class PlayerMetricService:
    def __init__(self, db: Session):
        self.repository = PlayerMetricRepository(db)

    def save(self, playerMetricRequestDTO: PlayerMetricRequestDTO):
        playerMetricDTO = playerMetricRequestDTO_to_playerMetricDTO(playerMetricRequestDTO)
        playerMetricDTO.uuid = get_uuid()
        playerMetricDTO.create_date_time = datetime.now()
        playerMetric = playerMetricDTO_to_playerMetric(playerMetricDTO)
        self.repository.save(playerMetric)
        return player_metric_to_response_dto(playerMetricDTO)

    def get_latest_player_metrics_by_user_uuid(self, user_uuid):
        playerMetric = self.repository.get_latest_player_metric_by_user_uuid(user_uuid)
        playerMetricDTO = playerMetric_to_playerMetricDTO(playerMetric)
        return playerMetricDTO


    def get_latest_3_player_metrics_by_user_uuid(self, user_uuid):
        playerMetrics = self.repository.get_latest_3_player_metrics_by_user_uuid(user_uuid)
        playerMetricDTOs = playerMetrics_to_playerMetricDTOs(playerMetrics)
        return playerMetricDTOs

    def get_latest_10_player_metrics_by_user_uuid(self, user_uuid):
        playerMetrics = self.repository.get_latest_10_player_metrics_by_user_uuid(user_uuid)
        playerMetricDTOs = playerMetrics_to_playerMetricDTOs(playerMetrics)
        return playerMetricDTOs

    def get_latest_10_player_metrics_by_user_uuid_for_api_response(self, user_uuid):
        playerMetricDTOs = self.get_latest_10_player_metrics_by_user_uuid(user_uuid)
        return player_metrics_to_response_dtos(playerMetricDTOs)

    def convert_player_metric_to_json(self,playerMetricDTO):
        playerMetricJson = player_metricDTO_to_json(playerMetricDTO)
        return playerMetricJson

    def convert_player_list_metric_to_json(self,playerMetricDTOs):
        playerMetricsJson = player_metricDTO_list_to_json(playerMetricDTOs)
        return playerMetricsJson
from sqlalchemy.orm import Session
from src.mapper.PlayerMetricMapper import playerMetrics_to_playerMetricDTOs, player_metricDTO_list_to_json, \
    player_metricDTO_to_json, playerMetric_to_playerMetricDTO
from src.repository.PlayerMetricRepository import PlayerMetricRepository


class PlayerMetricService:
    def __init__(self, db: Session):
        self.repository = PlayerMetricRepository(db)

    def get_latest_player_metrics_by_user_uuid(self, user_uuid):
        playerMetric = self.repository.get_latest_player_metric_by_user_uuid(user_uuid)
        playerMetricDTO = playerMetric_to_playerMetricDTO(playerMetric)
        return playerMetricDTO

    def get_latest_10_player_metrics_by_user_uuid(self, user_uuid):
        playerMetrics = self.repository.get_latest_10_player_metrics_by_user_uuid(user_uuid)
        playerMetricDTOs = playerMetrics_to_playerMetricDTOs(playerMetrics)
        return playerMetricDTOs

    def convert_player_metric_to_json(self,playerMetricDTO):
        playerMetricJson = player_metricDTO_to_json(playerMetricDTO)
        return playerMetricJson

    def convert_player_list_metric_to_json(self,playerMetricDTOs):
        playerMetricsJson = player_metricDTO_list_to_json(playerMetricDTOs)
        return playerMetricsJson
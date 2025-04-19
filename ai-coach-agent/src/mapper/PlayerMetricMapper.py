import json
from datetime import datetime
from typing import List

from src.dto.PlayerMetricDTO import PlayerMetricDTO
from src.model.PlayerMetric import PlayerMetric
from src.requestDTO.PlayerMetricRequestDTO import PlayerMetricRequestDTO
from src.responseDTO.PlayerMetricResponseDTO import PlayerResponseMetricDTO

def playerMetricRequestDTO_to_playerMetricDTO(player_metric_request_DTO: PlayerMetricRequestDTO) -> PlayerMetricDTO:
    player_metric_dto = PlayerMetricDTO()
    player_metric_dto.blood_oxygen_level = player_metric_request_DTO.blood_oxygen_level
    player_metric_dto.body_temperature = player_metric_request_DTO.body_temperature
    player_metric_dto.calories_burned = player_metric_request_DTO.calories_burned
    player_metric_dto.gait_analysis = player_metric_request_DTO.gait_analysis
    player_metric_dto.gps_data = player_metric_request_DTO.gps_data
    player_metric_dto.heart_rate = player_metric_request_DTO.heart_rate
    player_metric_dto.heart_rate_variability = player_metric_request_DTO.heart_rate_variability
    player_metric_dto.impact_collision_detection = player_metric_request_DTO.impact_collision_detection
    player_metric_dto.jump_count = player_metric_request_DTO.jump_count
    player_metric_dto.jump_height = player_metric_request_DTO.jump_height
    player_metric_dto.muscle_oxygenation = player_metric_request_DTO.muscle_oxygenation
    player_metric_dto.recovery_time_estimation = player_metric_request_DTO.recovery_time_estimation
    player_metric_dto.repetition_count_load = player_metric_request_DTO.repetition_count_load
    player_metric_dto.sleep_duration = player_metric_request_DTO.sleep_duration
    player_metric_dto.sleep_quality = player_metric_request_DTO.sleep_quality
    player_metric_dto.status = player_metric_request_DTO.status
    player_metric_dto.step_count = player_metric_request_DTO.step_count
    player_metric_dto.stress_level = player_metric_request_DTO.stress_level
    player_metric_dto.user_uuid = player_metric_request_DTO.user_uuid
    player_metric_dto.vo_max = player_metric_request_DTO.vo_max
    player_metric_dto.workout_duration = player_metric_request_DTO.workout_duration
    player_metric_dto.workout_type = player_metric_request_DTO.workout_type
    return player_metric_dto

def playerMetric_to_playerMetricDTO(player_metric: PlayerMetric) -> PlayerMetricDTO:
    player_metric_dto = PlayerMetricDTO()
    player_metric_dto.blood_oxygen_level = player_metric.blood_oxygen_level
    player_metric_dto.body_temperature = player_metric.body_temperature
    player_metric_dto.calories_burned = player_metric.calories_burned
    player_metric_dto.create_date_time = player_metric.create_date_time
    player_metric_dto.gait_analysis = player_metric.gait_analysis
    player_metric_dto.gps_data = player_metric.gps_data
    player_metric_dto.heart_rate = player_metric.heart_rate
    player_metric_dto.heart_rate_variability = player_metric.heart_rate_variability
    player_metric_dto.impact_collision_detection = player_metric.impact_collision_detection
    player_metric_dto.jump_count = player_metric.jump_count
    player_metric_dto.jump_height = player_metric.jump_height
    player_metric_dto.muscle_oxygenation = player_metric.muscle_oxygenation
    player_metric_dto.recovery_time_estimation = player_metric.recovery_time_estimation
    player_metric_dto.repetition_count_load = player_metric.repetition_count_load
    player_metric_dto.sleep_duration = player_metric.sleep_duration
    player_metric_dto.sleep_quality = player_metric.sleep_quality
    player_metric_dto.status = player_metric.status
    player_metric_dto.step_count = player_metric.step_count
    player_metric_dto.stress_level = player_metric.stress_level
    player_metric_dto.user_uuid = player_metric.user_uuid
    player_metric_dto.uuid = player_metric.uuid
    player_metric_dto.vo_max = player_metric.vo_max
    player_metric_dto.workout_duration = player_metric.workout_duration
    player_metric_dto.workout_type = player_metric.workout_type
    return player_metric_dto

def playerMetricDTO_to_playerMetric(player_metric_dto: PlayerMetricDTO) -> PlayerMetric:
    player_metric = PlayerMetric()
    player_metric.blood_oxygen_level = player_metric_dto.blood_oxygen_level
    player_metric.body_temperature = player_metric_dto.body_temperature
    player_metric.calories_burned = player_metric_dto.calories_burned
    player_metric.create_date_time = player_metric_dto.create_date_time
    player_metric.gait_analysis = player_metric_dto.gait_analysis
    player_metric.gps_data = player_metric_dto.gps_data
    player_metric.heart_rate = player_metric_dto.heart_rate
    player_metric.heart_rate_variability = player_metric_dto.heart_rate_variability
    player_metric.impact_collision_detection = player_metric_dto.impact_collision_detection
    player_metric.jump_count = player_metric_dto.jump_count
    player_metric.jump_height = player_metric_dto.jump_height
    player_metric.muscle_oxygenation = player_metric_dto.muscle_oxygenation
    player_metric.recovery_time_estimation = player_metric_dto.recovery_time_estimation
    player_metric.repetition_count_load = player_metric_dto.repetition_count_load
    player_metric.sleep_duration = player_metric_dto.sleep_duration
    player_metric.sleep_quality = player_metric_dto.sleep_quality
    player_metric.status = player_metric_dto.status
    player_metric.step_count = player_metric_dto.step_count
    player_metric.stress_level = player_metric_dto.stress_level
    player_metric.user_uuid = player_metric_dto.user_uuid
    player_metric.uuid = player_metric_dto.uuid
    player_metric.vo_max = player_metric_dto.vo_max
    player_metric.workout_duration = player_metric_dto.workout_duration
    player_metric.workout_type = player_metric_dto.workout_type
    return player_metric

def playerMetrics_to_playerMetricDTOs(player_metrics: List[PlayerMetric]) -> List[PlayerMetricDTO]:
    player_metric_dtos: List[PlayerMetricDTO] = []
    for player_metric in player_metrics:
        player_metric_dto = playerMetric_to_playerMetricDTO(player_metric)
        player_metric_dtos.append(player_metric_dto)
    return player_metric_dtos


def player_metric_to_response_dto(dto: PlayerMetricDTO) -> PlayerResponseMetricDTO:
    create_date_time = dto.create_date_time
    if isinstance(create_date_time, datetime):
        create_date_time = create_date_time.isoformat()

    return PlayerResponseMetricDTO(
        blood_oxygen_level=dto.blood_oxygen_level,
        body_temperature=dto.body_temperature,
        calories_burned=dto.calories_burned,
        create_date_time=create_date_time,
        gait_analysis=dto.gait_analysis,
        gps_data=dto.gps_data,
        heart_rate=dto.heart_rate,
        heart_rate_variability=dto.heart_rate_variability,
        impact_collision_detection=dto.impact_collision_detection,
        jump_count=dto.jump_count,
        jump_height=dto.jump_height,
        muscle_oxygenation=dto.muscle_oxygenation,
        recovery_time_estimation=dto.recovery_time_estimation,
        repetition_count_load=dto.repetition_count_load,
        sleep_duration=dto.sleep_duration,
        sleep_quality=dto.sleep_quality,
        status=dto.status,
        step_count=dto.step_count,
        stress_level=dto.stress_level,
        user_uuid=dto.user_uuid,
        uuid=dto.uuid,
        vo_max=dto.vo_max,
        workout_duration=dto.workout_duration,
        workout_type=dto.workout_type
    )

def player_metrics_to_response_dtos(dtos: List[PlayerMetricDTO]) -> List[PlayerResponseMetricDTO]:
    return [player_metric_to_response_dto(dto) for dto in dtos]

def player_metricDTO_to_json(player_metric_dto: PlayerMetricDTO) -> str:
    return json.dumps({
        "player_metric": {
            "blood_oxygen_level": player_metric_dto.blood_oxygen_level,
            "body_temperature": player_metric_dto.body_temperature,
            "calories_burned": player_metric_dto.calories_burned,
            "create_date_time": player_metric_dto.create_date_time,
            "gait_analysis": player_metric_dto.gait_analysis,
            "gps_data": player_metric_dto.gps_data,
            "heart_rate": player_metric_dto.heart_rate,
            "heart_rate_variability": player_metric_dto.heart_rate_variability,
            "impact_collision_detection": player_metric_dto.impact_collision_detection,
            "jump_count": player_metric_dto.jump_count,
            "jump_height": player_metric_dto.jump_height,
            "muscle_oxygenation": player_metric_dto.muscle_oxygenation,
            "recovery_time_estimation": player_metric_dto.recovery_time_estimation,
            "repetition_count_load": player_metric_dto.repetition_count_load,
            "sleep_duration": player_metric_dto.sleep_duration,
            "sleep_quality": player_metric_dto.sleep_quality,
            "status": player_metric_dto.status,
            "step_count": player_metric_dto.step_count,
            "stress_level": player_metric_dto.stress_level,
            "user_uuid": player_metric_dto.user_uuid,
            "uuid": player_metric_dto.uuid,
            "vo_max": player_metric_dto.vo_max,
            "workout_duration": player_metric_dto.workout_duration,
            "workout_type": player_metric_dto.workout_type
        }
    })



def player_metricDTO_list_to_json(player_metric_dto_list: list[PlayerMetricDTO]) -> str:
    return json.dumps({
        "player_metrics": [
            {
                "blood_oxygen_level": dto.blood_oxygen_level,
                "body_temperature": dto.body_temperature,
                "calories_burned": dto.calories_burned,
                "create_date_time": dto.create_date_time,
                "gait_analysis": dto.gait_analysis,
                "gps_data": dto.gps_data,
                "heart_rate": dto.heart_rate,
                "heart_rate_variability": dto.heart_rate_variability,
                "impact_collision_detection": dto.impact_collision_detection,
                "jump_count": dto.jump_count,
                "jump_height": dto.jump_height,
                "muscle_oxygenation": dto.muscle_oxygenation,
                "recovery_time_estimation": dto.recovery_time_estimation,
                "repetition_count_load": dto.repetition_count_load,
                "sleep_duration": dto.sleep_duration,
                "sleep_quality": dto.sleep_quality,
                "status": dto.status,
                "step_count": dto.step_count,
                "stress_level": dto.stress_level,
                "user_uuid": dto.user_uuid,
                "uuid": dto.uuid,
                "vo_max": dto.vo_max,
                "workout_duration": dto.workout_duration,
                "workout_type": dto.workout_type
            } for dto in player_metric_dto_list
        ]
    })
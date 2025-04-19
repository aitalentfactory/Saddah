from sqlalchemy import text
from sqlalchemy.orm import Session

from src.model.PlayerMetric import PlayerMetric


class PlayerMetricRepository:
        def __init__(self, db: Session):
            self.db = db

        def get_latest_player_metric_by_user_uuid(self, user_uuid):
            query = text("""
                SELECT id, blood_oxygen_level, body_temperature, calories_burned, create_date_time, 
                       gait_analysis, gps_data, heart_rate, heart_rate_variability, impact_collision_detection, 
                       jump_count, jump_height, muscle_oxygenation, recovery_time_estimation, repetition_count_load, 
                       sleep_duration, sleep_quality, status, step_count, stress_level, user_uuid, uuid, 
                       vo_max, workout_duration, workout_type
                FROM player_metric 
                WHERE user_uuid = :user_uuid 
                ORDER BY create_date_time DESC 
                LIMIT 1
            """)

            result = self.db.execute(query, {"user_uuid": user_uuid}).fetchone()

            player_metric = PlayerMetric()
            if result is not None:
                player_metric.seqId = result.id
                player_metric.blood_oxygen_level = result.blood_oxygen_level
                player_metric.body_temperature = result.body_temperature
                player_metric.calories_burned = result.calories_burned
                player_metric.create_date_time = result.create_date_time
                player_metric.gait_analysis = result.gait_analysis
                player_metric.gps_data = result.gps_data
                player_metric.heart_rate = result.heart_rate
                player_metric.heart_rate_variability = result.heart_rate_variability
                player_metric.impact_collision_detection = result.impact_collision_detection
                player_metric.jump_count = result.jump_count
                player_metric.jump_height = result.jump_height
                player_metric.muscle_oxygenation = result.muscle_oxygenation
                player_metric.recovery_time_estimation = result.recovery_time_estimation
                player_metric.repetition_count_load = result.repetition_count_load
                player_metric.sleep_duration = result.sleep_duration
                player_metric.sleep_quality = result.sleep_quality
                player_metric.status = result.status
                player_metric.step_count = result.step_count
                player_metric.stress_level = result.stress_level
                player_metric.user_uuid = result.user_uuid
                player_metric.uuid = result.uuid
                player_metric.vo_max = result.vo_max
                player_metric.workout_duration = result.workout_duration
                player_metric.workout_type = result.workout_type
            return player_metric

        def get_latest_3_player_metrics_by_user_uuid(self, user_uuid):
            query = text("""
             SELECT id, blood_oxygen_level, body_temperature, calories_burned, create_date_time, 
                    gait_analysis, gps_data, heart_rate, heart_rate_variability, impact_collision_detection, 
                    jump_count, jump_height, muscle_oxygenation, recovery_time_estimation, repetition_count_load, 
                    sleep_duration, sleep_quality, status, step_count, stress_level, user_uuid, uuid, 
                    vo_max, workout_duration, workout_type
             FROM player_metric 
             WHERE user_uuid = :user_uuid 
             ORDER BY create_date_time DESC 
             LIMIT 3
         """)
            results = self.db.execute(query, {"user_uuid": user_uuid}).fetchall()

            player_metrics = []
            for result in results:
                player_metric = PlayerMetric()
                player_metric.seqId = result.id
                player_metric.blood_oxygen_level = result.blood_oxygen_level
                player_metric.body_temperature = result.body_temperature
                player_metric.calories_burned = result.calories_burned
                player_metric.create_date_time = result.create_date_time
                player_metric.gait_analysis = result.gait_analysis
                player_metric.gps_data = result.gps_data
                player_metric.heart_rate = result.heart_rate
                player_metric.heart_rate_variability = result.heart_rate_variability
                player_metric.impact_collision_detection = result.impact_collision_detection
                player_metric.jump_count = result.jump_count
                player_metric.jump_height = result.jump_height
                player_metric.muscle_oxygenation = result.muscle_oxygenation
                player_metric.recovery_time_estimation = result.recovery_time_estimation
                player_metric.repetition_count_load = result.repetition_count_load
                player_metric.sleep_duration = result.sleep_duration
                player_metric.sleep_quality = result.sleep_quality
                player_metric.status = result.status
                player_metric.step_count = result.step_count
                player_metric.stress_level = result.stress_level
                player_metric.user_uuid = result.user_uuid
                player_metric.uuid = result.uuid
                player_metric.vo_max = result.vo_max
                player_metric.workout_duration = result.workout_duration
                player_metric.workout_type = result.workout_type
                player_metrics.append(player_metric)
            return player_metrics

        def get_latest_10_player_metrics_by_user_uuid(self, user_uuid):
            query = text("""
             SELECT id, blood_oxygen_level, body_temperature, calories_burned, create_date_time, 
                    gait_analysis, gps_data, heart_rate, heart_rate_variability, impact_collision_detection, 
                    jump_count, jump_height, muscle_oxygenation, recovery_time_estimation, repetition_count_load, 
                    sleep_duration, sleep_quality, status, step_count, stress_level, user_uuid, uuid, 
                    vo_max, workout_duration, workout_type
             FROM player_metric 
             WHERE user_uuid = :user_uuid 
             ORDER BY create_date_time DESC 
             LIMIT 10
         """)
            results = self.db.execute(query, {"user_uuid": user_uuid}).fetchall()

            player_metrics = []
            for result in results:
                player_metric = PlayerMetric()
                player_metric.seqId = result.id
                player_metric.blood_oxygen_level = result.blood_oxygen_level
                player_metric.body_temperature = result.body_temperature
                player_metric.calories_burned = result.calories_burned
                player_metric.create_date_time = result.create_date_time
                player_metric.gait_analysis = result.gait_analysis
                player_metric.gps_data = result.gps_data
                player_metric.heart_rate = result.heart_rate
                player_metric.heart_rate_variability = result.heart_rate_variability
                player_metric.impact_collision_detection = result.impact_collision_detection
                player_metric.jump_count = result.jump_count
                player_metric.jump_height = result.jump_height
                player_metric.muscle_oxygenation = result.muscle_oxygenation
                player_metric.recovery_time_estimation = result.recovery_time_estimation
                player_metric.repetition_count_load = result.repetition_count_load
                player_metric.sleep_duration = result.sleep_duration
                player_metric.sleep_quality = result.sleep_quality
                player_metric.status = result.status
                player_metric.step_count = result.step_count
                player_metric.stress_level = result.stress_level
                player_metric.user_uuid = result.user_uuid
                player_metric.uuid = result.uuid
                player_metric.vo_max = result.vo_max
                player_metric.workout_duration = result.workout_duration
                player_metric.workout_type = result.workout_type
                player_metrics.append(player_metric)
            return player_metrics


        def save(self,player_metric):
            insert_query = text("""
                INSERT INTO player_metric (
                    blood_oxygen_level, body_temperature, calories_burned, create_date_time, 
                    gait_analysis, gps_data, heart_rate, heart_rate_variability, impact_collision_detection, 
                    jump_count, jump_height, muscle_oxygenation, recovery_time_estimation, repetition_count_load, 
                    sleep_duration, sleep_quality, status, step_count, stress_level, user_uuid, uuid, 
                    vo_max, workout_duration, workout_type
                ) VALUES (
                    :blood_oxygen_level, :body_temperature, :calories_burned, :create_date_time, 
                    :gait_analysis, :gps_data, :heart_rate, :heart_rate_variability, :impact_collision_detection, 
                    :jump_count, :jump_height, :muscle_oxygenation, :recovery_time_estimation, :repetition_count_load, 
                    :sleep_duration, :sleep_quality, :status, :step_count, :stress_level, :user_uuid, :uuid, 
                    :vo_max, :workout_duration, :workout_type
                )
            """)

            result = self.db.execute(insert_query, {
                "blood_oxygen_level": player_metric.blood_oxygen_level,
                "body_temperature": player_metric.body_temperature,
                "calories_burned": player_metric.calories_burned,
                "create_date_time": player_metric.create_date_time,
                "gait_analysis": player_metric.gait_analysis,
                "gps_data": player_metric.gps_data,
                "heart_rate": player_metric.heart_rate,
                "heart_rate_variability": player_metric.heart_rate_variability,
                "impact_collision_detection": player_metric.impact_collision_detection,
                "jump_count": player_metric.jump_count,
                "jump_height": player_metric.jump_height,
                "muscle_oxygenation": player_metric.muscle_oxygenation,
                "recovery_time_estimation": player_metric.recovery_time_estimation,
                "repetition_count_load": player_metric.repetition_count_load,
                "sleep_duration": player_metric.sleep_duration,
                "sleep_quality": player_metric.sleep_quality,
                "status": player_metric.status,
                "step_count": player_metric.step_count,
                "stress_level": player_metric.stress_level,
                "user_uuid": player_metric.user_uuid,
                "uuid": player_metric.uuid,
                "vo_max": player_metric.vo_max,
                "workout_duration": player_metric.workout_duration,
                "workout_type": player_metric.workout_type
            })
            self.db.commit()
            return result.lastrowid

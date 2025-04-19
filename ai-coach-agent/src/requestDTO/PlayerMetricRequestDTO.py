from pydantic import BaseModel, Field, field_validator


class PlayerMetricRequestDTO(BaseModel):
    blood_oxygen_level: str = Field(default=None, alias='blood_oxygen_level')
    body_temperature: str = Field(default=None, alias='body_temperature')
    calories_burned: str = Field(default=None, alias='calories_burned')
    gait_analysis: str = Field(default=None, alias='gait_analysis')
    gps_data: str = Field(default=None, alias='gps_data')
    heart_rate: str = Field(default=None, alias='heart_rate')
    heart_rate_variability: str = Field(default=None, alias='heart_rate_variability')
    impact_collision_detection: str = Field(default=None, alias='impact_collision_detection')
    jump_count: str = Field(default=None, alias='jump_count')
    jump_height: str = Field(default=None, alias='jump_height')
    muscle_oxygenation: str = Field(default=None, alias='muscle_oxygenation')
    recovery_time_estimation: str = Field(default=None, alias='recovery_time_estimation')
    repetition_count_load: str = Field(default=None, alias='repetition_count_load')
    sleep_duration: str = Field(default=None, alias='sleep_duration')
    sleep_quality: str = Field(default=None, alias='sleep_quality')
    status: str = Field(default=None, alias='status')
    step_count: str = Field(default=None, alias='step_count')
    stress_level: str = Field(default=None, alias='stress_level')
    user_uuid: str = Field(default=None, alias='user_uuid')
    vo_max: str = Field(default=None, alias='vo_max')
    workout_duration: str = Field(default=None, alias='workout_duration')
    workout_type: str = Field(default=None, alias='workout_type')

    @field_validator(
        'blood_oxygen_level', 'body_temperature', 'calories_burned',
        'gait_analysis', 'gps_data', 'heart_rate', 'heart_rate_variability',
        'impact_collision_detection', 'jump_count', 'jump_height', 'muscle_oxygenation',
        'recovery_time_estimation', 'repetition_count_load', 'sleep_duration', 'sleep_quality',
        'status', 'step_count', 'stress_level', 'user_uuid', 'vo_max',
        'workout_duration', 'workout_type', mode='before'
    )
    def not_empty_string(cls, v, field):
        if v is None or str(v).strip() == '':
            raise ValueError(f'{field.alias} is required')
        return v

from sqlalchemy import text
from sqlalchemy.orm import Session

from src.model.Training import Training


class TrainingRepository:
        def __init__(self, db: Session):
            self.db = db

        def saveTraining(self, training: Training):
            query = text("""
                                INSERT INTO player_training (
                                    status, user_uuid, uuid, training,create_date_time
                                ) VALUES (
                                    :STATUS, :USER_UUID, :UUID, :TRAINING,:CREATE_DATETIME
                                )
                            """)
            result = self.db.execute(
                query,
                {
                    "STATUS": training.status,
                    "USER_UUID": training.user_uuid,
                    "UUID": training.uuid,
                    "TRAINING": training.training,
                    "CREATE_DATETIME": training.create_date_time
                }
            )
            self.db.commit()
            return result.lastrowid


        def get_latest_10_training_by_user_uuid(self, user_uuid):
            query = text("""
             SELECT id, status, user_uuid, uuid, training,create_date_time
             FROM player_training 
             WHERE user_uuid = :user_uuid 
             ORDER BY create_date_time DESC 
             LIMIT 1
         """)
            results = self.db.execute(query, {"user_uuid": user_uuid}).fetchall()

            trainings = []
            for result in results:
                training = Training()
                training.id = result.id
                training.status = result.status
                training.user_uuid = result.user_uuid
                training.uuid = result.uuid
                training.create_date_time = result.create_date_time
                training.training = result.training
                trainings.append(training)
            return trainings
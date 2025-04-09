
CREATE DATABASE `soccer` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
-- soccer.ai_user definition

CREATE TABLE `ai_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `fullname` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `uuid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- soccer.player_metric definition

CREATE TABLE `player_metric` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `blood_oxygen_level` varchar(255) DEFAULT NULL,
  `body_temperature` varchar(255) DEFAULT NULL,
  `calories_burned` varchar(255) DEFAULT NULL,
  `create_date_time` varchar(255) DEFAULT NULL,
  `gait_analysis` varchar(255) DEFAULT NULL,
  `gps_data` varchar(255) DEFAULT NULL,
  `heart_rate` varchar(255) DEFAULT NULL,
  `heart_rate_variability` varchar(255) DEFAULT NULL,
  `impact_collision_detection` varchar(255) DEFAULT NULL,
  `jump_count` varchar(255) DEFAULT NULL,
  `jump_height` varchar(255) DEFAULT NULL,
  `muscle_oxygenation` varchar(255) DEFAULT NULL,
  `recovery_time_estimation` varchar(255) DEFAULT NULL,
  `repetition_count_load` varchar(255) DEFAULT NULL,
  `sleep_duration` varchar(255) DEFAULT NULL,
  `sleep_quality` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `step_count` varchar(255) DEFAULT NULL,
  `stress_level` varchar(255) DEFAULT NULL,
  `user_uuid` varchar(255) DEFAULT NULL,
  `uuid` varchar(255) DEFAULT NULL,
  `vo_max` varchar(255) DEFAULT NULL,
  `workout_duration` varchar(255) DEFAULT NULL,
  `workout_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- soccer.player_training definition

CREATE TABLE `player_training` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `training` text NOT NULL,
  `status` varchar(1) NOT NULL,
  `uuid` varchar(100) NOT NULL,
  `user_uuid` varchar(100) NOT NULL,
  `create_date_time` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
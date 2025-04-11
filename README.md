![image](https://github.com/aitalentfactory/Saddah/blob/main/صده.jpg)

 Saddah
The system analyses player data (fitness levels, past injuries, performance stats). AI adjusts training schedules dynamically based on real-time insights.
Players and coaches receive personalized training plans via an interactive dashboard. 
Uses RAG (Retrieval-Augmented Generation) to pull relevant training suggestions from large datasets.
Integrates live data from IoT wearables for performance tracking


Saddah Project -  AI-Powered Personalized Football Trainer for GoalKeepers


This repository brings together all components of the Saddah Project, an AI-powered football training and injury prediction platform. It includes datasets, machine learning pipelines, data analysis notebooks, and the complete application code.

📂 Repository Structure:
============================================

📁 1/ Github_Dataset:
======================

Original  datasets downloaded from Github  Includes sports performance and injury
https://github.com/josedv82/public_sport_science_datasets/tree/main


📁 2/Kaggle_dataset:
=====================

Original datasets downloaded from Kaggle. The datasets provided include the players data for the Career Mode from FIFA 15 to FIFA 23.
[https://www.kaggle.com/datasets/joebeachcapital/fifa-players](https://www.kaggle.com/datasets/joebeachcapital/fifa-players)




📁 3/Saddah-main (Application Source Code):
===========================================

This folder contains the main application logic, including:

- mobile frontend
- Backend server/API
- Integration points with the AI model

📁 4/ai-coach-agent (AI Model):
===================================

Includes all code and scripts used to build and fine-tune the AI football training assistant, such as:

- Prompt formatting and data conversion
- OpenAI API usage and fine-tuning jobs
- LangChain/OpenAI SDKs

📁 5/data-analysis-and-fine-tuning:
====================================

Notebooks and Python scripts for:

- Exploratory data analysis (EDA)
- Preparing datasets for fine-tuning
- Uploading data to OpenAI
- Monitoring fine-tuning jobs

📅 6/Injuries_Dataset.ipynb:
==============================

A detailed notebook analyzing athlete injury data, covering:

- Feature descriptions
- Missing value checks
- Visualizations (correlation heatmaps, distributions, trends)
- Comparisons between injured and non-injured athletes

📦7/ Saddah_website:
============================

Contains the source code or compiled version of the official Saddah project website. This may include:
- Static HTML/CSS files
- JavaScript logic
- Demo content for online deployment

📃 How to Use This Repository:
===============================

1) Start by exploring the Kaggle_dataset or Github_Dataset folders.
2) Run Injuries_Dataset.ipynb to get insights on injury trends.
3)Dive into the ai-coach-agent to understand the AI pipeline.
4)Use Saddah-main to run or modify the app.
5) deploy the website in Saddah_website to present  solution.

✨ Project Highlights:
==========================

- Personalized training plans using GPT-3.5/4 fine-tuning
- Injury risk detection based on multi-week performance data
- Integrated app experience with AI feedback
- Strong focus on real-world datasets and visual analytics





![image](https://github.com/aitalentfactory/Saddah/blob/main/صده.jpg)

 Saddah
The system analyses player data (fitness levels, past injuries, performance stats). AI adjusts training schedules dynamically based on real-time insights.
Players and coaches receive personalized training plans via an interactive dashboard. 
Uses RAG (Retrieval-Augmented Generation) to pull relevant training suggestions from large datasets.
Integrates live data from IoT wearables for performance tracking


Saddah Project - AI Football Coach & Injury Insight - AI-Powered Personalized Football Trainer![image](https://github.com/user-attachments/assets/e48141f3-790a-4a5e-88c6-9768bc853701)


This repository brings together all components of the Saddah Project, an AI-powered football training and injury prediction platform. It includes datasets, machine learning pipelines, data analysis notebooks, and the complete application code.

📂 Repository Structure

📁 Github_Dataset

Original or raw datasets downloaded from Github  https://github.com/josedv82/public_sport_science_datasets/tree/main
![image](https://github.com/user-attachments/assets/ecd720e2-43d9-4db5-98dc-56f0815125b4) Includes sports performance and injury

📁 Kaggle_dataset

Original or raw datasets downloaded from Kaggle. Includes sports performance and injury-related datasets in their original form.
https://www.kaggle.com/datasets/joebeachcapital/fifa-players
![image](https://github.com/user-attachments/assets/7f3d979c-e830-4bad-b57e-bbf1bea3ae4c)


📁 Saddah-main (Application Source Code)

This folder contains the main application logic, including:

mobile frontend

Backend server/API

Integration points with the AI model

📁 ai-coach-agent (AI Model)

Includes all code and scripts used to build and fine-tune the AI football training assistant, such as:

Prompt formatting and data conversion

OpenAI API usage and fine-tuning jobs

LangChain/OpenAI SDKs

📁 data-analysis-and-fine-tuning

Notebooks and Python scripts for:

Exploratory data analysis (EDA)

Preparing datasets for fine-tuning

Uploading data to OpenAI

Monitoring fine-tuning jobs

📅 Injuries_Dataset.ipynb

A detailed notebook analyzing athlete injury data, covering:

Feature descriptions

Missing value checks

Visualizations (correlation heatmaps, distributions, trends)

Comparisons between injured and non-injured athletes

📦 Saddah_website.zip

Contains the source code or compiled version of the official Saddah project website. This may include:

Static HTML/CSS files

JavaScript logic

Demo content for online deployment

📃 How to Use This Repository

Start by exploring the Kaggle_dataset or Github_Dataset folders.

Run Injuries_Dataset.ipynb to get insights on injury trends.

Dive into the ai-coach-agent to understand the AI pipeline.

Use Saddah-main to run or modify the app.

 deploy the website in Saddah_website to present  solution.

✨ Project Highlights

Personalized training plans using GPT-3.5/4 fine-tuning

Injury risk detection based on multi-week performance data

Integrated app experience with AI feedback

Strong focus on real-world datasets and visual analytics





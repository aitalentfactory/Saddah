import json


def generate_report_prompt(player_metrics_json: str) -> str:
    """
    Generates a prompt for an LLM to create a detailed report based on the given JSON data string.

    Parameters:
        json_str (str): A string containing the JSON data representing player metrics.

    Returns:
        str: A prompt string that can be given to an LLM to generate a detailed report.
    """
    try:
        # Parse the JSON string into a dictionary
        data = json.loads(player_metrics_json)
        # Convert the dictionary back to a pretty-formatted JSON string
        formatted_data = json.dumps(data, indent=2)
    except json.JSONDecodeError:
        # If the input is not a valid JSON, use the original string.
        formatted_data = player_metrics_json

    prompt = (
        "You are provided with the following JSON data representing player metrics collected over multiple sessions. "
        "Each record includes various physiological metrics (e.g., blood oxygen level, heart rate, muscle oxygenation), "
        "performance metrics (e.g., step count, jump count, calories burned, VO₂ max), recovery and wellness data (e.g., "
        "sleep duration, sleep quality, recovery time estimation), as well as workout details such as workout type and "
        "GPS data. \n\n"
        "Your task is to analyze the data in chronological order using the 'create_date_time' field, identify any trends, "
        "improvements, or potential areas for enhancement, and generate a detailed report. Consider the following aspects:\n"
        "1. **Physiological Metrics:** Stability or improvement in blood oxygen level, body temperature, heart rate, and heart rate variability.\n"
        "2. **Performance Metrics:** Changes in calories burned, step count, jump count, jump height, and VO₂ max over time.\n"
        "3. **Recovery & Wellness Metrics:** Trends in sleep duration, sleep quality, and recovery time estimation.\n"
        "4. **Activity Context:** Variations in workout type, duration, GPS data, and impact collision detection.\n\n"
        "Include insights on how the user's performance has evolved and recommendations for further improvement. \n\n"
        "Here is the JSON data:\n\n"
    )

    prompt += formatted_data

    prompt += (
        "\n\nGenerate a comprehensive report with detailed analysis, insights, and recommendations based on the observed trends."
    )

    return prompt


def generate_training_schedule_prompt(report: str) -> str:
    """
    Generates a prompt for an LLM to create a one-week football training schedule based on a detailed performance report.
    The schedule should improve the player's performance, prevent injuries, and include two designated rest days with healthy recovery activities.
    The response must be structured day-by-day with specific activities and include training timings for each exercise.

    Parameters:
        report (str): The detailed performance report generated from the player's metrics.

    Returns:
        str: A prompt string for generating a training schedule.
    """
    prompt = (
        "You are an experienced AI football trainer and coach. Based on the detailed performance report provided below, "
        "your task is to generate a comprehensive 1-week training schedule that aims to enhance the player's performance "
        "and minimize the risk of future injuries. The schedule must include two designated full rest days. On these rest days, "
        "include healthy recovery activities such as gentle yoga, foam rolling, light walking, stretching, meditation, or other low-impact recovery exercises. \n\n"
        "The training schedule should be structured day-by-day with specific activities for each day, and must include recommended training "
        "timings for each exercise. Here is an example of the desired format and level of detail:\n\n"
        "Day 1 (Monday):\n"
        "   - Warm-up: Dynamic stretching and a light jog (e.g., 10 minutes)\n"
        "   - Sprint Drills: Multiple sprint exercises with full recovery (e.g., 4 x 50m sprints with 1-2 minutes rest between sprints)\n"
        "   - Technical Drills: Ball control and passing exercises (e.g., 20 minutes)\n"
        "   - Strength Training: Lower body exercises (e.g., squats, lunges, 15 minutes)\n"
        "   - Cool-down: Light jogging and stretching (e.g., 10 minutes)\n\n"
        "Day 2 (Tuesday):\n"
        "   - Warm-up: Jogging and dynamic stretches (e.g., 10 minutes)\n"
        "   - Agility Drills: Ladder drills and cone exercises (e.g., 20 minutes)\n"
        "   - Tactical Drills: Football-specific drills (e.g., positional play, passing under pressure, 30 minutes)\n"
        "   - Cool-down: Static stretching (e.g., 10 minutes)\n\n"
        "Day 3 (Wednesday): Rest Day\n"
        "   - Healthy Recovery: Gentle yoga, light walking, foam rolling, and meditation (e.g., 20-30 minutes of recovery activities)\n\n"
        "Day 4 (Thursday):\n"
        "   - Warm-up: Dynamic stretching and a light jog (e.g., 10 minutes)\n"
        "   - Sprint and Endurance Drills: Sprint exercises with active recovery (e.g., 6 x 100m sprints with jogging recovery, 15 minutes total)\n"
        "   - Strength and Conditioning: Core and plyometric exercises (e.g., 20 minutes)\n"
        "   - Cool-down: Stretching and deep breathing exercises (e.g., 10 minutes)\n\n"
        "Day 5 (Friday):\n"
        "   - Warm-up: Ball work combined with dynamic stretching (e.g., 10 minutes)\n"
        "   - Technical Skills: Dribbling, shooting, and ball control drills (e.g., 30 minutes)\n"
        "   - Agility & Coordination: Cone drills and balance exercises (e.g., 15 minutes)\n"
        "   - Cool-down: Stretching exercises (e.g., 10 minutes)\n\n"
        "Day 6 (Saturday): Rest Day\n"
        "   - Healthy Recovery: Light stretching, foam rolling, or a relaxed walk, along with hydration and meditation (e.g., 20-30 minutes)\n\n"
        "Day 7 (Sunday):\n"
        "   - Warm-up: Light jogging and dynamic stretches (e.g., 10 minutes)\n"
        "   - Match Simulation: Scrimmage or tactical drills replicating match scenarios (e.g., 40 minutes)\n"
        "   - Recovery: Cool-down activities including static stretching and foam rolling (e.g., 15 minutes)\n\n"
        "Based on the detailed performance report provided below, please generate a similar day-by-day training schedule for the next 1 week. "
        "Ensure that the schedule is football-specific, includes both training sessions and two full rest days with healthy recovery activities, "
        "and specifies the recommended training timing for each exercise according to the insights from the report.\n\n"
        "Detailed Performance Report:\n\n"
    )

    prompt += report
    prompt += (
        "\n\nGenerate the full 1-week training schedule in the format shown above with clear daily recommendations, activities, and "
        "training timings for each exercise, including healthy recovery strategies on the rest days."
    )

    return prompt


def generate_prompt_with_history_and_report(training_history_json: str, performance_report: str) -> str:
    """
    Generate a prompt for an LLM to create a new training schedule for an 11-year-old football player
    based on historical training data and a performance analysis report.

    Parameters:
        training_history_json (str): A JSON string containing an array of past training schedules with timestamps.
        performance_report (str): The LLM-generated performance analysis report based on player's metrics.

    Returns:
        str: A prompt string for the LLM.
    """
    # Parse the JSON string to ensure it's valid
    training_history = json.loads(training_history_json)

    prompt = (
        "You are an experienced AI football trainer and coach specialized in youth development. "
        "Your task is to analyze the training performance of an 11-year-old football player and design a new 7-day training schedule. "
        "Use the historical training sessions provided below along with the performance report to plan a new, creative, safe, and effective training schedule. \n\n"

        "Guidelines:\n"
        "- The training must be age-appropriate for an 11-year-old boy.\n"
        "- Include a variety of activities: warm-up, drills, strength, agility, tactical skills, match simulation, and cool-down.\n"
        "- Include training **timing for each exercise** (e.g., 10 minutes, 15 minutes, etc.).\n"
        "- Include **2 rest days** (non-consecutive if possible).\n"
        "- On rest days, add **healthy recovery activities** like stretching, foam rolling, light walking, breathing exercises, or meditation.\n"
        "- Do not repeat the same drills every day—incorporate learning from historic schedules and avoid overtraining similar muscle groups.\n"
        "- Avoid including fixed times like '9 AM'. Let the LLM decide if needed based on intensity/volume.\n"
        "- Training duration per day should be moderate (e.g., 45–60 minutes total) to suit the age group.\n\n"

        "🧾 Performance Report:\n"
        f"{performance_report}\n\n"

        "📊 Historical Training Schedules:\n"
    )

    for entry in training_history.get("trainings", []):
        prompt += f"\nCreated on: {entry['create_date_time']}\n{entry['training']}\n"

    prompt += (
        "\n\nNow based on the above history and analysis report, generate a **new 7-day training schedule** in the following format:\n\n"
        "Day 1 (Monday):\n"
        "   - Warm-up: Light jog and dynamic stretching (10 minutes)\n"
        "   - Technical Drill: Passing under pressure (15 minutes)\n"
        "   - Strength Training: Bodyweight squats and lunges (10 minutes)\n"
        "   - Tactical Awareness: Small-sided game (15 minutes)\n"
        "   - Cool-down: Breathing and stretching (10 minutes)\n\n"
        "Day 2 (Tuesday): ...\n"
        "...\n\n"
        "Please ensure the weekly plan reflects learning and variation from past training history, incorporates the performance feedback, "
        "focuses on both development and injury prevention, and stays engaging and balanced for a young athlete."
    )

    return prompt


def generate_training_promptaa(training_history_json: str, performance_report: str) -> str:
    """
    Generate a prompt for an LLM to create a new training schedule for an 11-year-old football player
    based on historical training data and a performance analysis report.

    Parameters:
        training_history_json (str): A JSON string containing past training schedules with timestamps.
        performance_report (str): The performance analysis report detailing the player's health and performance.

    Returns:
        str: A prompt string for the LLM.
    """
    # Parse the JSON string to ensure it's valid
    training_history = json.loads(training_history_json)

    prompt = (
        "You are an experienced AI football trainer specializing in youth development. "
        "Your task is to analyze the training performance of an 11-year-old football player and design a new 7-day training schedule. "
        "Use the historical training sessions provided below along with the performance report to plan a new, creative, safe, and effective training schedule. "
        "But the new training should be different than historical training sessions. \n\n"

        "Guidelines:\n"
        "- The training must be age-appropriate for an 11-year-old boy.\n"
        "- Include a variety of activities: warm-up, drills, strength, agility, tactical skills, match simulation, and cool-down.\n"
        "- Specify the duration for each exercise (e.g., 10 minutes, 15 minutes, etc.).\n"
        "- Include 2 rest days (non-consecutive if possible).\n"
        "- On rest days, suggest healthy recovery activities like stretching, foam rolling, light walking, breathing exercises, or meditation.\n"
        "- Avoid repeating the same drills every day—incorporate learnings from historical schedules and prevent overtraining of similar muscle groups.\n"
        "- Do not include fixed times like '9 AM'; determine the timing based on intensity and volume.\n"
        "- Training duration per day should be moderate (e.g., 45–60 minutes total) to suit the age group.\n"
        "- **Health Considerations:** If the performance report indicates health issues, adjust the training plan accordingly. "
        "For minor health concerns, recommend light activities such as gentle stretching or light walking. "
        "For significant health issues, suggest complete rest or bed rest as appropriate.\n\n"

        "Performance Report:\n"
        f"{performance_report}\n\n"

        "Historical Training Schedules:\n"
    )

    for entry in training_history.get("trainings", []):
        prompt += f"\nCreated on: {entry['create_date_time']}\n{entry['training']}\n"

    prompt += (
        "\n\nBased on the above history and analysis report, generate a new 7-day training schedule in the following format:\n\n"
        "Day 1 (Monday):\n"
        "   - Warm-up: Light jog and dynamic stretching (10 minutes)\n"
        "   - Technical Drill: Passing under pressure (15 minutes)\n"
        "   - Strength Training: Bodyweight squats and lunges (10 minutes)\n"
        "   - Tactical Awareness: Small-sided game (15 minutes)\n"
        "   - Cool-down: Breathing and stretching (10 minutes)\n\n"
        "Day 2 (Tuesday): ...\n"
        "...\n\n"
        "Please ensure the weekly plan reflects learnings and variations from past training history, incorporates the performance feedback, "
        "focuses on both development and injury prevention, and remains engaging and balanced for a young athlete. "
    )

    return prompt


def generate_training_prompt(training_history_json: str, performance_report: str, question: str) -> str:
    """
    Generate a prompt for an LLM to create a new training schedule for an 11-year-old football player
    based on historical training data and a performance analysis report.

    Parameters:
        training_history_json (str): A JSON string containing past training schedules with timestamps.
        performance_report (str): The performance analysis report detailing the player's health and performance.

    Returns:
        str: A prompt string for the LLM.
    """
    # Parse the JSON string to ensure it's valid
    training_history = json.loads(training_history_json)

    prompt = (
        "You are an experienced AI football trainer specializing in youth development. "
        "Your task is to analyze the training performance of football player and design a new training schedule according to user question below.\n"
        f"user question: {question}\n\n"
        "Use the historical training sessions provided below along with the performance report to plan a new, creative, safe, and effective training schedule. "
        "But the new training should be different than historical training sessions. \n\n"

        "Guidelines:\n"
        "- The training must be age-appropriate from the performance report.\n"
        "- The training must be according to user question \n"
        "- Include a variety of activities: warm-up, drills, strength, agility, tactical skills, match simulation, and cool-down.\n"
        "- Specify the duration for each exercise (e.g., 10 minutes, 15 minutes, etc.).\n"
        "- Include 2 rest days (non-consecutive if possible).\n"
        "- On rest days, suggest healthy recovery activities like stretching, foam rolling, light walking, breathing exercises, or meditation.\n"
        "- Avoid repeating the same drills every day—incorporate learnings from historical schedules and prevent overtraining of similar muscle groups.\n"
        "- Do not include fixed times like '9 AM'; determine the timing based on intensity and volume.\n"
        "- Training duration per day should be moderate (e.g., 45–60 minutes total) to suit the age group.\n"
        "- **Health Considerations:** If the performance report indicates health issues, adjust the training plan accordingly. "
        "For minor health concerns, recommend light activities such as gentle stretching or light walking. "
        "For significant health issues, suggest complete rest or bed rest as appropriate.\n\n"

        "Performance Report:\n"
        f"{performance_report}\n\n"

        "Historical Training Schedules:\n"
    )

    for entry in training_history.get("trainings", []):
        prompt += f"\nCreated on: {entry['create_date_time']}\n{entry['training']}\n"

    prompt += (
        "\n\nBased on the above history and analysis report, generate a new training schedule in the following format:\n\n"
        "Day 1 (Monday):\n"
        "   - Warm-up: Light jog and dynamic stretching (10 minutes)\n"
        "   - Technical Drill: Passing under pressure (15 minutes)\n"
        "   - Strength Training: Bodyweight squats and lunges (10 minutes)\n"
        "   - Tactical Awareness: Small-sided game (15 minutes)\n"
        "   - Cool-down: Breathing and stretching (10 minutes)\n\n"
        "Day 2 (Tuesday): ...\n"
        "...\n\n"
        "Please ensure the weekly plan reflects learnings and variations from past training history, incorporates the performance feedback, "
        "focuses on both development and injury prevention, and remains engaging and balanced for a young athlete. "
    )

    return prompt


def generate_prompt_routh(question: str):
    prompt = (
        "You are a classification assistant. You will be given a user's question.\n "
        "If the question is related to training schedules (such as session timings, rescheduling, practice plans, or training updates), respond only with:\n\n "
        "KB \n\n"
        "If the question is about anything else (e.g., strategy, performance analysis, general AI tasks, injuries, team formation, or anything not directly about training schedule), respond only with: \n\n"
        "AI \n\n"
        "Do not provide any explanation. Just return either KB or AI. \n"
        "Here is the user's question: \n"
        f"{question}\n"
    )

    return prompt



def extract_name(question: str) -> str:
    prompt = f"""
    You are an intelligent assistant. Your task is to extract the full name(s) of any person mentioned in the given sentence or question.

    Only return the name(s) as plain text (e.g., "John Doe"). If no name is found, return "None".

    ### Examples:

    Input: "When is the next training session for Sarah Johnson?"  
    Output: Sarah Johnson

    Input: "Has Dr. Ahmed Ali submitted the report?"  
    Output: Ahmed Ali

    Input: "Can you tell me who scheduled the last meeting?"  
    Output: None

    Input: "Schedule a session with Michael Jordan next week."  
    Output: Michael Jordan

    Input: "Is there any feedback from Coach Linda?"  
    Output: Linda

    ### Now extract name(s) from the following input:
    "{question}"
    """
    return prompt


def prompt_translation(question: str):
    # Prompt to detect and translate non-English
    prompt = f"""
            Detect if the following question is in English. 
            If it is NOT in English, translate it to English and return the translated version only.
            If it is already in English, return it as-is.

            Question: "{question}"
            """
    return prompt


def generate_rank_prompt(users_data: dict) -> str:
    """
    Generates a prompt to instruct an LLM to analyze each player's metrics and trainings
    in chronological order to assign a rank between 0 to 100 with two decimal places.
    """

    prompt = """
You are an expert sports performance evaluator. Given player metrics and training history for a list of athletes, evaluate and assign a `rank` score between 0.00 and 100.00 for each player. 

**Rules for Evaluation:**
1. For each user:
   - Sort `player_metrics` by `create_date_time` from oldest to newest.
   - Sort `player_trainings` by `create_date_time` from oldest to newest.
2. Evaluate overall performance based on:
   - Progression over time in physical and physiological metrics.
   - Frequency, variety, and intensity of trainings.
   - Consider rest, recovery, and training consistency.
3. Compare players collectively to rank them fairly.
4. Final `rank` should be a floating number with **two decimal precision**, in the range of **0 to 100**, reflecting performance and improvement.

Here is the player data in JSON format:
"""

    prompt += "\n\n" + json.dumps(users_data, indent=2)
    prompt += "\n\nPlease return the same JSON with the `rank` field for each player filled based on the analysis."

    return prompt

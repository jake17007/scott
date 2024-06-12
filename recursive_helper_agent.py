import json

from openai import OpenAI

STOPPING_LVL = 2  # How many levels of recursive research should we do?

client = OpenAI()

def query(prompt):
    chat = client.chat.completions.create(model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ])
    return chat.choices[0].message.content

def research_goal_helper(goal, recursion_lvl, stopping_lvl):
    if recursion_lvl < stopping_lvl:

        example_format = """
            {
                "goal_raw_text": "<original description>",
                "smart_goal_description": "<specific, measurable, actionable, etc...>",
                "tracking_metric": "<the name of a metric from the avilable metrics, or suggest a new metric>",
                "target_value": "<the current value of the given metric>",
                "deadline": "<the deadline of the goal in the format YYYY-MM-DD HH:MM:SS>",
                "subgoal_options": [
                    <list of three options for smart subgoals (strings)>
                ]
            }
        """

        example_response = """
            {
                "goal_raw_text": "lose 5 pounds of fat",
                "smart_goal_description": "Lose 5 Pounds of Body Fat within 10 weeks",
                "tracking_metric": "body_weight_pounds",
                "target_value": "180",
                "deadline": "2024-08-21 00:00:00",
                "subgoal_options": [
                    "Lose .5 Pounds of Body Fat wthin 1 week", 
                    "Exercise for 20 minutes by the end of the day",
                    "Eat salad for lunch today"
                ]
            }
        """

        available_metrics = """
            - body_weight_pounds: 180
            - body_fat_percentage: 16.5
            - daily_timespent_at_gym: 0,
            - salads_eaten: 0
        """

        prompt = f"""
            Create a smart goal from this natural language goal input as if you were a project manager.

            Goal: "{goal}"

            Your response should follow the formatting:
            {example_format}

            For example:
            {example_response}

            Available metrics:
            {available_metrics}

            Note:
            - subgoals should have a deadline of LESS THAN HALF of the original goal's deadline
            - today's date is 2024-06-12
        """
        response = json.loads(query(prompt))
        print(json.dumps(response, indent=4))
        [research_goal_helper(subgoal, recursion_lvl + 1, stopping_lvl) for subgoal in response["subgoal_options"]]

def research_goal(goal):
    research_goal_helper(goal, 0, STOPPING_LVL)

# research_goal("gain 10 pounds of muscle and look like a greek god / abercrombie model or smth")
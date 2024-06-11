import random
import time

from openai import OpenAI

# returns "red" 75% of the time, otherwise "blue"
def get_ball_color():
    value = random.random()
    if value < .75:
        return "red"
    return "blue"

class BallAgent:
    def __init__(self):
        self.brain = OpenAI()
        self.memory = []

    # ignore this, just reverses a list and make it a string
    def _reversed_memory_str(self):
        return ", ".join(reversed(self.memory))

    def guess_ball_color(self):
        prompt = f"""
            Try to guess which color the ball will be...

            Options (alphabetical order): blue, red

            Don't forget that the most recent ball colors 
            (starting with the most recent from left to right) were:
            {self._reversed_memory_str()}

            Please respond with a SINGLE WORD RESPONSE: the color of the ball
        """
        print("prompt: ", prompt)
        chat = self.brain.chat.completions.create(model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ])
        return chat.choices[0].message.content
    
    def act(self, state):
        response = self.query()
        return response

agent = BallAgent()
# train
for i in range(100):
    print(i)
    guess = agent.guess_ball_color()
    ball_color = get_ball_color()
    print(f"guess: {guess}, ball_color: {ball_color}")
    agent.memory.append(ball_color)
    time.sleep(1)

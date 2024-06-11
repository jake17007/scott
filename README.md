# Playground

run.py shows an agent learning to guess the color of a ball
- at each second, the agent guesses the next ball's color (blue or red)
- unknown to the agent, there always is a 75% chance of red (25% chance of blue)
- the agent has access to "memory" of the previous balls' colors included in its context

## Explanation

this explains how a very basic learning agent with a goal and state of their environment (context) could be modeled

'''
State:  # (aka metric, a digital representation of an entity)
- current_time
- current_state[][]  # a table
- get_history()  # returns collection of states over time
- update(t)  # returns data from sources (fitbit) and updates current_state

Goal:  # (aka metric goal)
- id
- target_state[][]  # the desired state (i.e. target values of the metric)
- target_time  # (deadline)

Agent:
- brain  # an llm; for example, can do `response = brain.query(prompt)`
- goal_id # the agent's goal (a target state)
- update(state):
    prompt = """
        Based on the current state, what action do you want to pick to reach your goal?
        State: {state}
        Goal: {goal}

        Here's your available actions:
        {available_actions}

        Respond with the actions as a list ['foo', 'bar', 'baz']

        OR

        Create a new action e.g. ['foo', 'def my_fun():\n    print('hello')', 'baz']

        OR

        Create a subgoal (with a target metric) and subagent
        
        OR

        ...

        Don't foget your previous actions {action_history} and results {state.get_history()}
    """
    actions = self.brain.query()
    actions.act()  # updates state in real world


for t in timesteps:
    state.update(t)
    agents.update(state)
'''


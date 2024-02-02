import utils
import flappy_bird_gym
import time
import random
import numpy as np

class SmartFlappyBird:
    def __init__(self, iterations):
        self.Qvalues = utils.Counter()
        self.landa = 1
        self.epsilon = None
        self.alpha = None 
        self.iterations = iterations  # Training

    def policy(self, state):
        # implement the best way to get action base on current state
        return self.max_arg(state)

    @staticmethod
    def get_all_actions():
        return [0, 1]

    @staticmethod
    def convert_continuous_to_discrete(state):
        # implement the best way to convert continuous distance values to discrete values
        # range of x : (0.000, 1.650)
        # range of y : (-0.500, 0.650)

        x, y = state

        rounded_x = round(x, 1)
        rounded_y = round(y, 1)

        if rounded_x == -0.0:
            rounded_x = 0.0
        if rounded_y == -0.0:
            rounded_y = 0.0

        return rounded_x, rounded_y

    def compute_reward(self, prev_info, new_info, done, observation):
        # implement the best way to compute reward base on observation and score
        observation = self.convert_continuous_to_discrete((observation))
        _, y = observation
        if done:  # Lost
            return -1000
        # Inside Pipe
        elif (0 <= y and y <= 0.05):
            new_info['score'] = prev_info['score'] + 1
            return 500
        else:  # Continues
            return 1

    def get_action(self, state):
        # implement the best way to get action base on current state
        if utils.flip_coin(self.epsilon):  # Random
            rand = random.randint(0, 100)
            choice = 1
            if rand < 90:
                choice = 0
            return SmartFlappyBird.get_all_actions()[choice]
        else:  # Based on Policy
            return self.policy(state)

    def maxQ(self, state):
        # return max Q value of a state
        state = self.convert_continuous_to_discrete(tuple(state))
        actions = self.get_all_actions()
        q_values = [self.Qvalues.get((state, action), 0) for action in actions]
        return max(q_values)

    def max_arg(self, state):
        # return argument of the max q of a state
        state = self.convert_continuous_to_discrete(tuple(state))
        actions = self.get_all_actions()
        values = [self.Qvalues.get((state, action), 0)
                  for action in actions]
        return actions[np.argmax(values)]

    def update(self, reward, state, action, next_state):
        # update q table
        state = self.convert_continuous_to_discrete(state)
        next_state = self.convert_continuous_to_discrete(next_state)
        my_tuple = state, action
        max_arg_next_state = self.max_arg(next_state)
        self.Qvalues[my_tuple] += self.alpha * \
            (reward + self.landa * (self.Qvalues[next_state, max_arg_next_state]) -
             self.Qvalues[my_tuple])

    def update_epsilon_alpha(self):
        # update epsilon and alpha base on iterations
        return NotImplemented

    def run_with_policy(self, landa):
        self.landa = landa
        env = flappy_bird_gym.make("FlappyBird-v0")
        observation = env.reset()
        info = {'score': 0}
        observations = []
        for _i in range(self.iterations):
            info = {'score': 0}
            while True:
                action = self.get_action(observation)  # policy affects here
                this_state = observation
                prev_info = info
                observation, reward, done, info = env.step(action)
                observations.append(observation)
                reward = self.compute_reward(prev_info, info, done, observation)
                self.update(reward, this_state, action, observation)
                self.update_epsilon_alpha()
                if done:
                    observation = env.reset()
                    break

        env.close()

    def run_with_no_policy(self, landa):
        scores = []
        for _ in range(10):
            self.landa = landa
            # no policy test
            env = flappy_bird_gym.make("FlappyBird-v0")
            observation = env.reset()
            info = {'score': 0}
            while True:
                action = self.get_action(observation)
                prev_info = info
                observation, reward, done, info = env.step(action)
                reward = self.compute_reward(prev_info, info, done, observation)
                env.render()
                time.sleep(1 / 30)  # FPS
                if done:
                    break
            env.close()
            scores.append(info['score'])

    def run(self):
        self.run_with_policy(1)
        self.run_with_no_policy(1)


program = SmartFlappyBird(iterations=2000)
program.run()

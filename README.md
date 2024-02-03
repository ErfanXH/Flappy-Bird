<div align='center'>

<h1>Flappy Bird AI</h1>
<p>This project aims to implement a <i>Reinforcement Learning</i> agent using Q-learning to play the <i>Flappy Bird</i> game. </p>

<p>
  Flappy Bird is a popular mobile game that was developed by Dong Nguyen. The game features a bird which the player controls by tapping the screen. Each tap causes the bird to briefly fly upwards, and then the bird starts falling due to gravity. The objective of the game is to navigate the bird through pairs of pipes that are coming from the right side of the screen to the left without touching them. The pipes are positioned at different heights and have a gap in between them. The game is over if the bird touches a pipe or the ground. The player's score is increased by one each time the bird successfully passes through a pair of pipes. The game is known for its high level of difficulty and addictive nature.
</p>

</div>

## :star2: About the Project

### :camera: Screenshots
<p align="center" width="100%">
  <a href=""><img src="Images/game_main.png" alt='image' width="30%" height='400'/></a>
  <a href=""><img src="Images/30.png" alt='image' width="30%" height='400'/></a>
  <a href=""><img src="Images/50.png" alt='image' width="30%" height='400'/></a>
<!--   <<a href=""><img src="Images/62.png" alt='image' width="25%" height='400'/></a> -->
</p>

## :toolbox: Getting Started

### :bangbang: Prerequisites

- Install python (python 3.8 Preferably) <a href="https://www.python.org/downloads/release/python-380/"> Here</a>
- Install gym environment
```bash
pip install gym
```
- Install flappy_bird_gym
```bash
pip install flappy_bird_gym
```


### :scroll: Code of Conduct

<div>
<p>Here's a breakdown of the class and its methods:</p>

<p><b>__init__(self, iterations)</b>: Initializes the agent with an empty Q-table, learning rate (alpha), discount factor (landa), exploration rate (epsilon), and the number of training iterations.</p>

<p><b>policy(self, state)</b>: Returns the action with the highest Q-value for the given state.</p>

<p><b>get_all_actions()</b>: Returns all possible actions (0 and 1).</p>

<p><b>convert_continuous_to_discrete(state)</b>: Converts the continuous state values to discrete values by rounding them to one decimal place.</p>

<p><b>compute_reward(self, prev_info, new_info, done, observation)</b>: Computes the reward based on the game status. If the game is over (done is True), it returns a large negative reward. If the bird is inside the pipe, it increases the score and returns a large positive reward. Otherwise, it returns a small positive reward.</p>

<p><b>get_action(self, state)</b>: Decides whether to take a random action (exploration) or the action with the highest Q-value (exploitation) based on the epsilon value. In test mode (mode is 1), it always chooses the action with the highest Q-value.</p>

<p><b>maxQ(self, state)</b>: Returns the maximum Q-value for the given state.</p>

<p><b>max_arg(self, state)</b>: Returns the action with the maximum Q-value for the given state.</p>

<p><b>update(self, reward, state, action, next_state)</b>: Updates the Q-value for the given state-action pair based on the Q-Learning update rule.</p>

<p><b>update_epsilon_alpha(self)</b>: Decreases the alpha and epsilon values over time to reduce the learning rate and the exploration rate.</p>

<p><b>run_with_policy(self, landa)</b>: Runs the game with the current policy for a given number of iterations. It updates the Q-table after each action and resets the game when it's over.</p>

<p><b>run_with_no_policy(self, landa)</b>: Runs the game without the policy (always choosing random actions) and prints the scores.</p>

<p><b>run(self)</b>: Runs the game with the policy, switches to test mode, and then runs the game without the policy.</p>

<p>The last lines of the code create an instance of the SmartFlappyBird class and run the game.</p>
</div>

## :warning: License

Distributed under the MIT License.

This code is provided by <a href="https://github.com/ErfanXH">ErfanXH</a> and all rights are reserved.

Project Link: [https://github.com/ErfanXH/Flappy-Bird](https://github.com/ErfanXH/Flappy-Bird)

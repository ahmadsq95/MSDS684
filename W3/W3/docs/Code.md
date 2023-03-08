%%html
<style>
  table {margin-left: 0 !important;}
</style>

# TODO
- [ ] In notebooks use data_structures.py
- [ ] Refer to code in RLGridWorld

### Notebooks 

- [ ] FirstVisitMCPrediction.ipynb
- [ ] IterativePolicyEvaluation.ipynb
- [ ] MCExploringStarts.ipynb
- [ ] OffPolicyMCControl.ipynb
- [ ] OffPolicyMCPrediction.ipynb
- [ ] OnPolicyFirstVisitMCControl.ipynb
- [ ] PolicyFromValues.ipynb
- [ ] PolicyIteration.ipynb
- [ ] QLearning.ipynb
- [ ] RLDataStructures.ipynb
- [ ] Sarsa.ipynb
- [ ] StandardAndNegativeGrids.ipynb
- [ ] TD0Prediction.ipynb
- [ ] ValueIteration.ipynb
- [ ] ValuesAndAPolicy.ipynb

# Algorithms for Gridworld

1 IterativePolicyEvaluation.ipynb - Computes value of a policy
2 PolicyIteration.ipynb - Compute values, update policy, until no policy update
3 ValueInteration.ipynb - Alternates computing value and policy update
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PolicyFromValues.ipynb - Utility to compute the optimal policy from given values 
2 FirstVisitMCPrediction.ipynb - Needs to be done
5 OnPolicyFirstVisitMCControl.ipynb
6 OffPolicyMCPrediction.ipynb - Needs to be done
7 OffPolicyMCControl.ipynb - Needs to be sdone
9 TD0Prediction.ipynb -
10 Sarsa.ipynb - Needs to be done 
11 QLearning.ipynb - 

| Number  | Page | Notebook | Description |
|---------|:-----|:---------|:------------|
|	1	  | 75	 | IterativePolicyEvaluation | Iterative Policy Evaluation, for estimating V | 
|	2	  | 80	 | PolicyIteration | Policy Iteration for estimating π | 
|	3	  | 83	 | ValueIteration | Value Iteration, for estimating π | 
|	4	  | 92	 | FirstVisitMCPrediction | First-visit MC prediction, for estimating V | 
|	5	  | 99	 | MCExploringStarts | Monte Carlo ES (Exploring Starts), for estimating π | 
|	6	  | 101	 | OnPolicyFirstVisitControl | On-policy first-visit MC control (for epsilon-soft policies), estimates π | 
|	7	  | 110	 | OffPolicyMCPrediction | Off-policy MC prediction (policy evaluation) for estimating Q | 
|	8	  | 111	 | OffPolicyMCControl | Off-policy MC control, for estimating π | 
|	9	  | 120	 | TD0Prediction | Tabular TD(0) for estimating V | 
|	10	  | 130	 | Sarsa | Sarsa (on-policy TD control) for estimating Q | 
|	11	  | 131	 | QLearning | Q-learning (off-policy TD control) for estimating π | 
|	12	  | 136	 |  | Double Q-learning, for estimating Q | 
|	13	  | 144	 |  | n-step TD for estimating V | 
|	14	  | 147	 |  | n-step Sarsa for estimating Q | 
|	15	  | 149	 |  | Off-policy n-step Sarsa for estimating Q | 
|	16	  | 154	 |  | n-step Tree Backup for estimating Q | 
|	17	  | 156	 |  | Off-policy n-step Q | 
|	18	  | 202	 |  | Gradient Monte Carlo Algorithm for Estimating V | 
|	19	  | 203	 |  | Semi-Gradient TD(0) for estimating V | 
|	20	  | 209	 |  | n-step semi-gradient TD for estimating V | 
|	21	  | 244	 |  | Episodic Semi-gradient Sarsa for Estimating Q | 
|	22	  | 247	 |  | Episodic semi-gradient n-step Sarsa for estimating Q | 
|	23	  | 251	 |  | Differential semi-gradient Sarsa for estimating Q | 
|	24	  | 255	 |  | Differential semi-gradient n-step Sarsa for estimating Q | 
|	25	  | 328	 |  | REINFORCE: Monte-Carlo Policy-Gradient Control (episodic) for π | 
|	26 	  | 330	 |  | REINFORCE with Baseline (episodic), for estimating π | 
|	27	  | 332	 |  | One-step Actor-Critic (episodic), for estimating π | 
|	28	  | 332	 |  | Actor-Critic with Eligibility Traces (episodic), for estimating π | 
|	29	  | 333	 |  | Actor-Critic with Eligibility Traces (continuing), for estimating π | 


# Functionality for using Reinforcement Learning algorithms

## playgridworld.py

```
# default game starting point is state = (0,0) 
# list of tuples that are (state, reward) pairs

def play_game(gw, policy, state=(0,0)):

def move(state, action): # only valid actions at states are sent to move

```

## algorithms.py

```
from grid import Grid

# from page 75 of Sutton and Barto, RL, 2nd. Ed.
def iterative_policy_evaluation(gw, policy, gamma=0.9, epsilon=0.001):

# from page 80 of Sutton and Barto, RL, 2nd. Ed.
def policy_iteration(gw, policy, gamma=0.9, epsilon=0.001):

# from page 83 of Sutton and Barto, RL 2nd. Ed.
def value_iteration(gw, gamma=0.9, epsilon=0.001):

# computes policy from values - argmax( values ) - my algorithm
def compute_policy_from_values(gw, gamma=0.9):

```

## data_structures.py

```
from grid import Grid

# defines a function of a state
def init_V(gw): # V maps states to real numbers

def init_pi(gw): # pi maps states to actions

# defines a function of a state and an action
def init_Q(gw): # Q maps states and actions tp real numbers

# defines a function of a state and an action
def init_C(gw):  # Q maps states and actions tp real numbers

# Returns maps states and actions to a list
def init_Returns(gw): 

```

# Functionality for creating gridworld environments

## env.py

```
""" creates standard and negative grids"""
from grid import Grid

def create_standard_grid(rewards=0.0):

def create_negative_grid(rewards=-0.1):

```

## grid.py

```
from node import Node

class Grid:
    """GridWorld's Grid of Nodes"""

    # Create Grid as list of lists with M rows and N columns
    def __init__(self, numberRows, numberColumns):
        
    # define iterator for states in grid
    def __iter__(self):
 
    # define next i,j pair for iterator
    def __next__(self):    

    def get_node(self,state):

    def print_grid_state(self):    

    def print_grid_rewards(self):

    def init_rewards(self,reward):
        
    def is_valid_node_index(self,i,j): 

    def is_barrier(self,state):

    def set_barrier(self,state):

    def is_terminal(self,state):

    def set_terminal(self,state):

    def set_reward(self,state,direction,reward):

    def valid_decisions(self,state):

    def valid_decisions_and_rewards(self,state):

    def set_value(self,state,value):

    def get_value(self,state):

    def get_reward_for_action(self,state,action):

    def get_value_at_destination(self,state,action):

    def print_grid_states_decisions(self):

    def print_values(self):

    def print_policy(self,policy):

```

## node.py

```
# this class contains the definition of a node for the gridworld problem
# a node --
#   1. knows where it is
#   2. has a value, that can be updated
#   3. knows if it is a terminal node
#   4. knows if it is a barrier node
#   5. knows what rewards are available for taking an action (left, right, up, down) 
#      - Reward is None if action is invalid

class Node:
    """GridWorld Node"""
    
    def __init__(self):
        self.state = None           # (i,j) tuple of coordinates of node
        self.value = None           # value of the node
        self.is_terminal = False    # flag for terminal state
        self.is_barrier = False     # flag for barrier state
        self.left = None        # immediate reward for left, None if invalid
        self.right = None       # immediate reward for right, None if invalid    
        self.down = None        # immediate reward for down, None if invalid
        self.up = None          # immediate reward for up, None if invalid
    
    # setters and getters for node values
    def set_state(self,state):
    def get_state(self):
    def set_value(self,value):
    def get_value(self):
    def set_is_terminal(self,terminal):
    def get_is_terminal(self):
    def set_is_barrier(self,barrier):
    def get_is_barrier(self):
    
    # setters and getters for rewards for actions
    def set_left(self,reward):
    def get_left(self):
    def set_right(self,reward):
    def get_right(self):
    def set_down(self,reward):
    def get_down(self):
    def set_up(self,reward):
    def get_up(self):

```

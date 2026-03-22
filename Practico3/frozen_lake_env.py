import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map

class FrozenLakeEnv:
    def __init__(self, *args, **kwargs):
        self.env = gym.make(*args, **kwargs)

    @property
    def action_space(self):
        return self.env.action_space
    
    @property
    def observation_space(self):
        return self.env.observation_space

    def reset(self):
        return self.env.reset()[0]

    def step(self, action):
        obs, reward, done, _, _ = self.env.step(action)
        return obs, reward, done

    def render(self):
        return self.env.render()
    
    def map(self):
        return self.env.unwrapped.desc
    
    def grid_size(self):
        return self.env.unwrapped.desc.shape[0]
    
    def state_to_coords(self, state):
        n = self.grid_size()
        x = state % n
        y = state // n
        return x, y
    
    def goal(self):
        desc = self.env.unwrapped.desc
        nrow, ncol = desc.shape
        return nrow * ncol - 1
    
    def initial_state(self):
        return 0
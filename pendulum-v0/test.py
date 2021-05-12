import gym
import numpy as np
import pdb
env = gym.make('Pendulum-v0')
env.reset()

for _ in range(1000):
    env.render()
    # pdb.set_trace()
    obs,rew,done,_ = env.step(np.array([0.0]))
    # pdb.set_trace()
env.close()
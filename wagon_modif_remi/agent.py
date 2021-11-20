import gym
import numpy as np
from wagon_organise import WagonOrganise

env = WagonOrganise()
env.reset()
env.render()
sum_items = 0
sum_reward = 0
for _ in range(50):
    action = (np.random.randint(12), np.random.randint(3))
    observation, reward, done, info = env.step(action)
    print("le coli est placé à la position : ", action,
          "la récompense est : ", reward)
    sum_items = sum_items + 1 if reward > 0 else sum_items
    sum_reward = sum_reward + reward
    env.render()
print("le nombre d'items placés est : ", sum_items,
      "la somme des récompenses est : ", sum_reward,)

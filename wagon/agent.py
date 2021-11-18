import gym
import numpy as np
from wagon_organise import WagonOrganise

env = WagonOrganise()
env.reset()
for _ in range(20):
    action = (np.random.randint(13), np.random.randint(3))
    observation, reward, done, info = env.step(action)
    print("le coli est placé à la position : ", action,
          "le coli est de taille : ", observation,
          "la récompense pour avoir mit le colis est : ", reward)
    env.render()

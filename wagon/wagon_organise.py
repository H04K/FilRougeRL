import gym
import numpy as np
from numpy.core.einsumfunc import einsum_path
from gym.utils import seeding
from gym import error, spaces, utils


class WagonOrganise():
    def __init__(self):
        self.items = [(1, 3), (3, 3), (5, 1), (5, 1), (5, 1), (3, 3)]
        self.width = 12
        self.height = 3
        self.knapsack = np.zeros((self.width, self.height))
        self.state = None

    def step(self, action):
        """
        :param action: Tuples of (x, y) coordinates of item to put in the knapsack
        :return: state, reward, done, info
        """
        info = {}
        reward = 0
        done = False
        remove_current_item = False
        space_avaible = True
        try:
            if action[0] + self.items[0][0] <= self.width \
                    and action[1] + self.items[0][1] <= self.height:
                # put item in the wagon
                for i in range(action[0], self.items[0][0] + action[0]):
                    for j in range(action[1], self.items[0][1] + action[1]):
                        if self.knapsack[i, j] == 1:
                            space_avaible = False
                            break
                if space_avaible:
                    remove_current_item = True
                    for i in range(action[0], self.items[0][0] + action[0]):
                        for j in range(action[1], self.items[0][1] + action[1]):
                            self.knapsack[i, j] = 1
                # remove item from the list
                if remove_current_item:
                    self.items.pop(action[1])
        except IndexError:
            done = True

        if remove_current_item:
            reward = 1
        else:
            reward = -1

        # state = next item and the reshape state
        result = np.zeros((self.width * self.height)+2)
        result[:2] = self.items[0]
        result[2:] = self.knapsack.flatten()

        return result, reward, done, info

    def render(self):
        print(self.knapsack)
        return

    def reset(self):
        self.items = [(1, 3), (3, 3), (5, 1), (5, 1), (5, 1), (3, 3)]
        self.knapsack = np.zeros((self.width, self.height))
        result = np.zeros((self.width * self.height)+2)
        result[:2] = self.items[0]
        result[2:] = self.knapsack.flatten()

        return result

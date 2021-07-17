# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:17:53 2020

@author: Doc
"""

import gym
env = gym.make('Pendulum-v0')
env.reset() #returns an initial observation
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()
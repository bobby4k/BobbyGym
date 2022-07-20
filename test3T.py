#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Tic-Tac-Toe 井字棋
#   仅仅用来测试自定义env

import gym
import gym_ttt
from random import shuffle

env = gym.make('TTT-v0', render_mode=None)

action_all = []
for x in range(3):
    for y in range(3):
        action_all.append((x,y))

for i_episode in range(10):
    shuffle(action_all)
    env.reset()

    i_step = 0 
    for action in action_all:
        i_step += 1
        print("step {} in episode {} with x{} y{}".format(i_step,i_episode+1, action[0], action[1])  )
        observation, reward, done, info = env.step(action)
        if done:
            print("Game Finish")            
            break

env.close()
print('bye~')
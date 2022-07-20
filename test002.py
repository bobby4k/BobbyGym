#!/usr/bin/python
# -*- coding: UTF-8 -*-
import gym
from numpy import take_along_axis

env = gym.make('CartPole-v0')

t_all = []  #计算能坚持的平均setp
for i_episode in range(20):
    observation = env.reset()  #环境给出的初始反馈
    for t in range(100):
        env.render()
        # print(observation)
        action = env.action_space.sample()  #产生一个随机行动
        observation, reward, done, info = env.step(action)  #得到行动的反馈
        if done:
            print("Esisode[{}] finished after {} timesteps\n".format(i_episode+1,t+1))
            t_all.append(t)
            break
        #END if done
    #END for setp
#END for episode

env.close()
print("we played {} steps".format(sum(t_all)/len(t_all)))
#maybe 25.95 steps


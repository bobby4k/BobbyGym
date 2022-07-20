#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 添加小车反馈：如果杆往右歪，则往右走；
"""
「观测状态」有四维：
    小车位置、小车速度、杆的角度和杆顶端的速度（初始状态每个值均在 ±0.05 区间内取随机值）；
「终止条件」有三条：
    杆的角度大于 ±12 度，小车的位置超过 ±2.4，以及迭代次数超过 200（v1 为 500）；
每个步骤的「奖励」均为 1（包括终止步）。
"""
import gym

env = gym.make("CartPole-v0")
t_all = []
action_bef = 0  #纪律上一次action
action_threshold = 0.1  #阈值

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        cp, cv, pa, pv = observation
        #pa代表棍子倾斜角度
        if abs(pa) <= action_threshold:
            action = 1 - action_bef
        elif pa >= 0: 
            action = 1
        else:
            action = 0
        observation, reward, done, info = env.step(action)
        action_bef = action  #纪律上一次移动距离
        if done:
            print("Esisode[{}] finished after {} timesteps vs last pa {}\n".format(i_episode+1,t+1, pa))
            t_all.append(t)
            break
    #END for step
#END for i

env.close()
print("we can make {} steps\n".format(sum(t_all)/len(t_all)))
#maybe 42.75 steps,  根据不同action_bef阈值 0.1~0.3, 结果正相关
#END FILE
#!/usr/bin/python
# -*- coding: UTF-8 -*-
""""
井字棋 
    action固定规则:自动根据counter 偶数O, 奇数X
"""
from platform import win32_edition
import gym
from gym import Env, error, spaces, utils


DEFAULT_TTT_TIC = '-'
class TTTEnv(gym.Env):

    def __init__(self, render_mode=None):
        self.reset()  #开始既重置环境

        self.render_mode = render_mode
        #必须定义 spaces
        self.observation_space = spaces.Box(low=0,high=2,dtype=int)
        self.action_space = spaces.Discrete(2)

        # self.render()

    def step(self, action):
        x,y = action[0],action[1]  #棋盘坐标，0-2
        if self.done :
            print("Game Over")
            return self.state, self.reward, self.done, self.add
        elif  x>=3 or y>=3 or self.state[x][y] != DEFAULT_TTT_TIC:
            print("invalid step")
            return self.state, self.reward, self.done, self.add
        else:
            #偶数O
            self.state[x][y] = 'O' if (self.counter % 2 == 0) else 'X' 
            self.counter += 1
            if self.counter == 9: 
                self.done = 1 #放满棋盘

        self.render()  #展示当前棋盘

        win = self.check()  #判断胜负
        # print("dadsadsa win{}".format(win))
        if win:  #0无人获胜 1玩家胜 2电脑胜
            self.done = 1
            win_user = 'agent' if win==1 else 'target'
            print(" {} 获胜, congratulations".format(win_user))
            self.add[win_user] = 1
            self.reward = 1 if win==1 else -1  #玩家胜利则奖励

        return self.state, self.reward, self.done, self.add

    def check(self):
        if self.counter < 5:
            return 0
        for i in range(3): # 判断横竖三行是否有连子，有则返回对应胜者
            if self.state[i][0] != DEFAULT_TTT_TIC and self.state[i][1] == self.state[i][0] and self.state[i][1] == self.state[i][2]:
                if self.state[i][0] == 'O': # o代表第一名选手的棋子
                    return 1
                else:
                    return 2
            if self.state[0][i] != DEFAULT_TTT_TIC and self.state[1][i] == self.state[0][i] and self.state[1][i] == self.state[2][i]:
                if self.state[0][i] == 'O': # o代表第一名选手的棋子
                    return 1
                else:
                    return 2
        # 判断两条对角线上是否有连子
        if self.state[0][0] != DEFAULT_TTT_TIC and self.state[1][1] == self.state[0][0] and self.state[1][1] == self.state[2][2]:
            if self.state[0][0] == 'O': # o代表第一名选手的棋子
                    return 1
            else:
                return 2
        if self.state[0][2] != DEFAULT_TTT_TIC and self.state[1][1] == self.state[0][2] and self.state[1][1] == self.state[2][0]:
            if self.state[0][2] == 'O': # o代表第一名选手的棋子
                return 1
            else:
                return 2
        # 所有其他情况均无胜者
        return 0

    #打印3x3表格
    def render(self):
        print("\tTic-Tac-Toe Table:")
        for i in range(3):
            print("\n\t", end='') #换一行
            for j in range(3):
                print(self.state[i][j], end=' ')
        print("\n")

    def reset(self):
        super().reset()

        self.state = [[DEFAULT_TTT_TIC for _ in range(3)] for _ in range(3)]
        self.counter = 0  #当前步数, 偶数O, 奇数X
        self.done = 0  #对局结束
        self.add = {'agent':0, 'target':0}  #两个玩家 1表示胜利
        self.reward = 0
        return self.state

    def getPosition(self,x,y):
        item = self.state[x][y]
        return item

    def close(self):
        print("env closed")


#END class


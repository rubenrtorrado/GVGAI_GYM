#!/usr/bin/env python
import gym
import gym_gvgai
import Agent as Agent



env = gym_gvgai.make('gvgai-aai-lvl0-v0')
agent = Agent.Agent()
print('Starting ' + env.env.game + " with Level " + str(env.env.lvl))
total_score = list()  # record every testing score
testing_times = 100  # total testing times
# reset environment
actions = env.env.GVGAI.actions()
stateObs = None
for i in range(testing_times):  # testing 100 times
    current_score = 0  # record current testing round score
    stateObs = env.reset()
    for t in range(1000):
        # env.render()
        # choose action based on trained policy
        action_id = agent.act(stateObs, actions)
        # do action and get new state and its reward
        stateObs, increScore, done, debug = env.step(action_id)
        current_score += increScore
        # print("Action " + str(action_id) + " tick " + str(t+1) + " reward " + str(increScore) + " win " + debug["winner"])
        # break loop when terminal state is reached
        if done:
            print("Game over at game tick " + str(t+1) + " with player " + debug['winner'] + ", score is " + str(current_score))
            total_score.append(current_score)
            break
print(sum(total_score) / len(total_score))

#!/usr/bin/env python
import gym
import gym_gvgai
import Agent as Agent

testing_times = 20
# Predefined names referring to framework
games = ['gvgai-cec1', 'gvgai-cec2', 'gvgai-cec3']
training_levels = ['lvl0-v0', 'lvl1-v0','lvl2-v0']
test_levels = ['lvl3-v0', 'lvl4-v0']

for game_name in games:
    for level in test_levels:
        env = gym_gvgai.make(game_name + '-'+level)
        agent = Agent.Agent()
        print('Starting ' + env.env.game + " with Level " + str(env.env.lvl))
        total_score = list()  # record every testing score
        # reset environment
        actions = env.env.GVGAI.actions()
        state_obs = None
        for i in range(testing_times):  # testing 100 times
            current_score = 0  # record current testing round score
            state_obs = env.reset()
            for t in range(1000):
                # env.render()
                # choose action based on trained policy
                action_id = agent.act(state_obs, actions)
                # do action and get new state and its reward
                state_obs, incre_score, done, debug = env.step(action_id)
                current_score += incre_score
                # print("Action " + str(action_id) + " tick " + str(t+1) + " reward " + str(increScore) + " win " + debug["winner"])
                # break loop when terminal state is reached
                if done:
                    print("Game over at game tick " + str(t+1) + " with player " + debug['winner'] + ", score is " + str(current_score))
                    total_score.append(current_score)
                    break
        print(sum(total_score) / len(total_score))

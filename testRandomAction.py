import gym
import gym_gvgai

env = gym.make('gvgai-aliens-lvl0-v0')
env.reset()

score = 0
for i in range(100):
    action_id = env.action_space.sample()
    state, reward, isOver, info = env.step(action_id)
    score += reward
    #print("Action " + str(action_id) + " played at game tick " + str(i+1) + ", reward=" + str(reward) + ", new score=" + str(score))
    test = info['grid'][0][0][0]
    #if(test):
    #    print(test.itypeKey)
    #else:
    #    print("None")
    if isOver:
        print("Game over at game tick " + str(i+1) + " with player " + info['winner'])
        break

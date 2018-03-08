import gym
import gym_gvgai
env = gym.make('aliens-gvgai-v0')	#Can't specify levels yet
env.reset()

import timeit

start = timeit.timeit()

for i in range(1000):
    #env.render()
    image, score, end, info = env.step(env.action_space.sample()) # take a random action
    if(end):
    	print(i)
    	break
end = timeit.timeit()

print(end - start)
#Probably have issues running twice on same machine
	#Log files will clash
	#Socket numbers will clash

#TODO:
	#Allow level selection
	#Get game screen size
	#Make sure java server shuts down correctly
	#Get available moves for a game
	#Make game selection not based on a file list
	#Turn GVGAI into a jar file
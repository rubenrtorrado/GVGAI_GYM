import gym
import gym_gvgai
env = gym.make('aliens-gvgai-v0')	#Can't specify levels yet
env.reset()
for i in range(100):
    #env.render()
    image, score, end, info = env.step(env.action_space.sample()) # take a random action
    if(end):
    	print(i)
    	break

#Probably have issues running twice on same machine
	#Log files will clash
	#Socket numbers will clash

#TODO:
	#Allow level selection
	#Get game screen size
	#Get available moves for a game
	#Make game selection not based on a file list
	#Turn GVGAI into a jar file
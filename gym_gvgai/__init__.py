from gym.envs.registration import registry, register, make, spec
import os

dir = os.path.dirname(__file__)
gamePath = os.path.join(dir, os.path.normpath('envs/games'))
games = os.listdir(gamePath)

#games = [g[:-9] for g in gameFiles if '_lvl0.txt' in g] #generate games list

for game in games:
	for lvl in range(5):
		#    for obs_type in ['image', 'json']:
		# space_invaders should yield SpaceInvaders-v0 and SpaceInvaders-ram-v0
		name = game.split('_')[0]
		version = int(game.split('_')[1][1:])
		register(
    		id='gvgai-{}-lvl{}-v{}'.format(name, lvl, version),
    		entry_point='gym_gvgai.envs.gvgai_env:GVGAI_Env',
    		kwargs={'game': name, 'level': lvl, 'version': version},    #'obs_type': obs_type
    		max_episode_steps=2000
    		#nondeterministic=nondeterministic,
    		#Play with different setups here
		)
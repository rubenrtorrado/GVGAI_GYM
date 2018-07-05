from gym.envs.registration import registry, register, make, spec
import os

dir = os.path.dirname(__file__)
gamesPath = os.path.join(dir, os.path.normpath('envs/games'))
games = os.listdir(gamesPath)

for game in games:
	gamePath = os.path.join(gamesPath, game)
	if(os.path.isdir(gamePath)):
		#Currently if there are more than 5 levels, JavaServer.java will not load them. It expects lvl0 - lvl4.
		lvls = len([lvl for lvl in os.listdir(gamePath) if 'lvl' in lvl])
		for lvl in range(lvls):
			#    for obs_type in ['image', 'json']:
			# space_invaders should yield SpaceInvaders-v0 and SpaceInvaders-ram-v0
			name = game.split('_')[0]
			version = int(game.split('_')[-1][1:])
			register(
	    		id='gvgai-{}-lvl{}-v{}'.format(name, lvl, version),
	    		entry_point='gym_gvgai.envs.gvgai_env:GVGAI_Env',
	    		kwargs={'game': name, 'level': lvl, 'version': version},    #'obs_type': obs_type
	    		max_episode_steps=2000
	    		#nondeterministic=nondeterministic,
	    		#Play with different setups here
			)
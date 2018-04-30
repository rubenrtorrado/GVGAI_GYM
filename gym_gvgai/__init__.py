from gym.envs.registration import registry, register, make, spec
import os

dir = os.path.dirname(__file__)
gamePath = os.path.join(dir, os.path.normpath('envs/games'))
gameFiles = os.listdir(gamePath)

games = [g[:-9] for g in gameFiles if '_lvl0.txt' in g] #generate games list

for game in games:
#    for obs_type in ['image', 'json']:
    # space_invaders should yield SpaceInvaders-v0 and SpaceInvaders-ram-v0
    register(
        id='{}-gvgai-v0'.format(game),
        entry_point='gym_gvgai.envs.gvgai_env:GVGAI_Env',
        kwargs={'game': game},    #'obs_type': obs_type
        max_episode_steps=2000
        #nondeterministic=nondeterministic,
        #Play with different setups here
    )
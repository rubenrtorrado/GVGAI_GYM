#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simulate VGDL Games
"""
import os
import sys
import numpy as np

dir = os.path.dirname(__file__)
gvgai_path = os.path.join(dir, "gvgai", "clients", "GVGAI-PythonClient", "src", "utils")
sys.path.append(gvgai_path)

import gym
from gym import error, spaces, utils
import ClientCommGYM as gvgai

class GVGAI_Env(gym.Env):
    """
    Define a VGDL environment.
    The environment defines which actions can be taken at which point and
    when the agent receives which reward.
    """

    def __init__(self, game):
        self.__version__ = "0.0.1"
        print("GVGAI_Env - Version {}".format(self.__version__))

        gameID = temp_game_id(game)
        #self.GVGAI = gvgai.ClientCommGYM(gameID, dir)
        self.GVGAI = gvgai.ClientCommGYM()

        #Only allow gridphysics games for now
        #Get number of moves for a selected game
        self.action_space = spaces.Discrete(3)

        # Observation is the remaining time
        #screen_height, screen_width = self.GVGAI.gameSize()
        self.observation_space = spaces.Box(low=0, high=255, shape=(110, 300, 4), dtype=np.uint8)
        print("GET SCREEN DIMENSIONS!!! (FIX: Right now just 200x200)")

    def step(self, action):
        """
        The agent takes a step in the environment.
        Parameters
        ----------
        action : int
        Returns
        -------
        ob, reward, episode_over, info : tuple
            state (image) :
                An image of the current frame of the game
            reward (float) :
                Total reward (Philip: Should it be incremental reward? Check Atari)
            isOver (bool) :
                whether it's time to reset the environment again.
            info (dict):
                info that can be added for debugging
        """
        state, reward, isOver = self.GVGAI.step(action)
        
        return state, reward, isOver, {}

    def reset(self):
        """
        Reset the state of the environment and returns an initial observation.
        Returns
        -------
        observation (object): the initial observation of the space.
        """
        return self.GVGAI.reset()

    def render(self, mode='human', close=False):
        #Add rendering capability
        #If we add render, add close
        return

def temp_game_id(name):
    #Move games out of examples folder
    games = ["aliens", "angelsdemons", "assemblyline", "avoidgeorge", "bait",
                "beltmanager", "blacksmoke", "boloadventures", "bomber", "bomberman",
                "boulderchase", "boulderdash", "brainman", "butterflies", "cakybaky",
                "camelRace", "catapults", "chainreaction", "chase", "chipschallenge",
                "clusters", "colourescape", "chopper", "cookmepasta", "cops",
                "crossfire", "defem", "defender", "digdug", "dungeon",
                "eighthpassenger", "eggomania", "enemycitadel", "escape", "factorymanager",
                "firecaster", "fireman", "firestorms", "freeway", "frogs",
                "garbagecollector", "gymkhana", "hungrybirds", "iceandfire", "ikaruga",
                "infection", "intersection", "islands", "jaws", "killBillVol1",
                "labyrinth", "labyrinthdual", "lasers", "lasers2", "lemmings",
                "missilecommand", "modality", "overload", "pacman", "painter",
                "pokemon", "plants", "plaqueattack", "portals", "raceBet",
                "raceBet2", "realportals", "realsokoban", "rivers", "roadfighter",
                "roguelike", "run", "seaquest", "sheriff", "shipwreck", 
                "sokoban", "solarfox", "superman", "surround", "survivezombies",
                "tercio", "thecitadel", "thesnowman", "waitforbreakfast", "watergame",
                "waves", "whackamole", "wildgunman", "witnessprotection", "wrapsokoban",
                "zelda", "zenpuzzle"]
    return games.index(name)

ACTION_MEANING = {
    0 : "NOOP",
    1 : "FIRE",
    2 : "UP",
    3 : "RIGHT",
    4 : "LEFT",
    5 : "DOWN",
}
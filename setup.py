#!/usr/bin/env python
import os
import sys
import setuptools
import build as java

from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

#Run gym_gvgai/envs/gvgai/build.py to compile Java source code.
path = os.path.join(os.path.dirname(__file__), "gym_gvgai", "envs", "gvgai")

class InstallWithJava(install):
    def run(self):
        """compile special java dependencies before the others."""
        java.main(path)
        install.run(self)

class DevelopWithJava(develop):
    def run(self):
        """compile special java dependencies before the others."""
        java.main(path)
        develop.run(self)

class EggInfoWithJava(egg_info):
    def run(self):
        """compile special java dependencies before the others."""
        #java.main(path)
        egg_info.run(self)

setup(name='gym_gvgai',
	version='0.0.3',
	packages= find_packages(),
	install_requires=['gym>=0.10.5', 'numpy>=1.13.3', 'pillow>=5.3.0'],
	cmdclass = {
		'install': InstallWithJava,
		'develop': DevelopWithJava,
        'egg_info': EggInfoWithJava,
		}
	)

#Make sure a git pull doesn't result in weird error where java isn't rebuilt
#so the compiled code doesnt match the source code.
# Solution: Git hook -> post-merge -> delete build directory

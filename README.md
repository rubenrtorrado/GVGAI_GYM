# GVGAI GYM

An [OpenAI Gym](gym.openai.com) environment for games written in the [Video Game Description Language](http://www.gvgai.net/vgdl.php), including the [Generic Video Game Competition](http://www.gvgai.net/) framework.

## Installation

- Clone this repository to your local machine.
- To install the package, run `pip install -e <package-location>`
  (This should install OpenAI Gym automatically, otherwise it can be installed [here](https://github.com/openai/gym)
- Install a Java compiler `javac` (e.g. `sudo apt install openjdk-9-jdk-headless`)

## Usage

Demo video on [YouTube](https://youtu.be/O84KgRt6AJI)

Once installed, it can be used like any OpenAI Gym environment.

Run the following line to get a list of all GVGAI environments.
```Python
[env.id for env in gym.envs.registry.all() if env.id.startswith('gvgai')]
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/rubenrtorrado/GVGAI_GYM.

## License

This code is available as open source under the terms of the [Apache License 2.0](https://opensource.org/licenses/Apache-2.0).

# GVGAI Single-Player Competition @CIG18

The 2nd GVGAI Single-Player Competition will be organised at [the IEEE’s 2018 Conference on Computational Intelligence and Games (CIG18)](https://project.dke.maastrichtuniversity.nl/cig2018/?page_id=255).

**Important notice: A new GVGAI-Gym will be used in this competition. The competition rules have been changed.**

## Rules
Due to the long training time, the GVGAI server won’t be used for training your agent. Please train your agent using your own machine or server.

### Preparation

Download and set up the new GVGAI-Gym framework on your machine/server.

Demo video on [YouTube](https://youtu.be/O84KgRt6AJI)

### Training Phase (NOW - 1 July 2018)

Program your agent and train it 
- on as many games/levels as you want;
- using as much time as you want for deciding an action per game tick;
- using as much time as you want for training.

### Validation Phase (2 - 22 July 2018)

- On 2 July 2018, we will release 3 games (G1, G2 and G3) and 2 levels each for training. Unknown levels of the same 3 games will be used for validation. 
- Train your agent on the given levels of given games using as much time as you want.

### Submission

- Zip your trained agent.
- Submit your agent to the competition. 
- Submission will be opened from 3 July 2018 and closed at 22 July 2018 23:59 (GMT).

*Remark: no feedback will be given until the bug report phase will start.*

### Bug Report Phase 

- Submission will be closed at 22 July 2018 23:59 (GMT).
- You will be contacted if we have problems running your agent on our server.

### Validation Phase

Your agent will play multiple time the same games (G1, G2 and G3) that we have released for training, but on private levels.
At this phase, your agent should return a legal action in **no more than 100ms per game tick**.

## Timeline

- Release games for competition: 2 July 2018
- Submission deadline: 22 July 2018 23:59 (GMT)
- Testing on server: 23-27 July 2018 23:59 (GMT)
- Starting validation on server: 28 July 2018
- Announcement of results: during the CIG18

## Resources

[GVGAI website](http://www.gvgai.net)

[GVGAI-Gym (master branch)](https://github.com/rubenrtorrado/GVGAI_GYM) 

[Demo video on YouTube](https://youtu.be/O84KgRt6AJI)

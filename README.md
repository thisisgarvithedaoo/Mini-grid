<p align="center">
    <img src="https://raw.githubusercontent.com/Farama-Foundation/Minigrid/master/minigrid-text.png" width="500px"/>
</p>

<p align="center">
  <img src="figures/door-key-curriculum.gif" width=200 alt="Figure Door Key Curriculum">
</p>

The Minigrid library contains a collection of discrete grid-world environments to conduct research on Reinforcement Learning. The environments follow the [Gymnasium]() standard API and they are designed to be lightweight, fast, and easily customizable. 

# Installation

To install the Minigrid library use `pip install minigrid`.

We support Python 3.7, 3.8, 3.9 and 3.10 on Linux and macOS. We will accept PRs related to Windows, but do not officially support it.

# Environments
The included environments can be divided in two groups. The original `Minigrid` environments and the `BabyAI` environments. 

## Minigrid
The list of the environments that were included in the original `Minigrid` library can be found in the [documentation](https://minigrid.farama.org/environments/minigrid/). These environments have in common a triangle-like agent with a discrete action space that has to navigate a 2D map with different obstacles (Walls, Lava, Dynamic obstacles) depending on the environment. The task to be accomplished is described by a `mission` string returned by the observation of the agent. These mission tasks include different goal-oriented and hierarchical missions such as picking up boxes, opening doors with keys or navigating a maze to reach a goal location. Each environment provides one or more configurations registered with Gymansium. Each environment is also programmatically tunable in terms of size/complexity, which is useful for curriculum learning or to fine-tune difficulty.

## BabyAI
These environments have been imported from the [BabyAI](https://github.com/mila-iqia/babyai) project library and the list of environments can also be found in the [documentation](https://minigrid.farama.org/environments/babyai/). The purpose of this collection of environments is to perform research on grounded language learning. The environments are derived from the `Minigrid` grid-world environments and include an additional functionality that generates synthetic
natural-looking instructions (e.g. “put the red ball next to the box on your left”) that command the the agent to navigate the world (including unlocking doors) and move objects to specified locations in order to accomplish the task.
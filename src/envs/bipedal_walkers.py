"""
This environment is adapted from gymnasium library
"""

from os import getcwd, path
import numpy as np

from gymnasium import utils
from gymnasium.envs.mujoco import MujocoEnv
from gymnasium.spaces import Box

DEFAULT_CAMERA_CONFIG = {
  "trackbodyid": 1,
  "distance": 4.0,
  "lookat": np.array((0.0,0.0,0.8925)),
  "elevation": -20.0,
}

class BipedalWalkerV1(MujocoEnv, utils.EzPickle):
  metadata = {
    "render_modes": [
      "human",
      "rgb_array",
      "depth_array"
    ],
    "render_fps" : 80
  }

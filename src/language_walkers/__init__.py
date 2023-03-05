from gymnasium.envs.registration import register


register(
  id="bipedal_walker-v1",
  entry_point="language_walkers.envs:BipedalWalkerV1",
  max_episode_steps=1000,
)

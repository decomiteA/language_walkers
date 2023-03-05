from setuptools import setup


setup(
  name="language_walkers",
  version="0.0.1",
  author="Antoine de Comite",
  author_email="antoinedecomite@gmail.com",
  description="Different kind of walkers simulated in MuJoCo",
  python_requires=">=3.7.1",
  install_requires=["gymnasium==0.27.0", "mujoco==2.3.1.post1"]
)

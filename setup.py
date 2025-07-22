from pathlib import Path
from setuptools import find_packages, setup


long_description = (Path(__file__).parent / "README.md").read_text()

core_requirements = [
    # "gymnasium==0.29.1",
    # "tqdm==4.66.4",
    # "ipdb==0.13.13",
    # "mujoco==3.1.6",
    # "mujoco-mjx==3.1.6",
    # "dm_control",
    # "brax==0.9.4",
]

setup(
    name="shadow_hand",
    version="1.0.0",
    author="Wenlong Huang, Igor Mordatch, Pieter Abbeel, Deepak Pathak (Modified by Youngdo Lee)",
    url="https://github.com/huangwl18/geometry-dex/tree/main",
    description="Dexterous Manipulation Benchmark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">3.7",
    install_requires=core_requirements,
)
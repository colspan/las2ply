from setuptools import setup, find_packages
import las2ply

setup(
    name='las2ply',
    version='0.0.1',
    packages=[
        'las2ply',
        'las2ply.format',
        'las2ply.convert',
    ],
    install_requires=[
        'laspy',
        'numpy',
        'open3d',
    ],
    entry_points={
        'console_scripts': [
            'las2ply = las2ply.command:las2ply_cmd',
        ],
    },
)

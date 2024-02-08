from setuptools import setup, find_packages

setup(
    name='ascii_graphics_engine',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ascii_graphics_engine = ascii_graphics_engine.runner:main',
        ],
    },
    install_requires=[
        'numpy>=1.24.4',
    ],
    license='MIT',
    keywords='3D, game, engine',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ],
)

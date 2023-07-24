from setuptools import setup

setup(
    name='Camera Tracking',
    version='0.0.1',  # Update with your project version
    description='Camera tracking software for integrating Televic Microphones with Panasonic PTZ Cameras',
    author='Kyle Langevin',
    author_email='kyle.langevin@gmail.com',
    packages=['Camera Tracking'],  # Update with the name of your main package

    # Add the URL to your GitHub repository here
    install_requires=[
        'requests',
        'tkinter',
        'threading',
    ],

    dependency_links=[
        'https://github.com/Chrisrdouglas/pynasonic_ptz/tarball/master'
    ],

    # Other optional information you may want to include
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


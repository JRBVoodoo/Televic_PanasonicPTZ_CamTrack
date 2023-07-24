from setuptools import setup

setup(
    name='Televic_Panasonic_CameraTracking',
    version='0.0.1',  # Update with your project version
    description='Camera tracking software for integrating Televic Microphones with Panasonic PTZ Cameras',
    author='Kyle Langevin',
    author_email='kyle.langevin@gmail.com',
    packages=['Televic_Panasonic_CameraTrack'],  # Update with the name of your main package

    # Add the URL to your GitHub repository here
    install_requires=[
        'git+https://github.com/Chrisrdouglas/pynasonic_ptz.git',
        'requests',
        'tkinter',
        'threading',
    ],

    # Other optional information you may want to include
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


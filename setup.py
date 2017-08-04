from setuptools import setup

requirements = [
    # package requirements go here
]

setup(
    name='buzz',
    version='0.1.0',
    description="Queries the FAA Airport Status API",
    author="Curtis Hampton",
    author_email='CurtLHampton@gmail.com',
    url='https://github.com/CurtLH/buzz',
    packages=['buzz'],
    entry_points={
        'console_scripts': [
            'buzz=buzz.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='buzz',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)

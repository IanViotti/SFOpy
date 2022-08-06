import setuptools

setuptools.setup(
    name="SFOpy",
    version="0.1.0",
    author="Ian Viotti",
    description="Creates Sunflower Optimization algorithm",
    packages=setuptools.find_packages(), 
    classifiers=[  
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
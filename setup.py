from setuptools import setup, find_packages

setup(
    name="nepali_word_to_speech",  # Replace with your library name
    version="0.1.0",
    author="Padam Prasad Dhakal",
    author_email="your.email@example.com",
    description="A Python library to convert Nepali words to speech",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PadamPrasadDhakal/Nepali-Word-to-Speech",  # Replace with your repository URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 
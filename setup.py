import setuptools

setuptools.setup(
    name="voice-feedback",
    version="0.1.0",
    author="Will Crichton",
    author_email="wcrichto@cs.stanford.com",
    description="",
    url="https://github.com/willcrichton/voice-feedback",
    packages=['src'],
    python_requires='>=3.6',
    install_requires=['torch', 'pyannote.audio @ git+https://github.com/pyannote/pyannote-audio.git']
)

from setuptools import setup

setup(
    name="petriflow",
    version="0.1.0",
    author="stackdump",
    author_email="myork@stackdump.com",
    description="declare and simulate Petri-nets using python",
    license='MIT',
    keywords='pflow petri-net statemachine statevector',
    packages=['petriflow'],
    include_package_data=True,
    install_requires='',
    long_description="""
    This library used to declare and simulate Petri-nets.

    Models declared using this library should be standard enought to convert to PNML or Pflow
    petri-net encoding, though currently does not provide a means to do so.
    """,
    url="https://pflow.dev",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License"
    ],
)

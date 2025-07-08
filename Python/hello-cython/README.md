# Hello Cython

Using Cython to boost Python performance and alleviate bottlenecks

## Prerequisites

See the [Cython docs for what you need to have installed](https://cython.readthedocs.io/en/stable/src/quickstart/install.html)

## Getting started

Set up the project
```shell
uv venv
```

Install the dependencies and build the project
```shell
uv sync
```
There's a lot of magic happening behind the scenes here, the setuptools/Cython set up does the following:
- Compiles the Cython files into C code
- Compiles the C code into a shared object file
- We can then use the .so files in Python as if they were regular Python modules

I'm oversimplifying, but that's the gist of it.

Run the code
```shell
uv run hello # or just python main.py
```

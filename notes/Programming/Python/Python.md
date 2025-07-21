# Python

## Virtual Environments

A virtual environment acts as a workspace that you can install different packages to and set up for specific projects. This can be handy as some packages my interfere with each other or some projects require older or new versions of a package. To set up a simple virtual environment the following command can be used.

``` bash
python3 -m venv <env_name>
```

To use that virtual environment you must `source` the `active` in the environments `bin` directory.


``` bash
source ~/.venv/<env_name>/bin/active
```

This is an example in reality the virtual environment may be located in a different directory.

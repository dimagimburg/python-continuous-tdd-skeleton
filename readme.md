# Python Project Skeleton For continuous TDD
This project is a full suite project ready for development with Test Driven Design and isolated virtual environment.

The directory structure is as follows:


## Run development environment
The development environment should be running under python3x versions
* For windows users - if you have both python 2.x and python 3.x installed please follow the next instructions:
    1. install globally virtualenv `pip install virtualenv` or `pip3 install virtualenv`
    2. Setup virtual environment `virtualenv --python="YOUR_PYTHON_PATH" venv --no-site-packages` (YOUR_PYTHON_PATH could be something like `c:\python36\python.exe`)
    3. `venv\Scripts\activate`
    4. `pip install -r requirements-dev.txt` this should install all development dependencies into the virtual environment.
    5. run `ptw` - this will run the tests continuously for faster TDD.
* Ubuntu users:
    1. install virtualenv `pip install virtualenv` (or ` sudo -H python3 -m pip install virtualenv`)
    2. virtualenv venv --no-site-packages
    3. `sudo python3 -m pip install -r requirements-dev.txt`
    4. `ptw`
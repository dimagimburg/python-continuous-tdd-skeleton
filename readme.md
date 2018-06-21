# Python Project Skeleton For continuous TDD
This project is a full suite project ready for development with Test Driven Design and isolated virtual environment.

The directory structure is as follows:


## Run development environment
The development environment should be running under python3x versions
* For windows users - if you have both python 2.x and python 3.x installed please follow the next instructions:
    1. Setup virtual environment `virtualenv --python="YOUR_PYTHON_PATH" venv --no-site-packages` (YOUR_PYTHON_PATH could be something like `c:\python36\python.exe`)
    2. `venv\Scripts\activate`
    3. `pip install -r requirements-dev.txt` this should install all development dependencies into the virtual environment.
    4. run `ptw` - this will run the tests continuously for faster TDD.
# Pre-requisites and setup

## Pre-requisites

This project is based on `Python3`, `pip` and `venv`.

### Installing Python3 on your Mac. 

On Mac, [Homebrew](https://brew.sh/) can be used (or download the official installer from [here](https://www.python.org/downloads/)).

Run the following command on a terminal:
```
brew install python
```
Check Python installation by getting the Python3 version:
```
python3 --version
```

## Project setup.

### Creating a virtual env with using the Python3 baked module `venv` (optional).
I recommend creating a Virual Env to avoid interfering other Python project on your local (and I consider it a good practice), although it is optional due to it does not impact the behavior of this implementation. For more information please visit [this documentation](https://docs.python.org/3/library/venv.html).

0. Clone this repository.
1. Move to the cloned repository's directory.
```
cd <path-to>/BackEndAutomationPython
```
2. Create the virtual env.
```
python3 -m venv ./
```
3. Activate the virtual env.
```
source bin/activate
```

### Installing project dependencies.
1. Move to the cloned repository's directory.
```
cd <path-to>/BackEndAutomationPython
```
2. Use `pip` to install dependencies.
```
pip install -r requirements.txt
```

### Sources
[Python3 Guide](https://python3.guide/).

## Postman mock server

In order to test the scenarios created on this project, a Postman collection is added in order to create a mock server to execute the test cases against.
To create the mock server, follow the steps bellow (more information on this Postman [documentation](https://learning.postman.com/docs/designing-and-developing-your-api/mocking-data/setting-up-mock/)):

- Install [Postman](https://www.postman.com/).
- Import the collection [My_API_for_testing.postman_collection.json](https://github.com/sebalanfranco/BackEndAutomationPython/blob/master/features/support/postman_collections/My_API_for_testing.postman_collection.json).
- From the collection's options, select "Mock collection".
- Copy the mock server url and replace the `{POSTMAN_MOCK_SERVER_URL}` place holder from the Behave [configuration file](https://github.com/sebalanfranco/BackEndAutomationPython/blob/master/behave.ini).
- You are ready to go! Follow [the tests execution](TestsExecution.md) documentation to start.


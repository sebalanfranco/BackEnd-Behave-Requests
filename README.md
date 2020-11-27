# BackEndAutomationPython

## What is the purpose of this repo?

The main goal is to implement a Python automation testing framework to test a simple REST API, in order to consolidate concepts about the language, quality assurance approach and communication strategy.
The core of this project is based on [Behave](https://behave.readthedocs.io/en/latest/), a BDD framework for Python. 

## What does this repo cover?

Given the main goal is to consolidate concepts and expose a quality assurance approach to tackle the REST API testing main aspects, the content is not going deeper on each topic but trying to identefy them and stablish a baseline for the implementation of an automation testing framework in Python. 

## Some practices used.

**JSon schema validation**: in order to check the structure of the API responses, JSon schemas are used (supported by [jsonschema](https://pypi.org/project/jsonschema/)).
**Utils custom modules**: aiming at keeping the steps definition as simple as possible, the code is organized in modules within the `steps/utils/` folder.
**Scenarios tagging**: all scenarios are organized in suites based on priority and featured affected using [tags](https://behave.readthedocs.io/en/latest/tag_expressions.html).
**Postmam mocking**: this is an extra mile. Given this project is mainly oriented on implementing a BDD automation framework for Python (no matter which API is under test), a Postman server is setup with some mocks in order to execute the tests (visit [this documentation](https://learning.postman.com/docs/designing-and-developing-your-api/mocking-data/setting-up-mock/)).

## Table of contents
- [Pre-requisites and setup](docs/Setup.md)
- [Testing approach](QA.md)
- [Tests execution](TestsExecution.md)
- [Reports](Reports.md)
- [Conclusions](Conclusions.md)

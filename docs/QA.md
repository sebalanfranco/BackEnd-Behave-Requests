# Quality Asurance approach

Listed below some of the QA practices implemented on this project.

The idea is to provide an overview of QA aspect used to build the tests and explain why each desition is taken.

## BDD: Gherkin as communication language

All the scenarios are written in [Gherkin syntax](https://cucumber.io/docs/gherkin/). 

Using the Given - When - Then structure, each test is written in a friendly syntax allowing to share and interact over them with different team members' roles. Using this as a common language to describe how a system should behave, allows QAs, devs, POs and other roles to interact more efficiently at early stages of the development proces. 

## Scenario tagging

This is a powerfull tool available in most of the automation frameworks that allows to orgnize the tests cases based on a totally customizable criteria.

In this project, the tests are organized and tagged based on the fuctionality and, crossing this criteria, prioritized into smoke, sanity and regression suites. This approach adds flexibility on executions, allowing to execute all the scenarios to test an specific feature or use them as a part of continues integration pipelines by playing with the smoke, sanity and regression tags. 

## API response validation with JSon schemas

This practice is attached to the system under test on this project, in this case, a RESTful API. 

JSon schemas is a powerful tool to validate the structure of an API response in one step. This project tries to keep the JSon schema validation as simple as possible, but trying to show of useful it is, using a core schema with all the reusable definitions in a file and then specifying the validation schema for each response (extending the definitions if needed).

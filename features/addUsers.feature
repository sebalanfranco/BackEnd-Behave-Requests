@users
@add
Feature: add users
    In order to add users to the system
    As a system admin
    I want to be able to send a request to the API
    
    @smoke
    Scenario: add a valid user
        When a POST request is sent to "/users" with body:
        """
            {
                "username": "sebalan",
                "name": "Seba",
                "lastname": "Lanfranco",
                "email": "sebalanfranco@whatever.com"
            }
        """
        Then the response should have the code "201"
        And the response body should have "metadata/code" equals to "201"
        And the response body should have "metadata/message" equals to "Created"
        And the response body should have "data/username" equals to "sebalan"
        And the response body should have "data/name" equals to "Seba"
        And the response body should have "data/lastname" equals to "Lanfranco"
        And the response body should have "data/email" equals to "sebalanfranco@whatever.com"
        And the repsonse body should be valid based on "add_user" schema
@users
@edit
Feature: edit users
    In order to edit existent users on the system
    As a system admin
    I want to be able to send a request to the API
    
    @smoke
    Scenario: edit a valid user
        When a PUT request is sent to "/users" with body:
        """
            {
                "id": 1,
                "username": "sebalan",
                "name": "Sebastian",
                "lastname": "Lanfranco",
                "email": "sebalanfranco@whatever.com"
            }
        """
        Then the response should have the code "200"
        And the response body should have "metadata/code" equals to "200"
        And the response body should have "metadata/message" equals to "OK"
        And the response body should have "data/id" equals to "1"
        And the response body should have "data/username" equals to "sebalan"
        And the response body should have "data/name" equals to "Sebastian"
        And the response body should have "data/lastname" equals to "Lanfranco"
        And the response body should have "data/email" equals to "sebalanfranco@whatever.com"
        And the repsonse body should be valid based on "edit_user" schema
        
    @regression
    Scenario: try to edit a user with not found id
        When a PUT request is sent to "/users" with body:
        """
            {
                "id": 99,
                "username": "sebalan",
                "name": "Sebastian",
                "lastname": "Lanfranco",
                "email": "sebalanfranco@whatever.com"
            }
        """
        Then the response should have the code "200"
        And the response body should have "metadata/code" equals to "200"
        And the response body should have "metadata/message" equals to "OK"
        And the response body should have "data/id" equals to "1"
        And the response body should have "data/username" equals to "sebalan"
        And the response body should have "data/name" equals to "Sebastian"
        And the response body should have "data/lastname" equals to "Lanfranco"
        And the response body should have "data/email" equals to "sebalanfranco@whatever.com"
        And the repsonse body should be valid based on "edit_user" schema
        
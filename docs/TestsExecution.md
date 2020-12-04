# Tests execution

Given all the scenarios are tagged as explained [here](https://github.com/sebalanfranco/BackEndAutomationPython/blob/master/docs/QA.md#scenario-tagging), the tests execution is pretty flexible by using the `behave` command.

## Test suites

- `@smoke`: contain the tests that ensures the core functionality of the API is healthy.
- `@sanity`: an step forward on validating the main features of the API, ensuring that all the functionalities are working as expected.
- `@regression`: alternative and error validation tests, ansures that the whole API is healthy.

## Execution commands

First of all, execute the steps in the [Setup](Setup.md) section. Once the setup is completed, execute all or specific test cases as follow. 

### All test cases

``` 
behave
```

### Specific suite

``` 
behave --tags=smoke
```

### Specific functionality

``` 
behave --tags=users
```

### Change base url if testing against another environment (replace `{ENV_URL}` placeholder)
``` 
behave -D url={ENV_URL}
```

Follow this Behave [documentation](https://behave.readthedocs.io/en/latest/tag_expressions.html) to know more about using tags.

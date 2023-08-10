Deployement Notes:

1. Clone the repo locally. 
2. Navigate to the folder/repo which haven been pulled/cloned locally.
3. Run the follwing command to setup the enviornment:

    ```
    pip install -r requirements.txt
    ```

3. Once the environement setup is complete. There will be a tests folder, which consists of all the test cases. User need to navigate to the master folder:

    a. To run all the test cases:      

      ```
      pytest -s -v  %test_folder% --browser %browser_name%
      ```


    b. To run indivisual feature file
    
    
      ```
      pytest %test_case_folder%/%test_case_name% --browser %browser_name%
      ```

    c. To run test suites. Test suites are defined by adding the tags to the Scenarios in the feature file:

    ```
    pytest %pytest_test_suite% --browser chrome
    ```

5. To generate allure report, this is a 2 step method

    a. Run the test suite by giving the behave allure command. PSB the command
    
    ```
    pytest %pytest_test_suite% --browser chrome --alluredir %directory_name%
    ```

    b. Generate allure based HTML report
    
    ``` 
    allure generate %allure_html_report_folder% --clean -o %%allure_result_folder%%
    ```

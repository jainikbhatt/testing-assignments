## Things need to do after cloning project
###### Check if python is installed or not if not then install python latest version using this link.
         - https://www.python.org/downloads/

###### Install selenium for selenium libraries:
        - For Windows: python -m pip install selenium 
###### Install pytest for python unit test framwork:
        - For Windows: pip install pytest
###### Install pytest-html for report generating:
        - For Windows: pip install pytest-html
###### Install Openpyxl for excel support:
        - For Windows: pip install Openpyxl

###### Install related drivers for open browser and replace driver path to the "open_Browser" variable which is located in testCases > test_cases.py
        - Note: you can downloads drivers using this link https://www.selenium.dev/documentation/en/webdriver/driver_requirements/ 

## For run test cases and generat report using this command.
###### <Project Path>pytest -v --html=Reports/report.html --self-contained-html  <testCases Path>

## Email with attached html report enter this command.
###### <testCases Path>py Email.py 

## For run data driven test case enter this command.
###### <Project Path>py DDTestCases.py

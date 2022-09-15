# PyBAPageTest
### Environment
- Chrome - version 104 or above
- Python - 3.7 (https://www.python.org/downloads/windows/, this should download a file similar in name to: python-3.7.9-amd64.exe)
- pip - latest (Please ensure pip is up to date by executing: `python -m pip install -U pip`)
- Allure - check HTML tes results (Please check below to see how to install Allure in Windows)
### Package structure
```
PyBAPageTest
|
│   README.md
│   requirements.txt                      ==> Python dependencies
|
└───allure_results                        ==> JSON test results for Allure to generate HTML test report.
|
└───src                       
   │
   └───driver
   |    └───chrome                        ==> Support chrome for now
   |           chromedriver.exe
   |
   └───features                           ==> BDD testing files      
   |      config.json                     ==> specify browser, to be extened for other configurations
   |
   └───pages                              ==> Selenium PageObjects
   |
   └───util                               ==> utility functions  
```
### How to run tests
1. Get the package: `Download ZIP` or git cmd: `git clone https://github.com/ericsunssg/PyBAPageTest.git`
2. When using `Download ZIP`, please unzip the file, e.g to `C:\Temp1` or any path (this article will use C:\Temp1 as an example) 
3. Set up Python virtural enviroment - Windows Cmd: `python -m venv C:\Temp1\PyBAPageTest-main\venv`
4. Activate the Python virtural environment -  Windows Cmd: `C:\Temp1\PyBAPageTest-main\venv\Scripts>activate`
5. Install the dependencies under Python virtual environment - `(venv) C:\Temp1\PyBAPageTest-main>pip install -r requirements.txt`
6. Run the test: `(venv) C:\Temp1\PyBAPageTest-main>behave ./src/features -f allure_behave.formatter:AllureFormatter -o allure_results`
7. The summary of test results will be shown and JSON test result files will be generated under `C:\Temp1\PyBAPageTest-main\allure_results`
8. Using Allure to check test results - Windows Powershell: `allure serve C:\Temp1\PyBAPageTest-main\allure_results`
> Note: the above step 6 generates JSON test results for Allure to generate HTML reports, it can also generate XML(`behave --junit`) and JSON report(`behave -f json`)
### How to install Allure in windows
- Windows PowerShell: `scoop install allure` 
- The above cmd may fail if scoop is not in your Windows, install it using PowerShell: `iwr -useb get.scoop.sh | iex`

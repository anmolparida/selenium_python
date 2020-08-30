*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem


*** Test Cases ***
Adding Chrome Driver to the Path Variable
    Log  %{PATH}
    Append To Environment Variable  PATH   C:\Users\aparida\OneDrive\Code\Selenium_Python\Drivers
    Log  %{PATH}
    Open Browser  https://www.google.com  browser=chrome
    Close All Browsers
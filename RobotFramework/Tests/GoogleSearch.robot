*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
This is Sample Test Case
    [Documentation]  Google Test
    [Tags]  Regression
    Open Browser  https://www.google.com/   chrome
    Close Browser

*** Keywords ***
Software Testing Mentor

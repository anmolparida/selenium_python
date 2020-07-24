*** Settings ***
Documentation  Basic Search Functionality
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
1. Verify Basic Search Functionality for eBay
    [Documentation]  This test case verifies the basic ebay search
    [Tags]  Functional,Regression
    #PreCondition
    Open Browser  https://www.ebay.com/  chrome
#    Maximize Browser Window
    #Steps
    Input Text  //input[@id='gh-ac']  Mobile
    Click Button   //input[@class='btn btn-prim gh-spr']
    Page Should Contain  results for Mobile
    #Post Condition
    Close Browser

*** Keywords ***

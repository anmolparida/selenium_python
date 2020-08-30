*** Settings ***
Library  RequestLibrary

*** Variables ***
${base_url}  http://dummy.restapiexample.com/api/v1/
${employeeId}  1


*** Test Cases ***
Get Employee Information
    Create Session  mysession ${employeeId}
    ${response} = get request mysession  employees/${employeeId}
    log to console  ${response.status_code}
    log to console  ${response.content}
    log to console  ${response.headers}

*** Keywords ***


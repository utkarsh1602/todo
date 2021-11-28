*** Settings ***
Library           RequestsLibrary

*** Variables ***
${DEMO_URL}      http://127.0.0.1:5000

*** Test Cases ***
Test
    create session  mysession   ${DEMO_URL}
    ${response}=    get on session     mysession   /
    
    log to console  ${response.status_code}
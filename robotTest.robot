*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        chrome
${URL}            https://www.google.com

*** Test Cases ***
Search on Google
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text      name=q    Robot Framework
    Press Keys      name=q    \\13  # Appuie sur la touche Entrée (Return)
    Wait Until Page Contains Element    css:div#search
    Page Should Contain Element    css:div#search

*** Keywords ***
Maximize Browser Window
    Maximize Browser Window

Press Keys
    [Arguments]    ${locator}    ${keys}
    Press Keys    ${locator}    ${keys}

*** Settings ***
Library     Per.py


*** Test Cases ***
test_case_1
    [Tags]    Level1
    ${a}   set variable  1
    log     ${a}
    should be equal  ${a}   1
test_case_2
   ${a}   set variable  1
    Per.pri      ${a}
   should be equal  ${a}   2



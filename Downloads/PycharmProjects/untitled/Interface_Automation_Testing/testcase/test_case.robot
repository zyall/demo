*** Settings ***
Library         ../Person.py
Variables       const.py

*** Variables ***


*** Test Cases ***
test case 1：摇一摇
    ${appId}   set variable   PA01100000000_01_SDK
    &{param}   create dictionary  userId=   deviceId=3df618b6c3c66882c8d656725b98929bb  devieceType=ios   osVersion=11   appId=${appId}    appVersion=4.4.0.0   sdkVersion=4.1.0.42
    #${filepath}  set variable  param_file
    #${param}     Person.Get_param     ${filepath}
    #log     ${param}
    Person.Senddata   ${url}    ${param}
    Person.Check_request_code
    @{response_body}  Person.Get_response_body
    should be equal    @{response_body}     ${body}
    Person.Check_response_code
    ${message}  Person.Check_response_message
    should be equal  ${message}     Operation successfully.
    ${icon}    Person.Get_icon
    should be equal     ${icon}     https://dn-pingan-anydoor-001.qbox.me/MAAM_YAOYIYAOIMG_100179

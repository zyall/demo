*** Settings ***
Library                 Selenium2Library

*** Test Cases ***
test case 1
          open browser          http://www.baidu.com          chrome
          input text          id=kw          robot framework学习
          click button          id=su

test case 2
          ${a}          Set variable          hello world
          log          ${a}

test case 3
          ${a}          get time          hello world
          sleep          2
          log          ${a}

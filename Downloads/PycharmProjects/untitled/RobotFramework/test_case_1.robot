*** Settings ***
Library                 Selenium2Library

*** Test Cases ***
test case 1
          ${a}          Set variable          hello world
          ${hi}          Catenate          hello          world
          log          ${a}
          log          ${hi}

test case 2
          ${list1}          Create List          a          b          c          #定义列表
          log          ${list1}
          @{list}          Create List          1          2
          log many          @{list}

test case 3
          ${a}          get time          hello world
          sleep          2
          log          ${a}

test case 4
          ${a}          Set variable          95
          run keyword if          ${a}>=90          log          优秀
          ...          ELSE IF          ${a}>=80          log          良好
          ...          ELSE IF          ${a}>=60          log          及格
          ...          ELSE          log          不及格

test case 5
          @{list}          Create List          a          b          c
          :FOR          ${i}          in range           4
          \          log          ${i}
          :FOR          ${i}          in          @{list}
          \          log          ${i}

test case 6
          open browser          http://www.baidu.com          chrome
          input text          id=kw          robot framework学习
          click button          id=su
          close browser

*** Settings ***
Library       Selenium2Library
suite setup
suite teardown

*** Variables ***
@{list}       name      address     phone
&{dict}       name=Matti    address=xxx         phone=123
*** Test Cases ***
 1:定义变量
       ${a}     Set variable    hello world           #定义变量
       ${hi}   Catenate       hello      world   #连接对象
       log          ${a}
       log          ${hi}
test case 2:Get time
       ${a}      Get time       hello world
       log       ${a}
test case 3 :列表
    log        ${list}
    log many   @{list}
    log many   @{list}[0]

test case 4：字典1
    log        ${dict}
    log many   &{dict}
test case 5：字典2
    &{dict}    create dictionary    a=1
     log        ${dict}

test case 6：if语句
     ${a}    Set variable     34
     run keyword if     ${a}>=90    log    优秀
     ...     else if   ${a}>=80    log    良好
     ...     ELSE IF    ${a}>=60    log    及格
     ...     ELSE       log        不及格
test case 7：循环
    :FOR   ${i}  in    @{list}
    \     log   ${i}
test case 8：中断循环
    :FOR   ${i}  in range    10
    \     run keyword if     ${i}==4      Exit For Loop
    \     log     ${i}
    log   outside loop
test case 8:Evaluate                              #通过它可以使用 Python 语言中所提供的方法
    ${d}      Evaluate          random.randint(10,99)          random
    log       ${d}

test case 9：selenium UI自动化
    open browser  http://www.baidu.com  Chrome
    input text      id=kw    robot framework学习
    click button   id=su
    #close browser


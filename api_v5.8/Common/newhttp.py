#usr/bin/python
# encoding:utf-8
import json
import requests
from Common.readexcel import ExcelUtil
from Common.writeexcel import copy_excel,WriteExcel
from conf import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def send_requests(se,testdata):
    '''封装requests请求'''
    method = testdata["method"]
    url = baseurl + testdata["url"]
    # url后面的params参数
    try:
        # str转换dict
        params = eval(testdata["params"])
    except:
        params = None

    # 请求头部headers
    try:
        headers = eval(testdata["headers"])
    except:
        headers = None

    # post请求body类型
    type = testdata["type"]

    test_nub = testdata['id']
    logger.info("*******正在执行用例：-----  %s  ----**********" % test_nub)
    logger.info("请求方式：%s, 请求url:%s" % (method, url))
    logger.info("请求params：%s" % params)

    # post请求body内容
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}

    # 判断传data数据还是json
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata
    if method == "post":
        logger.info("post请求body类型为：%s,body内容为：%s" % (type, body))

    verify = False
    # 接收返回数据
    res = {}

    try:
        r = se.request(method=method,url=url,params=params,headers=headers,data=body,verify=verify)
        logger.info("页面返回信息：%s" % r.content.decode("utf-8"))
        res['id'] = testdata['id']
        res['rowNum'] = testdata['rowNum']
        res["statuscode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.content.decode("utf-8")
        res["times"] = str(r.elapsed.total_seconds())  # 接口请求时间转str
        if res["statuscode"] != "200":
            res["error"] = res["text"]
            logger.info(res["error"])
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
        else:
            res["result"] = "fail"
        logger.info("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
        return res
    except Exception as msg:
        res["msg"] = str(msg)
        return res



def wirte_result(result, filename):
    # 返回结果的行数row_nub
    row_nub = result['rowNum']
    # 写入statuscode
    wt = WriteExcel(filename)
    wt.write(row_nub, 8, result['statuscode'])  # 写入返回状态码statuscode,第8列
    wt.write(row_nub, 9, result['times'])  # 耗时
    wt.write(row_nub, 10, result['error'])  # 状态码非200时的返回信息
    wt.write(row_nub, 12, result['result'])  # 测试结果 pass 还是fail
    wt.write(row_nub, 13, result['msg'])  # 抛异常


if __name__ == "__main__":
    Excelpath1 = xlsPath + '/test.xlsx'
    Excelpath2 = xlsPath + '/testreport.xlsx'
    testdata = ExcelUtil(Excelpath1,0).dict_data()
    se = requests.session()
    res = send_requests(se, testdata[0])
    copy_excel(Excelpath1,Excelpath2)
    wirte_result(res,Excelpath2)






#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import readConfig as conf
from Common.Log import MyLog as Log

localReadConfig = conf.ReadConfig()
log = Log.get_log().logger
class ConfigHttp():
    def __init__(self):
        global host,timeout,headers,session
        host = localReadConfig.get_http('baseurl')
        timeout = localReadConfig.get_http('timeout')
        headers = localReadConfig.get_http('headers')
        session =requests.session()
        self.param = {}
        self.data = {}
        self.url = {}
        self.files = {}

    def set_url(self, url):
        self.url = host + url
        return self.url

    def set_params(self, params):
        self.params = params
        return self.params

    def set_data(self, data):
        self.data = data
        return self.data

    def set_files(self,files):
        self.files =files
        return self.files

    # defined http get method
    def get(self):
        try:
            response = session.get(self.url,params=self.params,headers=eval(headers),timeout=float(timeout))
            log.info("Send GET Http Successfully!")
            return response
        except Exception:
            log.error("Http Time Out")
    def post(self):
        try:
            response = session.post(self.url,data=self.data,headers=eval(headers),timeout=float(timeout))
            log.info("Send POST Http Successfully!")
            return response
        except Exception:
            log.error("Http Time Out")


if __name__=="__main__":
    A = ConfigHttp()
    A.get()
#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from conf import *

class ConfigHttp():
    def __init__(self):
        global session
        session =requests.session()
        self.param = {}
        self.data = {}
        self.url = {}
        self.files = {}

    def set_url(self, url):
        self.url = baseurl + url
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
            response = session.get(self.url,params=self.params,headers=headers,timeout=float(timeout))
            logger.info("Send GET Http Successfully!")
            return response
        except Exception:
            logger.error("Http Time Out")
    def post(self):
        try:
            response = session.post(self.url,data=self.data,headers=headers,timeout=float(timeout))
            logger.info("Send POST Http Successfully!")
            return response
        except Exception:
            logger.error("Http Time Out")


if __name__=="__main__":
    A = ConfigHttp()
    A.get()
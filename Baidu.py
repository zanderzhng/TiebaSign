# -*- coding: utf-8 -*-
import requests
import re
import json


def load_cookies(path):
    '''
    加载浏览器的Cookie
    '''
    with open(path, 'r') as f:
        data = json.load(f)
    cookies = dict()
    for item in data:
        cookies[item["name"]] = item["value"]
    return cookies


class Baidu():
    def __init__(self, cookies):
        self.base_url = "https://www.baidu.com"
        self.session = requests.session()
        self.session.cookies.update(cookies)
        self.session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
        self.username = self.get_username() or self.get_username() or self.get_username()
        print("Login:", self.username)

    def check_login(self):
        res = self.session.get(self.base_url)
        if re.search("'login':'1'", res.text):
            return True
        return False

    def get_username(self):
        res = self.session.get(self.base_url)
        match = re.search("=user-name>(.+?)<", res.text)
        if match:
            return match.group(1)
        else:
            print("Fail to get username!")
            return None

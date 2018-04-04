# -*- coding: utf-8 -*-

__author__ = 'arcosx'

import requests


class client(object):
    username = ""
    password = ""
    login_url = "https://ucapp.nuaa.edu.cn/wap/login/invalid"
    search_url = "https://app.nuaa.edu.cn/cardhis/wap/default/index"
    cookie = ""
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://app.nuaa.edu.cn/cardhis/wap/default/index',
    }

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        post_data = {'username': self.username, 'password': self.password}
        login_res = requests.post(self.login_url, data=post_data, headers=self.headers)
        cookies = login_res.cookies
        UUkey = 'UUkey=' + cookies['UUkey'] + '; '
        vjuid = 'vjuid=' + cookies['vjuid'] + '; '
        vjvd = 'vjvd=' + cookies['vjvd'] + '; '
        vt = 'vt=' + cookies['vt']
        header_cookie = UUkey + vjuid + vjvd + vt
        self.headers['Cookie'] = header_cookie
        return 1

    def search(self, begin_data, end_data):
        if self.login() == 0:
            return
        payload = "sdate=" + begin_data + "&edate=" + end_data
        res = requests.post(self.search_url, headers=self.headers, data=payload)
        return res.json()


if __name__ == '__main__':
    test = client(username='', password='')
    print(test.search(begin_data='2015-06-06', end_data='2018-04-03'))

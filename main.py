# -*- coding: utf-8 -*-
import requests
import sys


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
        'Cookie': ''
    }

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        post_data = {'username': self.username, 'password': self.password}
        login_res = requests.post(self.login_url, data=post_data)
        if login_res.json()['e'] == '10011':
            print(login_res.json()['m'])
            return 0

        cookies = login_res.cookies
        UUkey = 'UUkey=' + cookies['UUkey'] + '; '
        vjuid = 'vjuid=' + cookies['vjuid'] + '; '
        # vjvd = 'vjvd=' + cookies['vjvd'] + '; '
        vt = 'vt=' + cookies['vt']
        header_cookie = UUkey + vjuid + 'vjvd=03a083d8839b3be4c35122faf82a165c; ' + vt
        self.headers['Cookie'] = header_cookie
        return 1

    def search(self, begin_data, end_data):
        if self.login() == 0:
            return
        payload = "sdate=" + begin_data + "&edate=" + end_data
        res = requests.post(self.search_url, headers=self.headers, data=payload)
        print(res.json())


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    begin_data = sys.argv[3]
    end_data = sys.argv[4]
    test = client(username=username, password=password)
    test.search(begin_data=begin_data, end_data=end_data)

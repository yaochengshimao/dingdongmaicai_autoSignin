# @Time : 2023/6/2 15:21
# @Author : yaochengshimao
# @File : dingdongmaicai_autoSignin.py
# @Software: PyCharm
import requests


def sso_login(domain, username, password, CAPTCHA):
    data = {
        "username": username,
        "passowrd": password,
        "CAPTCHA": CAPTCHA
    }
    url = domain + "/api/v2/login"
    rep = requests.post(url, data=data)
    return rep.cookies


def signin(userid, cookie, domain):
    """
    上班自动签到
    :param userid: 员工工号
    :param cookie:sso_login返回的cookie
    :param domain: sso域名
    """
    url = domain + "/api/v2/user/attendance/signin"
    headers = {
        "cookie": cookie,
    }
    data = {
        "userId": userid,
    }
    rep = requests.post(url, data=data, headers=headers)
    if rep.json()['result']['flag'] == 1:
        print("siginin user:{id} success".format(id))
    else:
        print(rep)


if __name__ == "__main__":
    # 脚本设置定时任务，每天早上9.29自动打卡签到
    domain = "http://ssov2.ddxq.mobi/"

    userid = "C082631"
    username = "yaochengshimao@100.me"
    password = "!qaz@wsx#edc"
    CAPTCHA = "111222"

    cookie = sso_login(domain, password, username, CAPTCHA)
    signin(userid, cookie, domain)


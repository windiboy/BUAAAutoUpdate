import requests
import re
import time

###########用户需要更改的部分###############
your_name = '统一认证账号'
your_pwd = '统一认证密码'
wechat_key = '填入你的Server酱key'
form_data = '复制的form_data'
###########用户需要更改的部分###############

def wechat_post(text):
    url = 'https://sc.ftqq.com/' + wechat_key + '.send?text='+text+time.strftime("%m-%d", time.localtime())
    requests.get(url)
    
def buaaLogin(user_name, password):
    print("统一认证登录")

    postUrl = "https://app.buaa.edu.cn/uc/wap/login/check"
    postData = {
        "username": user_name,
        "password": password,
    }
    responseRes = requests.post(postUrl, data=postData)
    print(f"text = {responseRes.text}")
    return responseRes


def fillForm(res):
    s = requests.session()
    day = time.strftime("%Y%m%d", time.localtime())
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://app.buaa.edu.cn/ncov/wap/default/index',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': res.headers['set-cookie']
    }
    data = re.sub(r'date=\d{8}', 'data=' + day, form_data)
    r = s.post('https://app.buaa.edu.cn/ncov/wap/default/save', data=data, headers=headers)
    return r


def main_handler(event, context):
    result = fillForm(buaaLogin(your_name, your_pwd))
    wechat_post(result.text)
    return("DONE")

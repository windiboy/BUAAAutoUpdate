import requests
import re
import time

###########用户需要更改的部分###############
your_name = ''
your_pwd = ''
wechat_key = ''
bark_url = '' #可选 如果是iOS用户，可下载Bark APP，填入Bark中提供的url即可收到打卡结果的推送
form_data = ''

###########用户需要更改的部分###############

def wechat_post(text):
    url = 'https://sc.ftqq.com/' + wechat_key + '.send?text='+text+time.strftime("%m-%d", time.localtime())
    requests.get(url)


def bark_post(text):
    if bark_url != '':
        url = bark_url + text
        requests.get(url)


def buaaLogin(user_name, password):
    print("统一认证登录")

    postUrl = "https://app.buaa.edu.cn/uc/wap/login/check"
    postData = {
        "username": user_name,
        "password": password,
    }
    responseRes = requests.post(postUrl, data=postData)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    # print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    return responseRes


def fillForm(res):
    s = requests.session()
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://app.buaa.edu.cn/site/buaaStudentNcov/index',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': res.headers['set-cookie']
    }
    r = s.post('https://app.buaa.edu.cn/buaaxsncov/wap/default/save', data=form_data, headers=headers)
    return r


def main_handler(event, context):
    result = fillForm(buaaLogin(your_name, your_pwd))
    wechat_post(result.text)
    bark_post(result.text)
    return("DONE")
    

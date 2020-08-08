from selenium import webdriver
from selenium.webdriver import ActionChains
import time

wechat_key = '你的Server酱key'


def wechat_post(text):
    url = 'https://sc.ftqq.com/' + wechat_key + '.send?text='+text+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    browser.get(url)


if __name__ == '__main__':
    #这里改成你的统一认证用户名和密码
    user_name = 'user'
    pwd = 'password'

    # 加上这两句话不打开浏览器
    option = webdriver.ChromeOptions()
    #option.add_argument('headless') # 设置option
    # 用浏览器打开打卡的网址
    browser = webdriver.Chrome(options=option)
    browser.get("https://app.buaa.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.buaa.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex")

    # 输用户名和密码
    user_name_input = browser.find_element_by_css_selector('#app > div.content > div:nth-child(1) > input[type=text]')
    user_name_input.send_keys(user_name)
    user_pwd_input = browser.find_element_by_css_selector('#app > div.content > div:nth-child(2) > input[type=password]')
    user_pwd_input.send_keys(pwd)

    # 然后点击登录按钮
    login_button = browser.find_element_by_css_selector('#app > div.btn')
    ActionChains(browser).move_to_element(login_button).click(login_button).perform()
    print('点击登陆')

    # 跳转并点击获取位置按钮
    # 这样写是为了等待跳转页面加载出来
    while True:
        try:
            location_button = browser.find_element_by_css_selector('body > div.item-buydate.form-detail2 > div > div > section > div.form > ul > li:nth-child(7) > div > input[type=text]')
            break
        except:
            time.sleep(5)
            browser.get("https://app.buaa.edu.cn/ncov/wap/default/index")

    ActionChains(browser).move_to_element(location_button).click(location_button).perform()
    print('获取位置')
    
    
    # 选择温度
    temperature_button = browser.find_element_by_css_selector('body > div.item-buydate.form-detail2 > div > div > section > div.form > ul > li:nth-child(9) > div > div > div:nth-child(2)')
    ActionChains(browser).move_to_element(temperature_button).click(temperature_button).perform()
    print('选择温度')

    # 点击提交
    submit_button = browser.find_element_by_css_selector('body > div.item-buydate.form-detail2 > div > div > section > div.list-box > div > a')
    ActionChains(browser).move_to_element(submit_button).click(submit_button).perform()
    print('点击提交')

    time.sleep(1)
    # 确定
    while True:
        try:
            confirm_button = browser.find_element_by_css_selector('#wapcf > div > div.wapcf-btn-box > div.wapcf-btn.wapcf-btn-ok')
            print('提交成功')
            break
        except:
            try:
                confirm_button = browser.find_element_by_css_selector('#wapat > div > div.wapat-btn-box > div')
                print('今天已提交过')
                break
            except:
                time.sleep(0.5)
    ActionChains(browser).move_to_element(confirm_button).click(confirm_button).perform()
    wechat_post('提交成功')

    time.sleep(1)
    browser.quit()

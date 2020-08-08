# BUAAAutoUpdate
北京航空航天大学自动填写”疫情防控通“的每日上报信息。
![Telegram](https://github.com/windiboy/BUAAAutoUpdate/blob/master/picture/logo.png)
## 使用前提

- 该脚本的工作方式为：通过ChromeDrive模拟打开填报页面，模拟鼠标点击**位置、选择温度**并提交
- 分为校外版本**out_school.py**和校内版本**in_school.py**
- **本脚本参考了这位[同学](https://github.com/buaalzm/fuckdaka)，仅为学习开发使用，请勿瞒报谎报疫情信息，否则后果自负**

## 脚本依赖

- Python 3.6 或以上
- selenium库（以及对应浏览器的驱动程序）

**注：** 如果您需要让该脚本定期自动运行：

1. Linux/macOS 用户可以配置 cron 等工具。参考教程：
   1. https://www.ibm.com/developerworks/cn/education/aix/au-usingcron/index.html
   2. https://crontab.guru/
2. Windows 用户可以使用系统的「任务计划」功能。参考教程：
   1. https://www.cnblogs.com/jjliu/p/11505720.html
   
## windows 10环境配置
- 建议使用Anaconda进行环境配置
1. [下载并安装Anaconda](https://www.anaconda.com/products/individual)，需要记住安装位置。
2. 创建虚拟环境并激活，安装selenium库
```bash
conda create -n web python=3.6 
conda activate web
conda install selenium
```
3. [安装ChromeDrive](https://chromedriver.chromium.org/downloads)，注意版本对应：如果您使用的是Chrome版本85，请下载ChromeDriver 85.0.4183.38
- 需要将解压出来的chromedriver.exe分别放到**chrome浏览器的根目录和Anaconda对应虚拟环境的根目录**
- 例如C:\Program Files (x86)\Google\Chrome\Application  D:\Anaconda\envs\web
   
## 将运行结果推送到微信上

本脚本支持使用「[Server 酱](https://sc.ftqq.com/3.version)」将运行结果通过微信推送到手机上。

您只需要根据[官网上的介绍](https://sc.ftqq.com/3.version)，在「Server 酱」官网登录并绑定微信后，将网站提供的 SCKEY 作为参数传入脚本文件即可：

```bash
wechat_key = 'your key'
```

## 运行示例

假设您北航统一认证的账户和密码是：

- **用户名：** user
- **密码：** password

修改您所需要用的脚本文件，例如out_school.py
```bash
user_name = 'user'
pwd = 'password'
```
运行即可

## 版权

使用 MIT 协议发布，著作权由代码的贡献者所有。

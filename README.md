# BUAAAutoUpdate
北航打卡。
北京航空航天大学自动填写”疫情防控通“的每日上报信息。
![Telegram](https://github.com/windiboy/BUAAAutoUpdate/blob/master/picture/logo.png)

# 2020.09.23更新新功能——累计每日晚检未打卡名单
![Telegram](https://github.com/windiboy/BUAAAutoUpdate/blob/master/picture/daka.jpg)
## 新增功能
- 可以统计到目前为止未打卡名单
- 使用pyplot做图
- 推送到邮箱
- **需要统一认证账号有查看未打卡名单的权限**
## 操作步骤
### 脚本依赖
- Python 3.6 或以上
- requests
- openpyxl
- matplotlib.pyplot
### 修改py脚本中的个人信息
```bash
your_name = '统一认证账号'
your_pwd = '统一认证密码'
dir_name = 'C:\\Users\\xxx\\xxx\\xxx\\' #存放数据文件的地址 注意要使用绝对路径
file_name = dir_name+time.strftime("%m-%d", time.localtime())
dataBase_name = 'dateBase.xlsx'

msg_from = 'xxx@qq.com'  # 发送方邮箱
passwd = 'xxxxx'  # 填入发送方邮箱的授权码
msg_to = 'xxxx@qq.com'  # 收件人邮箱
```
### 设计定时启动或手动运行
- 运行后邮箱即可收到图片
- dataBase.xlsx即为数据库文件

# 2020.08.14更新2.0版本
## 新增功能
- 新增了out_school2.0.py和in_school2.0.py
- 舍弃了selenium，改用更方便的request库
- 可以通过腾讯云函数实现代码托管，参考了这位[同学](https://github.com/kngkngtian/AutoReport)
- 当然也可以只在本地运行，自动运行参考1.0说明文档

## 实现原理
- 获取每次提交时的源代码并记录，之后每天按照记录的源代码重复提交

## 操作步骤
### 获取需要提交的信息
- 使用chrome浏览器，打开并登录[疫情防控通校外](https://app.buaa.edu.cn/ncov/wap/default/index)/[疫情防控通校内](https://app.buaa.edu.cn/site/ncov/xisudailyup)
- 如果无法获取定位，可以参考[Chrome 自定位置](https://blog.csdn.net/u010844189/article/details/81163438)。
- 校外同学：在页面中填好全部信息之后，打开`F12`控制台，输入`vm.save()`，然后查看`network`标签中的`save`项。点击后查看`Headers`标签，点击`Form Data`右侧的`view source`，复制备用。
- 校内同学：在页面中填好全部信息之后，点击提交，然后查看`network`标签中的`save`项。点击后查看`Headers`标签，点击`Form Data`右侧的`view source`，复制备用。

### 修改py脚本中的个人信息
将个人账号密码、Server酱key和上面获取到的form_data替换掉对应的内容
```bash
your_name = '统一认证账号'
your_pwd = '统一认证密码'
wechat_key = '填入你的Server酱key'
form_data = '复制的form_data'
```

### 新建云函数
这里以腾讯云为例，进入[腾讯云函数页面](https://console.cloud.tencent.com/scf)，点击侧栏的`函数服务`，新建一个函数。
函数名称随意，运行环境选择`python3.6`，创建方式选择`空白函数`即可，点击完成。
选择`函数代码`标签，将修改完的python脚本代码替换掉原来的hello world代码，选择`保存并测试`。测试绿色表明成功同时会收到微信推送提示，失败的话请检查相关字符串是否正确。
### 设置触发器
选择左侧`触发管理`，创建一个新的触发器。选择`定时触发`，出发周期自定义，自己根据想要自动提交的时间输入Cron数据即可。推荐使用`0 1 0,8 * * * *`即可，该触发时间为每天的0:01和8:01，防止因为系统或某方面原因而失败。

### Enjoy

# 以下是1.0版本的内容
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

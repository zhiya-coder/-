import time
# 调用selenium库，访问翱翔门户体温填报链接
from selenium import webdriver  # 从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options  # 从options模块中调用 Options类
import schedule  # 引入schedule,定时执行

def yqtb_nwpu():
    chrome_options = Options()
    #默模式运行该脚本，即不弹出chrome窗口
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://yqtb.nwpu.edu.cn/wx/xg/yz-mobile/index.jsp')#转到翱翔门户登陆页面
    time.sleep(1)

    username=driver.find_element_by_id('username')
    username.clear()
    username.send_keys('2020262803')#抓取用户名栏并输入学号
    password=driver.find_element_by_id('password')
    password.clear()
    password.send_keys('wudongming152754')#抓取密码栏并输入密码
    driver.find_element_by_name('submit').click()#抓取登录按钮并点击
    time.sleep(1)
    driver.find_element_by_class_name('icon-shangbao1').click()
    time.sleep(1)
    driver.find_element_by_class_name('weui-btn_primary').click()#抓取提交按钮#提交
    sub=driver.find_element_by_id('brcn')
    driver.execute_script("arguments[0].click();", sub)
    driver.find_element_by_id('save_div').click()
    driver.close() #关闭浏览器
schedule.every().day.at("10:30").do(yqtb_nwpu) #部署在每天的10:30执行job()函数的任务

while True:
    schedule.run_pending()
    time.sleep(5)


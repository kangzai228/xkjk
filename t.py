import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://servicewechat.com/wx07a350fde1321fa4/14/page-frame.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
    'xweb_xhr': '1',
}

data = {
    'method': 'login',
    'userName': 'J36073100720230272',
    'password': 'becfec11418289ba36cd03ed0ef586e4',
    'userType': '2',
    'sourceType': 'iOS',
    'iosPassWord': '230272',
    'openId': 'oyHFEw3Fflw1IQ2QiuKGzMpsxTGY',
}

response = requests.post('https://www.ruijiaoyu.net/LoginManagerForApp', headers=headers, data=data)
print(response.json())
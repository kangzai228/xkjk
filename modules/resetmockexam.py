# 重新模拟
import requests

def resetmockexam(Token,StudentSessionId):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'Bearer '+Token,
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://xkjk.jxeea.cn:8000',
        'Pragma': 'no-cache',
        'Referer': 'https://xkjk.jxeea.cn:8000/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
        'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'StudentSessionId': StudentSessionId,
    }

    response = requests.post('https://xkjk.jxeea.cn:8000/EOAPI/studentexam/resetmockexam', headers=headers, json=json_data)
    # print(response.json()["ResultType"])
    return response.json()["ResultType"]

"""
{"ResultType":1,"Message":null,"Entity":true}
"""
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJFeGFtLkVPIiwiYXVkIjoiYXBpIiwic3ViIjoiOTNlMjE3MDE1NjcwYWU0MWJjZjY0NWZiM2IzN2Y5MmUiLCJ1a2luZCI6IjEwMDAiLCJuYmYiOjE2OTgyMDY3OTcsImV4cCI6MTY5ODI5MzE5NywiaWF0IjoxNjk4MjA2Nzk3fQ.-Og1sL-FFu9PQDPpQtgBinFicwPcSETw_0SlQwbpnX4',
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
    'Id': 114963,
}

response = requests.post('https://xkjk.jxeea.cn:8000/EOAPI/studentexam/getquestiondetail', headers=headers, json=json_data)
return response.json()['Entity']['OptionGroups']


"""
{
    "ResultType": 1,
    "Message": null,
    "Entity": {
        "QuestionID": 114509,
        "QuestionDisplayTypeId": 1,
        "QuestionContent": "<p>小明使用智能手机说出想要拨打电话人的姓名，手机马上识别出相应的手机号并进行拨号，这其中主要应用了人工智能中的(&nbsp;&nbsp;&nbsp; )</p>",
        "OptionGroups": [
            {
                "QuestionOptionGroupID": 79276172,
                "QuestionID": 114509,
                "Order": 1,
                "QuestionText": null,
                "DisplayTypeID": 0,
                "Options": [
                    {
                        "QuestionOptionGroupID": 79276172,
                        "QuestionID": 114509,
                        "QuestionOptionID": "A",
                        "QuestionOptionText": "<p>语音识别技术</p>",
                        "Order": 1
                    },
                    {
                        "QuestionOptionGroupID": 79276172,
                        "QuestionID": 114509,
                        "QuestionOptionID": "B",
                        "QuestionOptionText": "<p>指纹识别技术</p>",
                        "Order": 2
                    },
                    {
                        "QuestionOptionGroupID": 79276172,
                        "QuestionID": 114509,
                        "QuestionOptionID": "C",
                        "QuestionOptionText": "<p>字符识别技术</p>",
                        "Order": 3
                    },
                    {
                        "QuestionOptionGroupID": 79276172,
                        "QuestionID": 114509,
                        "QuestionOptionID": "D",
                        "QuestionOptionText": "<p>图像识别技术</p>",
                        "Order": 4
                    }
                ]
            }
        ]
    }
}
"""
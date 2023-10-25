import requests

def getstudentexaminfo(Token,StudentNo):
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
        'ExamID': 1,
        'StudentNo': StudentNo,
        'SeatNo': 0,
        'ExamSubjectID': 2,
        'Mac': '',
    }

    response = requests.post('https://xkjk.jxeea.cn:8000/EOAPI/studentlogin/getstudentexaminfo', headers=headers, json=json_data)
    return response.json()['Entity']['StudentInfo'],response.json()['Entity']['StudentSessionsID']


"""
{
    "ResultType": 1,
    "Message": null,
    "Entity": {
        "Offline": false,
        "StudentInfo": {
            "StudentNo": "22073100514120001",
            "StudentName": "郭湘",
            "IDNo": "360731200610077621",
            "HeadImage": "https://xkjk.jxeea.cn:9000/testeopublic/4c3949aa31894b328dcf701786099f19.jpg",
            "SchoolName": "于都县梓山中学",
            "ExamSiteId": 313
        },
        "LoginCount": 1,
        "LoginTime": "2023-10-25 12:10:43",
        "StudentSessionsID": "1717029463688749084",
        "RemainingTime": 0,
        "MonitorUrl": "https://xkjk.jxeea.cn:9000/testeopublic/studentsession/notice/4597/1717029463688749084.txt",
        "MonitorInterval": 5
    }
}
"""
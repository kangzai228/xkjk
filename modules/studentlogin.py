import requests,logging


def studentlogin(StudentNo):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Origin': 'https://xkjk.jxeea.cn:8000',
    'Referer': 'https://xkjk.jxeea.cn:8000/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
    json_data = {
        'ExamID': 1,
        'StudentNo': StudentNo,
        'Password': '123456',
        'LoginType': 0,
    }

    response = requests.post('https://xkjk.jxeea.cn:8000/EOAPI/studentlogin/studentlogin', headers=headers, json=json_data)
    # print(StudentNo,response.json()['Entity'])
    # logging.info(response.json()['Entity']['Token'])
    return response.json()['Entity']['Token'],response.json()['Entity']['ExamSubjectInfos']



if __name__=="__main__":
    StudentNo='22073100514120001'
    res=studentlogin(StudentNo)


"""
{
    "ResultType": 1,
    "Message": null,
    "Entity": {
        "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJFeGFtLkVPIiwiYXVkIjoiYXBpIiwic3ViIjoiOTNlMjE3MDE1NjcwYWU0MWJjZjY0NWZiM2IzN2Y5MmUiLCJ1a2luZCI6IjEwMDAiLCJuYmYiOjE2OTgyMDY3OTcsImV4cCI6MTY5ODI5MzE5NywiaWF0IjoxNjk4MjA2Nzk3fQ.-Og1sL-FFu9PQDPpQtgBinFicwPcSETw_0SlQwbpnX4",
        "ExamSubjectInfos": [
            {
                "ExamSubjectID": 1,
                "ExamSubjectName": "通用技术",
                "SubjectExamState": 1,
                "ErrMsg": null
            },
            {
                "ExamSubjectID": 2,
                "ExamSubjectName": "信息技术",
                "SubjectExamState": 1,
                "ErrMsg": null
            }
        ]
    }
}
"""
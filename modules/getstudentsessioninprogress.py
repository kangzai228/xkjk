import requests

def getstudentsessioninprogress(Token,StudentSessionId):
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
        'SubjectId': 2,
    }

    response = requests.post(
        'https://xkjk.jxeea.cn:8000/EOAPI/studentexam/getstudentsessioninprogress',
        headers=headers,
        json=json_data,
    )
    return response.json()['Entity']['QuestionAnswers']


"""
{
    "ResultType": 1,
    "Message": null,
    "Entity": {
        "StudentSessionsID": "1717029463688749084",
        "TotalScore": 100.0,
        "StudentScore": 0.0,
        "ExamInfo": {
            "StudentSessionsID": "1717029463688749084",
            "ExamBeginTime": "2023-10-17 10:30:00",
            "ExamEndTime": "2023-10-17 12:00:00",
            "StudentBeginTime": "2023-10-25 12:11:26",
            "ExamPaperID": 11,
            "StudentDoingQuestionMode": 1,
            "ExamDuration": 45,
            "InjuryTime": 0,
            "DoingQuestionTime": 2699,
            "ExamState": 3
        },
        "QuestionAnswers": [
            {
                "QuestionID": 125231,
                "Sort": 1,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276209,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 114963,
                "Sort": 2,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276174,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 123364,
                "Sort": 3,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276203,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 114509,
                "Sort": 4,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276172,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 123179,
                "Sort": 5,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276200,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 124712,
                "Sort": 6,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276207,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 114974,
                "Sort": 7,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276175,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 116658,
                "Sort": 8,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276230,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 118205,
                "Sort": 9,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276182,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 116258,
                "Sort": 10,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276216,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 120998,
                "Sort": 11,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276195,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 124526,
                "Sort": 12,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276206,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 115557,
                "Sort": 13,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276177,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 114989,
                "Sort": 14,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276215,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 117965,
                "Sort": 15,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276181,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 115797,
                "Sort": 16,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276178,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 114947,
                "Sort": 17,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276173,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 119688,
                "Sort": 18,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276186,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 120640,
                "Sort": 19,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276223,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 125271,
                "Sort": 20,
                "BaseScore": 2.0,
                "Score": 0.0,
                "QuestionCategoryId": 26,
                "QuestionCategoryName": "单选题",
                "QuestionTypeSort": 1,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276210,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 119903,
                "Sort": 21,
                "BaseScore": 3.0,
                "Score": 0.0,
                "QuestionCategoryId": 27,
                "QuestionCategoryName": "多选题",
                "QuestionTypeSort": 2,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276238,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 116399,
                "Sort": 22,
                "BaseScore": 3.0,
                "Score": 0.0,
                "QuestionCategoryId": 27,
                "QuestionCategoryName": "多选题",
                "QuestionTypeSort": 2,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276244,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 115251,
                "Sort": 23,
                "BaseScore": 3.0,
                "Score": 0.0,
                "QuestionCategoryId": 27,
                "QuestionCategoryName": "多选题",
                "QuestionTypeSort": 2,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276233,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 116444,
                "Sort": 24,
                "BaseScore": 3.0,
                "Score": 0.0,
                "QuestionCategoryId": 27,
                "QuestionCategoryName": "多选题",
                "QuestionTypeSort": 2,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276246,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 124591,
                "Sort": 25,
                "BaseScore": 3.0,
                "Score": 0.0,
                "QuestionCategoryId": 27,
                "QuestionCategoryName": "多选题",
                "QuestionTypeSort": 2,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276242,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 117052,
                "Sort": 26,
                "BaseScore": 3.0,
                "Score": 0.0,
                "QuestionCategoryId": 28,
                "QuestionCategoryName": "填空题",
                "QuestionTypeSort": 3,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276247,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 121615,
                "Sort": 27,
                "BaseScore": 3.0,
                "Score": 0.0,
                "QuestionCategoryId": 28,
                "QuestionCategoryName": "填空题",
                "QuestionTypeSort": 3,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276257,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 117662,
                "Sort": 28,
                "BaseScore": 3.0,
                "Score": 0.0,
                "QuestionCategoryId": 28,
                "QuestionCategoryName": "填空题",
                "QuestionTypeSort": 3,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276249,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 118933,
                "Sort": 29,
                "BaseScore": 3.0,
                "Score": 0.0,
                "QuestionCategoryId": 28,
                "QuestionCategoryName": "填空题",
                "QuestionTypeSort": 3,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276252,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 121780,
                "Sort": 30,
                "BaseScore": 3.0,
                "Score": 0.0,
                "QuestionCategoryId": 28,
                "QuestionCategoryName": "填空题",
                "QuestionTypeSort": 3,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276258,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 124684,
                "Sort": 31,
                "BaseScore": 10.0,
                "Score": 0.0,
                "QuestionCategoryId": 29,
                "QuestionCategoryName": "综合题",
                "QuestionTypeSort": 4,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276285,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    },
                    {
                        "QuestionOptionGroupId": 79276286,
                        "OrderIndex": 2,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    },
                    {
                        "QuestionOptionGroupId": 79276287,
                        "OrderIndex": 3,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    },
                    {
                        "QuestionOptionGroupId": 79276288,
                        "OrderIndex": 4,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 119207,
                "Sort": 32,
                "BaseScore": 10.0,
                "Score": 0.0,
                "QuestionCategoryId": 29,
                "QuestionCategoryName": "综合题",
                "QuestionTypeSort": 4,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276277,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    },
                    {
                        "QuestionOptionGroupId": 79276280,
                        "OrderIndex": 2,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    },
                    {
                        "QuestionOptionGroupId": 79276278,
                        "OrderIndex": 3,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    },
                    {
                        "QuestionOptionGroupId": 79276279,
                        "OrderIndex": 4,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            },
            {
                "QuestionID": 125719,
                "Sort": 33,
                "BaseScore": 10.0,
                "Score": 0.0,
                "QuestionCategoryId": 29,
                "QuestionCategoryName": "综合题",
                "QuestionTypeSort": 4,
                "Duration": 1,
                "SubmitDate": "0001-01-01 00:00:00",
                "Answers": [
                    {
                        "QuestionOptionGroupId": 79276289,
                        "OrderIndex": 1,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    },
                    {
                        "QuestionOptionGroupId": 79276293,
                        "OrderIndex": 2,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    },
                    {
                        "QuestionOptionGroupId": 79276290,
                        "OrderIndex": 3,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    },
                    {
                        "QuestionOptionGroupId": 79276291,
                        "OrderIndex": 4,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    },
                    {
                        "QuestionOptionGroupId": 79276292,
                        "OrderIndex": 5,
                        "Answer": null,
                        "StudentAnswer": null,
                        "BaseGroupScore": 0.0,
                        "GroupScore": 0.0
                    }
                ]
            }
        ]
    }
}
"""
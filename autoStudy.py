from time import sleep
import logging

from modules.studentlogin import studentlogin
from modules.getstudentexaminfo import getstudentexaminfo
from modules.getstudentsessioninprogress import getstudentsessioninprogress
from modules.getquestiondetail import getquestiondetail
from modules.downloadImage import downloadImage

from modules.submitexampaper import submitexampaper

def autoStudy(StudentNo):
    Token,ExamSubjectInfos=studentlogin(StudentNo)
    StudentInfo,StudentSessionsID=getstudentexaminfo(Token,StudentNo)
    QuestionAnswers=getstudentsessioninprogress(Token,StudentSessionsID)
    for QuestionAnswer in QuestionAnswers:
        # str(QuestionAnswers.index(QuestionAnswer+1)),
        print("*"*120)
        QuestionID=QuestionAnswer['QuestionID']
        QuestionContent,OptionGroups=getquestiondetail(Token,QuestionID)
        print(QuestionContent)
        downloadImage(QuestionContent)
        # print(OptionGroups)
        for OptionGroup in OptionGroups:
            Options=OptionGroup['Options']
            for Option in Options:
                QuestionOptionText=Option['QuestionOptionText']
                print(QuestionOptionText)
                downloadImage(QuestionOptionText)

        
        sleep(2)
    QuestionAnswers=submitexampaper(Token,StudentSessionsID)
    print(QuestionAnswers)

if __name__=="__main__":
    logging.basicConfig(level=logging.WARN)
    StudentNo='22073100514120001'
    autoStudy(StudentNo)
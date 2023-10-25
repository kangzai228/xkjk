from time import sleep
import logging

from modules.studentlogin import studentlogin
from modules.getstudentexaminfo import getstudentexaminfo
from modules.getstudentsessioninprogress import getstudentsessioninprogress
from modules.getquestiondetail import getquestiondetail
from modules.submitexampaper import submitexampaper

def autoStudy(StudentNo):
    Token,ExamSubjectInfos=studentlogin(StudentNo)
    StudentInfo,StudentSessionsID=getstudentexaminfo(Token,StudentNo)
    QuestionAnswers=getstudentsessioninprogress(Token,StudentSessionsID)
    for QuestionAnswer in QuestionAnswers:
        # str(QuestionAnswers.index(QuestionAnswer+1)),
        print("*"*80)
        QuestionID=QuestionAnswer['QuestionID']
        QuestionContent,OptionGroups=getquestiondetail(Token,QuestionID)
        print(QuestionContent)
        print(OptionGroups)
        
        sleep(2)
    QuestionAnswers=submitexampaper(Token,StudentSessionsID)
    print(QuestionAnswers)

if __name__=="__main__":
    logging.basicConfig(level=logging.WARN)
    StudentNo='22073100514120001'
    autoStudy(StudentNo)
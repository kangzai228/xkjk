from modules.studentlogin import studentlogin
from modules.getstudentexaminfo import getstudentexaminfo

from modules.submitexampaper import submitexampaper

def autoStudy():
    StudentNo='22073100514120001'
    Token,ExamSubjectInfos,StudentSessionsID=studentlogin(StudentNo)
    getstudentexaminfo(Token,StudentNo)
    getstudentsessioninprogress(Token,StudentSessionId)

    QuestionAnswers=submitexampaper(Token,StudentSessionsID)
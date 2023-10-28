from time import sleep
import logging

from modules.studentlogin import studentlogin
from modules.getstudentexaminfo import getstudentexaminfo
from modules.resetmockexam import resetmockexam

from modules.getstudentsessioninprogress import getstudentsessioninprogress
from modules.getquestiondetail import getquestiondetail
from modules.downloadImage import downloadImage

from modules.submitexampaper import submitexampaper
from modules.feiyingSQL import feiyingSQL
from modules.getSHA1 import getSHA1

def autoStudy(StudentNo):
    Token,ExamSubjectInfos=studentlogin(StudentNo)
    SubjectID=1
    StudentInfo,StudentSessionsID=getstudentexaminfo(Token,StudentNo,SubjectID)
    resetmockexam(Token,StudentSessionsID)

    QuestionAnswers=getstudentsessioninprogress(Token,StudentSessionsID)
    for QuestionAnswer in QuestionAnswers:
        print(QuestionAnswers.index(QuestionAnswer)+1,end=' ')
        print("*"*120)
        QuestionID=QuestionAnswer['QuestionID']
        QuestionCategoryId=QuestionAnswer['QuestionCategoryId']

        Question=getquestiondetail(Token,QuestionID)
        QuestionContent=Question['QuestionContent']
        OptionGroups=Question['OptionGroups']
        QuestionOptionGroupID=OptionGroups[0]["QuestionOptionGroupID"]
        sql1="INSERT INTO `Question` (`QuestionID`, `QuestionCategoryId`,`QuestionContent`,`QuestionOptionGroup` ) VALUES ( "+str(QuestionID)+", "+ str(QuestionCategoryId) +",'"+str(QuestionContent)+"',"+ str(QuestionOptionGroupID) +" )"
        # print(sql1)
        feiyingSQL(sql1)
        print(QuestionContent)
        downloadImage(QuestionContent)
        # print(OptionGroups)
        for OptionGroup in OptionGroups:
            Options=OptionGroup['Options']
            for Option in Options:
                QuestionID=Option['QuestionID']
                QuestionOptionID=Option['QuestionOptionID']
                QuestionOptionGroupID=Option['QuestionOptionGroupID']
                QuestionOptionText=Option['QuestionOptionText']
                QuestionOrder=Option['Order']
                sha1=getSHA1(str(QuestionOptionGroupID)+QuestionOptionID)
                print(QuestionOptionID,QuestionOptionText,sha1)
                downloadImage(QuestionOptionText)
                sql2="INSERT INTO `QuestionOption` (`QuestionOptionID`,`sha1`,`QuestionOptionText`,`QuestionOptionGroupID`,`QuestionOrder`) VALUES ('"+QuestionOptionID+"','"+sha1+"','"+ QuestionOptionText+"',"+ str(QuestionOptionGroupID)+","+str(QuestionOrder)+")"
                # print(sql2)
                feiyingSQL(sql2)
                sleep(0.1)
        sleep(0.5)
    QuestionAnswers=submitexampaper(Token,StudentSessionsID)
    print(QuestionAnswers)
    for QuestionAnswer in QuestionAnswers:
        QuestionID=QuestionAnswer['QuestionID']
        a_list=[]
        for m in QuestionAnswer["Answers"]:
            a_list.append(m["Answer"])
        Answers=';;;;;'.join(a_list)
        sql3="UPDATE `Question` SET `Answers` = '"+ Answers +"' WHERE `QuestionID`="+str(QuestionID)+";"
        print(sql3)
        feiyingSQL(sql3)
        sleep(0.2)

if __name__=="__main__":
    logging.basicConfig(level=logging.WARN)
    StudentNo='22073100514120001'
    autoStudy(StudentNo)
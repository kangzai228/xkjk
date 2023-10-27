# coding=utf-8

# 导入pymysql模块
import pymysql


def feiyingSQL(sql,database='xkjk',host='localhost'):
    # 连接database,参数1主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名称
    # host = '81.71.129.133'
    user='kangzai228'
    password='kang1938'
    # database='xkjk'
    port = 3308
    conn = pymysql.connect(host=host, port=port, user=user,
                           password=password, database=database, charset='utf8')
    # 创建一个可以执行SQL语句的光标对象
    cursor = conn.cursor()

    # 执行SQL语句
    if sql.split(" ")[0].upper() =="SELECT":
        try:
            cursor.execute(sql)
            isSuccessed = "1"
            # 打印返回的结果
            return_datas = cursor.fetchall()
        except:
            isSuccessed = "0"
            # 打印返回的结果
            return_datas = "database select error!"
    else:
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            conn.commit()
            isSuccessed = "1"
            return_datas = sql.split(" ")[0].lower()+" database success!"
        except:
            # 发生错误时回滚
            conn.rollback()
            isSuccessed = "0"
            return_datas = sql.split(" ")[0].lower()+" database error!"

    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()
    result = {
        "isSuccessed": isSuccessed,
        "data": return_datas,
    }
    return result


if __name__=="__main__":
    sql="INSERT INTO `QuestionOption` (`QuestionID`,`QuestionOptionID`,`QuestionOptionText`,`QuestionOptionGroupID`,`QuestionOrder`) VALUE (118472,D,<p>压力传感器</p>,79276185,4)"
    print(feiyingSQL(sql))
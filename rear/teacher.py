import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS

# 数据库连接
# 打开数据库连接
db = pymysql.connect(host='localhost', user='root', password='123456', database='students_select_course')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 后端服务启动
app = Flask(__name__)
CORS(app, resource=r'/*')  # 处理跨域资源共享


#  教师信息显示接口
@app.route('/showtehinfo', methods=['POST'])
def show_teacher_info():
    if request.method == "POST":
        # 执行显示数据库的操作
        tno = request.form.get("username")
        sql_show_info = "SELECT * from teacher where tno = %s"
        cursor.execute(sql_show_info, (tno,))
        stu_info = cursor.fetchone()
        if stu_info:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(stu_info)
        else:
            return jsonify({'error': 'No student found with the given sno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


#  课程数目查询接口
@app.route('/coursenum', methods=['POST'])
def show_course_num():
    if request.method == "POST":
        # 执行显示数据库的操作
        sql_show_info = "SELECT * from course"
        cursor.execute(sql_show_info, ())
        stu_info = cursor.fetchall()
        if stu_info:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(stu_info)
        else:
            return jsonify({'error': 'No student found with the given sno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


#  教师提交分数接口
@app.route('/addscore', methods=['POST'])
def add_student_score():
    if request.method == "POST":
        sno = request.form.get("sno")
        courseid = request.form.get("courseid")
        score = request.form.get("score")
        term = request.form.get("term")
        # 执行显示数据库的操作
        sql_add_info = "INSERT INTO study (sno,cno,term,score) VALUES(%s,%s,%s,%s);"
        cursor.execute(sql_add_info, (sno, courseid, term, score))
        # 提交事务
        db.commit()
        # 检查更新行数
        if cursor.rowcount > 0:
            return jsonify({'message': 'successfully'}), 200
        else:
            return jsonify({'error': 'No  found'}), 404
    else:
        return jsonify({'error': 'Invalid request method'}), 405


#  教师修改密码接口
@app.route('/updatacodeteh', methods=['POST'])
def update_code_teacher():
    if request.method == "POST":
        # 获取表单数据
        newcode = request.form.get("newcode")
        tno = request.form.get("username")
        oldpwd = request.form.get("oldpwd")
        if not newcode or not tno:
            return jsonify({'error': 'newcode and username are required'}), 400
        # 更新数据库
        sql_query_score = "UPDATE teacher_account SET tpassword = %s WHERE tusername = %s and tpassword = %s;"
        cursor.execute(sql_query_score, (newcode, tno, oldpwd))
        # 提交事务
        db.commit()
        # 检查更新行数
        if cursor.rowcount > 0:
            return jsonify({'message': 'Password updated successfully'}), 200
        else:
            return jsonify({'error': 'No student found with the given username'}), 404
    else:
        return jsonify({'error': 'Invalid request method'}), 405


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8689)
    db.close()
    print("结束")

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


#  学生信息显示接口
@app.route('/showstuinfo', methods=['POST'])
def show_student_info():
    if request.method == "POST":
        # 执行显示数据库的操作
        sno = request.form.get("username")
        sql_show_info = "SELECT   s.sno,  s.sname,   s.ssex,   s.sage,   c.cname AS class_name FROM   student AS s  JOIN   class AS c ON s.class_id = c.class_id WHERE s.sno = %s"
        cursor.execute(sql_show_info, (sno,))
        stu_info = cursor.fetchone()
        if stu_info:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(stu_info)
        else:
            return jsonify({'error': 'No student found with the given sno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


#  学生成绩查询显示接口
@app.route('/queryscore', methods=['POST'])
def query_student_score():
    if request.method == "POST":
        # 执行显示数据库的操作
        sno = request.form.get("username")
        term = request.form.get("term")
        sql_query_score = "SELECT s.score, c.tname, c.cname, c.cscore  FROM  study AS s INNER JOIN course AS c ON s.cno = c.cno WHERE s.sno = %s  AND s.term = %s"
        cursor.execute(sql_query_score, (sno, term))
        stu_score = cursor.fetchall()
        if stu_score:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(stu_score)
        else:
            return jsonify({'error': 'No student found with the given sno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


#  初始化学生成绩接口
@app.route('/showscore', methods=['POST'])
def show_student_score():
    if request.method == "POST":
        # 执行显示数据库的操作
        sno = request.form.get("username")
        term = "2024-2025春季学期"
        sql_query_score = "SELECT s.score, c.tname, c.cname, c.cscore  FROM  study AS s INNER JOIN course AS c ON s.cno = c.cno WHERE s.sno = %s  AND s.term = %s"
        cursor.execute(sql_query_score, (sno, term))
        stu_score = cursor.fetchall()
        if stu_score:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(stu_score)
        else:
            return jsonify({'error': 'No student found with the given sno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


#  学生修改密码接口
@app.route('/updatacodestu', methods=['POST'])
def update_code_student():
    if request.method == "POST":
        # 获取表单数据
        newcode = request.form.get("newcode")
        sno = request.form.get("username")
        oldpwd = request.form.get("oldpwd")
        if not newcode or not sno:
            return jsonify({'error': 'newcode and username are required'}), 400
        # 更新数据库
        sql_query_score = "UPDATE student_account SET spassword = %s WHERE susername = %s and spassword = %s;"
        cursor.execute(sql_query_score, (newcode, sno, oldpwd))
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
    app.run(host='0.0.0.0', port=8688)
    db.close()
    print("结束")

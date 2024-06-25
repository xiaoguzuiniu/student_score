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


# 登录接口
@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        id = request.form.get("id")
        username = request.form.get("username")
        password = request.form.get("password")
        if id == '1':
            # 检查用户名是否已存在
            sql_check_user = "SELECT * FROM student_account WHERE susername = %s and spassword = %s"
            cursor.execute(sql_check_user, (username, password))
            existing_user = cursor.fetchone()
            if existing_user:
                return jsonify({"message": "登录成功！"}), 200
            return jsonify({"error": "登录失败"}), 400
        if id == '2':
            # 检查用户名是否已存在
            sql_check_user = "SELECT * FROM teacher_account WHERE tusername = %s and tpassword = %s"
            cursor.execute(sql_check_user, (username, password))
            existing_user = cursor.fetchone()
            if existing_user:
                return jsonify({"message": "登录成功！"})
            return jsonify({"error": "登录失败"}), 400
        if id == '3':
            # 检查用户名是否已存在
            sql_check_user = "SELECT * FROM admin_account WHERE ausername = %s and apassword = %s"
            cursor.execute(sql_check_user, (username, password))
            existing_user = cursor.fetchone()
            if existing_user:
                return jsonify({"message": "登录成功！"})
            return jsonify({"error": "登录失败"}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8687)
    db.close()
    print("结束")

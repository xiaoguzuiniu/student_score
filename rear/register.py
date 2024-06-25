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


# 注册接口
@app.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        id = request.form.get("id")
        username = request.form.get("username")
        password = request.form.get("password")
        if id == '1':
            # 检查用户名是否已存在
            sql_check_user = "SELECT * FROM teacher_account WHERE tusername = %s"
            cursor.execute(sql_check_user, (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                return jsonify({"error": "用户已存在！"}), 400
            # 执行插入数据库的操作
            sql_insert_user = "INSERT INTO teacher_account (tusername, tpassword) VALUES (%s, %s)"
            try:
                cursor.execute(sql_insert_user, (username, password))
                db.commit()
                return jsonify({"message": "注册成功"})
            except Exception as e:
                db.rollback()
                return jsonify({"error": "注册失败"}), 500
        if id == '2':
            # 检查用户名是否已存在
            sql_check_user = "SELECT * FROM admin_account WHERE ausername = %s"
            cursor.execute(sql_check_user, (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                return jsonify({"error": "用户已存在！"}), 400
            # 执行插入数据库的操作
            sql_insert_user = "INSERT INTO admin_account (ausername, apassword) VALUES (%s, %s)"
            try:
                cursor.execute(sql_insert_user, (username, password))
                db.commit()
                return jsonify({"message": "注册成功"})
            except Exception as e:
                db.rollback()
                return jsonify({"error": "注册失败"}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8686)
    db.close()
    print("结束")

import os

import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
from datetime import datetime

# 数据库连接
# 打开数据库连接
db = pymysql.connect(host='localhost', user='root', password='123456', database='students_select_course')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 后端服务启动
app = Flask(__name__)
CORS(app, resource=r'/*')  # 处理跨域资源共享


# 数据恢复接口
@app.route('/restore_data', methods=['POST'])
def restore_table():
    if request.method == "POST":
        backup_file_path = request.form.get('backup_file')
        if not backup_file_path:
            return jsonify({'error': 'Backup file name is required'}), 400
        if not os.path.exists(backup_file_path):
            return jsonify({'error': 'Backup file does not exist'}), 404
        try:
            # 使用subprocess执行mysql命令进行恢复，通过指定配置文件连接MySQL
            subprocess.check_call([
                'mysql',
                '--defaults-file=C:/Users/15982/.my.cnf',  # 指定MySQL配置文件路径
                'students_select_course',
                '-e', f"source {backup_file_path}"
            ])
            return jsonify({'message': 'Restore successful'}), 200
        except subprocess.CalledProcessError as e:
            return jsonify({'error': str(e)}), 500

    else:
        return jsonify({'error': 'Invalid request method'}), 405


# 获取数据库表文件名的接口
@app.route('/sqlname', methods=['POST'])
def sqlname():
    if request.method == "POST":
        # 执行显示数据库的操作
        sql_sql_info = "SELECT * FROM backup_table"
        cursor.execute(sql_sql_info, ())
        sql_info = cursor.fetchall()
        if sql_info:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(sql_info)
        else:
            return jsonify({'error': 'No student found with the given sno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


# 删除数据库表文件的接口
@app.route('/sqlremove', methods=['POST'])
def sqlremove():
    if request.method == "POST":
        backup_table_name = request.form.get('backup_table_name')
        # 删除数据库中的备份表记录
        sql_delete_backup = "DELETE FROM backup_table WHERE backup_sql_name = %s"
        cursor.execute(sql_delete_backup, (backup_table_name,))
        db.commit()
        # 在本地文件系统中删除备份文件
        backup_file_path = os.path.join('D:\python_study\database', backup_table_name)
        if os.path.exists(backup_file_path):
            os.remove(backup_file_path)
        return jsonify({'message': 'Backup table removed successfully'}), 200
    else:
        return jsonify({'error': 'Invalid request method'}), 405


# 备份数据库表的接口
@app.route('/backup_table', methods=['POST'])
def backup_table():
    if request.method == "POST":
        table_name = request.form.get('table_name')
        if not table_name:
            return jsonify({'error': 'Table name is required'}), 400

        # 生成备份文件名，包含日期时间信息
        backup_file_name = f"{table_name}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"

        try:
            # 使用subprocess执行mysqldump命令
            subprocess.check_call([
                'mysqldump',
                '-u', 'root',
                '-p123456',
                'students_select_course',
                table_name,
                '-r', backup_file_name
            ])
            # 执行存储备份表名称的操作
            sql_add_sql_name = "INSERT INTO backup_table (backup_sql_name) VALUES(%s);"
            cursor.execute(sql_add_sql_name, (backup_file_name,))
            # 提交事务
            db.commit()
            # 检查更新行数
            if cursor.rowcount > 0:
                return jsonify({'message': 'Backup successful', 'backup_file': backup_file_name}), 200
        except subprocess.CalledProcessError as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid request method'}), 405


#  管理员界面教师信息获取接口
@app.route('/teacherinfo', methods=['POST'])
def select_teacher_info():
    if request.method == "POST":
        # 执行显示数据库的操作
        sql_select_teacher_info = "SELECT * from teacher"
        cursor.execute(sql_select_teacher_info, ())
        teacher_info = cursor.fetchall()
        if teacher_info:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(teacher_info)
        else:
            return jsonify({'error': 'No student found with the given sno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


#  管理员查询职工接口
@app.route('/queryteacher', methods=['POST'])
def query_teacher_info():
    if request.method == "POST":
        tno = request.form.get('tno')
        # 执行显示数据库的操作
        sql_select_teacher_info = "SELECT * from teacher where tno = %s"
        cursor.execute(sql_select_teacher_info, (tno,))
        teacher_info = cursor.fetchone()
        if teacher_info:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(teacher_info)
        else:
            return jsonify({'error': 'No teacher found with the given tno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


#  管理员删除职工接口
@app.route('/reamoveteacher', methods=['POST'])
def reamove_teacher():
    if request.method == "POST":
        tno = request.form.get('tno')
        # 执行显示数据库的操作
        sql_remove_teacher_info1 = "delete from teacher where tno = %s"
        cursor.execute(sql_remove_teacher_info1, (tno,))
        sql_remove_teacher_info2 = "delete from teacher_account where tusername = %s"
        cursor.execute(sql_remove_teacher_info2, (tno,))
        # 提交事务
        db.commit()
        # 检查更新行数
        if cursor.rowcount > 0:
            return jsonify({'message': 'successfully'}), 200
        else:
            return jsonify({'error': 'No  found'}), 404
    else:
        return jsonify({'error': 'Invalid request method'}), 405


#  管理员添加职工接口
@app.route('/addteacher', methods=['POST'])
def add_teacher():
    if request.method == "POST":
        tno = request.form.get("tno")
        tname = request.form.get("tname")
        tsex = request.form.get("tsex")
        tage = request.form.get("tage")
        title = request.form.get("title")
        phone = request.form.get("phone")
        code = request.form.get("code")
        # 执行显示数据库的操作
        sql_add_info = "INSERT INTO teacher (tno, tname, tsex,tage,title,phone) VALUES(%s,%s,%s,%s,%s,%s);"
        sql_add_user = "INSERT INTO teacher_account (tusername,tpassword) VALUES(%s,%s);"
        cursor.execute(sql_add_info, (tno, tname, tsex, tage, title, phone))
        cursor.execute(sql_add_user, (tno, code,))
        # 提交事务
        db.commit()
        # 检查更新行数
        if cursor.rowcount > 0:
            return jsonify({'message': 'successfully'}), 200
        else:
            return jsonify({'error': 'No  found'}), 404
    else:
        return jsonify({'error': 'Invalid request method'}), 405


#  管理员界面学生信息获取接口
@app.route('/studentinfo', methods=['POST'])
def select_student_info():
    if request.method == "POST":
        # 执行显示数据库的操作
        sql_select_teacher_info = "SELECT s.*, c.cname FROM students_select_course.student s JOIN class c ON s.class_id = c.class_id"
        cursor.execute(sql_select_teacher_info, ())
        teacher_info = cursor.fetchall()
        if teacher_info:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(teacher_info)
        else:
            return jsonify({'error': 'No student found with the given sno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


#  管理员查询学生接口
@app.route('/querystudent', methods=['POST'])
def query_student_info():
    if request.method == "POST":
        sno = request.form.get('sno')
        # 执行显示数据库的操作
        sql_select_student_info = "SELECT s.*, c.cname FROM students_select_course.student s JOIN class c ON s.class_id = c.class_id WHERE s.sno = %s"
        cursor.execute(sql_select_student_info, (sno,))
        student_info = cursor.fetchone()
        if student_info:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(student_info)
        else:
            return jsonify({'error': 'No teacher found with the given tno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


#  管理员删除学生接口
@app.route('/reamovestudent', methods=['POST'])
def reamove_student():
    if request.method == "POST":
        sno = request.form.get('sno')
        # 执行删除数据库记录的操作
        sql_remove_student_info1 = "DELETE FROM student WHERE sno = %s"
        cursor.execute(sql_remove_student_info1, (sno,))
        sql_remove_student_info2 = "DELETE FROM student_account WHERE susername = %s"
        cursor.execute(sql_remove_student_info2, (sno,))
        # 提交事务
        db.commit()

        # 检查更新行数
        if cursor.rowcount > 0:
            return jsonify({'message': 'Successfully deleted'}), 200
        else:
            return jsonify({'error': 'No records found to delete'}), 404
    else:
        return jsonify({'error': 'Invalid request method'}), 405


#  班级数目查询接口
@app.route('/classnum', methods=['POST'])
def show_class_num():
    if request.method == "POST":
        # 创建视图语句
        # CREATE VIEW
        # class_view AS
        # SELECT cname, class_id
        # FROR class
        # 执行显示数据库的操作
        sql_show_info = "SELECT cname, class_id FROM class_view;"

        cursor.execute(sql_show_info, ())
        stu_info = cursor.fetchall()
        if stu_info:
            # 使用jsonify将结果转换为JSON并返回
            return jsonify(stu_info)
        else:
            return jsonify({'error': 'No student found with the given sno'}), 404
    else:
        return jsonify({'error': 'No sno provided'}), 400


#  管理员添加学生接口
@app.route('/addstudent', methods=['POST'])
def add_student():
    if request.method == "POST":
        sno = request.form.get("sno")
        sname = request.form.get("sname")
        ssex = request.form.get("ssex")
        sage = request.form.get("sage")
        sclass = request.form.get("class")
        code = request.form.get("code")
        # 执行显示数据库的操作
        sql_add_info = "INSERT INTO student (sno, sname, ssex,sage,class_id) SELECT %s,%s,%s,%s,class_id  FROM class  WHERE cname = %s"
        sql_add_user = "INSERT INTO student_account (susername, spassword) values(%s,%s)"
        cursor.execute(sql_add_info, (sno, sname, ssex, sage, sclass))
        cursor.execute(sql_add_user, (sno, code))
        # 提交事务
        db.commit()
        # 检查更新行数
        if cursor.rowcount > 0:
            return jsonify({'message': 'successfully'}), 200
        else:
            return jsonify({'error': 'No  found'}), 404
    else:
        return jsonify({'error': 'Invalid request method'}), 405


#  管理员修改密码接口
@app.route('/updatacodeadm', methods=['POST'])
def update_code():
    if request.method == "POST":
        # 获取表单数据
        type = request.form.get("type")
        newcode = request.form.get("newcode")
        username = request.form.get("username")
        if not newcode or not username:
            return jsonify({'error': 'newcode and username are required'}), 400
        # 更新数据库
        if type == '职工':
            sql_updata_code = "UPDATE teacher_account SET tpassword = %s WHERE tusername = %s ;"
            cursor.execute(sql_updata_code, (newcode, username))
        if type == '学生':
            sql_updata_code = "UPDATE student_account SET spassword = %s WHERE susername = %s ;"
            cursor.execute(sql_updata_code, (newcode, username))
        if type == '管理员':
            sql_updata_code = "UPDATE admin_account SET apassword = %s WHERE ausername = %s ;"
            cursor.execute(sql_updata_code, (newcode, username))
        # 提交事务
        db.commit()
        # 检查更新行数
        if cursor.rowcount > 0:
            return jsonify({'message': 'Password updated successfully'}), 200
        else:
            return jsonify({'error': 'No student found with the given username'}), 404
    else:
        return jsonify({'error': 'Invalid request method'}), 405


#  管理员修改学生接口
@app.route('/updatestudent', methods=['POST'])
def updata_student():
    if request.method == "POST":
        sno = request.form.get("sno")
        sname = request.form.get("name")
        ssex = request.form.get("sex")
        sage = request.form.get("age")
        sclass = request.form.get("class")
        print(sclass)
        # 执行显示数据库的操作
        sql_updata_info = "UPDATE student SET sname = %s, ssex = %s, sage = %s, class_id = (SELECT class_id FROM class WHERE cname = %s) WHERE sno = %s;"
        cursor.execute(sql_updata_info, (sname, ssex, sage, sclass, sno))
        # 提交事务
        db.commit()
        # 检查更新行数
        if cursor.rowcount > 0:
            return jsonify({'message': 'successfully'}), 200
        else:
            return jsonify({'error': 'No  found'}), 404
    else:
        return jsonify({'error': 'Invalid request method'}), 405


#  管理员修改职工接口
@app.route('/updateteacher', methods=['POST'])
def updata_teacher():
    if request.method == "POST":
        tno = request.form.get("tno")
        sname = request.form.get("name")
        ssex = request.form.get("sex")
        sage = request.form.get("age")
        title = request.form.get("title")
        phone = request.form.get("phone")
        # 执行显示数据库的操作
        sql_updata_info = "UPDATE teacher SET tname = %s, tsex = %s, tage = %s, title = %s, phone = %s WHERE tno = %s;"
        cursor.execute(sql_updata_info, (sname, ssex, sage, title, phone, tno))
        # 提交事务
        db.commit()
        # 检查更新行数
        if cursor.rowcount > 0:
            return jsonify({'message': 'successfully'}), 200
        else:
            return jsonify({'error': 'No  found'}), 404
    else:
        return jsonify({'error': 'Invalid request method'}), 405


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8690)
    db.close()
    print("结束")

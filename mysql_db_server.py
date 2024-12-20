from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'sql7752654',
    'password': 'pxDs8kF4Me',
    'host': 'sql7.freemysqlhosting.net',
    'database': 'sql7752654'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    return "welcomeee to the Flask'trofim app!"

@app.route('/data', methods=['GET'])
def get_teacher_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT
            t.FullName,
            l.day,
            g.group_name,
            s.SubjectName,
            lt.lesson_type,
            r.RoomNumber
        FROM lesson l
        JOIN teachers t ON l.TeacherID = t.id
        JOIN groups g ON l.GroupID = g.id
        JOIN subjects1 s ON l.SubjectID = s.id
        LEFT JOIN lesson_type1 lt ON l.lesson_type = lt.id
        JOIN rooms r ON l.RoomID = r.id
        WHERE t.id = 1
        ORDER BY l.day''')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/group', methods=['GET'])
def get_group_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT
            g.group_name,
            t.FullName,
            l.day,
            s.SubjectName,
            lt.lesson_type,
            r.RoomNumber
        FROM lesson l
        JOIN teachers t ON l.TeacherID = t.id
        JOIN groups g ON l.GroupID = g.id
        JOIN subjects1 s ON l.SubjectID = s.id
        LEFT JOIN lesson_type1 lt ON l.lesson_type = lt.id
        JOIN rooms r ON l.RoomID = r.id
        WHERE g.id = 1
        ORDER BY l.day''')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/room', methods=['GET'])
def get_room_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT
            r.RoomNumber,
            g.group_name,
            t.FullName,
            l.day,
            s.SubjectName,
            lt.lesson_type
        FROM lesson l
        JOIN teachers t ON l.TeacherID = t.id
        JOIN groups g ON l.GroupID = g.id
        JOIN subjects1 s ON l.SubjectID = s.id
        LEFT JOIN lesson_type1 lt ON l.lesson_type = lt.id
        JOIN rooms r ON l.RoomID = r.id
        WHERE r.id = 1
        ORDER BY l.day''')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)

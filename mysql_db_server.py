from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'sql7751010',
    'password': 'B2hrwJGke7',
    'host': 'sql7.freemysqlhosting.net',
    'database': 'sql7751010'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/data', methods=['GET'])
def get_table_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT
            t.FullName,
            l.day,
            g.group_name,
            s.SubjectName,
            lt.lesson_type,
            r.RoomNumber'
        FROM Lesson l
        JOIN Teachers t ON l.TeacherID = t.id
        JOIN Groups g ON l.GroupID = g.id
        JOIN Subjects1 s ON l.SubjectID = s.id
        LEFT JOIN Lesson_Type1 lt ON l.lesson_type = lt.id
        JOIN Rooms r ON l.RoomID = r.id
        WHERE t.id = @TeacherID
        ORDER BY l.day''')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)

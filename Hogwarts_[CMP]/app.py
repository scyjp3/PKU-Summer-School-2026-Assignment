from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = 'hogwarts_secret_key_123'

students = {
    'harry': {'password': 'potter', 'name': '哈利·波特', 'house': '格兰芬多', 'year': 5, 'email': 'harry@hogwarts.edu'},
    'ron': {'password': 'weasley', 'name': '罗恩·韦斯莱', 'house': '格兰芬多', 'year': 5, 'email': 'ron@hogwarts.edu'},
    'hermione': {'password': 'granger', 'name': '赫敏·格兰杰', 'house': '格兰芬多', 'year': 5, 'email': 'hermione@hogwarts.edu'},
    'draco': {'password': 'malfoy', 'name': '德拉科·马尔福', 'house': '斯莱特林', 'year': 5, 'email': 'draco@hogwarts.edu'}
}

assignments = [
    {'id': 1, 'title': '魔药课作业 - 复方汤剂', 'course': '魔药学', 'teacher': '斯内普教授', 'deadline': '2026-07-30', 'status': 'pending', 'score': None, 'submitted': False},
    {'id': 2, 'title': '变形课作业 - 老鼠变茶杯', 'course': '变形术', 'teacher': '麦格教授', 'deadline': '2026-08-05', 'status': 'pending', 'score': None, 'submitted': False},
    {'id': 3, 'title': '魔咒课作业 - 悬浮咒', 'course': '魔咒学', 'teacher': '弗立维教授', 'deadline': '2026-07-28', 'status': 'graded', 'score': 92, 'submitted': True},
    {'id': 4, 'title': '黑魔法防御术 - 守护神咒', 'course': '黑魔法防御术', 'teacher': '卢平教授', 'deadline': '2026-08-10', 'status': 'pending', 'score': None, 'submitted': False},
    {'id': 5, 'title': '草药课作业 - 曼德拉草', 'course': '草药学', 'teacher': '斯普劳特教授', 'deadline': '2026-07-25', 'status': 'graded', 'score': 88, 'submitted': True},
    {'id': 6, 'title': '天文学作业 - 月球轨道', 'course': '天文学', 'teacher': '辛尼斯塔教授', 'deadline': '2026-08-15', 'status': 'pending', 'score': None, 'submitted': False}
]

@app.route('/')
def index():
    if 'username' in session:
        return render_template('dashboard.html')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in students and students[username]['password'] == password:
        session['username'] = username
        return jsonify({'success': True, 'user': students[username]})
    return jsonify({'success': False, 'message': '用户名或密码错误'})

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/api/user')
def get_user():
    if 'username' in session:
        return jsonify({'success': True, 'user': students[session['username']]})
    return jsonify({'success': False, 'message': '未登录'})

@app.route('/api/assignments')
def get_assignments():
    if 'username' not in session:
        return jsonify({'success': False, 'message': '未登录'})
    return jsonify({'success': True, 'assignments': assignments})

@app.route('/api/assignment/<int:aid>')
def get_assignment(aid):
    if 'username' not in session:
        return jsonify({'success': False, 'message': '未登录'})
    assignment = next((a for a in assignments if a['id'] == aid), None)
    if assignment:
        return jsonify({'success': True, 'assignment': assignment})
    return jsonify({'success': False, 'message': '作业不存在'})

@app.route('/api/submit/<int:aid>', methods=['POST'])
def submit_assignment(aid):
    if 'username' not in session:
        return jsonify({'success': False, 'message': '未登录'})
    data = request.get_json()
    assignment = next((a for a in assignments if a['id'] == aid), None)
    if assignment:
        assignment['submitted'] = True
        assignment['status'] = 'submitted'
        assignment['submitted_content'] = data.get('content', '')
        return jsonify({'success': True, 'message': '作业提交成功！猫头鹰已送出'})
    return jsonify({'success': False, 'message': '作业不存在'})

@app.route('/api/statistics')
def get_statistics():
    if 'username' not in session:
        return jsonify({'success': False, 'message': '未登录'})
    graded = [a for a in assignments if a['score'] is not None]
    avg_score = sum(a['score'] for a in graded) / len(graded) if graded else 0
    return jsonify({
        'success': True,
        'total': len(assignments),
        'submitted': sum(1 for a in assignments if a['submitted']),
        'pending': sum(1 for a in assignments if a['status'] == 'pending'),
        'graded': len(graded),
        'avg_score': round(avg_score, 1),
        'scores': [a['score'] for a in graded],
        'courses': ['魔药学', '变形术', '魔咒学', '黑魔法防御术', '草药学', '天文学']
    })

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect(url_for('index'))

@app.route('/assignments')
def assignments_page():
    if 'username' in session:
        return render_template('assignments.html')
    return redirect(url_for('index'))

@app.route('/statistics')
def statistics_page():
    if 'username' in session:
        return render_template('statistics.html')
    return redirect(url_for('index'))

@app.route('/profile')
def profile_page():
    if 'username' in session:
        return render_template('profile.html')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
document.addEventListener('DOMContentLoaded', function() {
    setupLogin();
    setupDashboard();
    setupAssignments();
    setupStatistics();
    setupProfile();
    setupLogout();
});

async function apiGet(endpoint) {
    try {
        const response = await fetch(endpoint);
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        return { success: false, message: '网络错误' };
    }
}

async function apiPost(endpoint, data) {
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        return { success: false, message: '网络错误' };
    }
}

function setupLogin() {
    const form = document.getElementById('login-form');
    if (!form) return;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value;
        
        if (!username || !password) {
            alert('请输入用户名和密码');
            return;
        }

        const result = await apiPost('/login', { username, password });
        
        if (result.success) {
            window.location.href = '/dashboard';
        } else {
            alert(result.message);
        }
    });
}

function setupLogout() {
    const logoutBtn = document.getElementById('logout-btn');
    if (!logoutBtn) return;

    logoutBtn.addEventListener('click', function() {
        if (confirm('确定要离开霍格沃茨吗？')) {
            window.location.href = '/logout';
        }
    });
}

function setupDashboard() {
    const welcomeTitle = document.getElementById('welcome-title');
    const welcomeHouse = document.getElementById('welcome-house');
    
    if (!welcomeTitle) return;

    apiGet('/api/user').then(result => {
        if (result.success) {
            const user = result.user;
            welcomeTitle.textContent = '欢迎回来，' + user.name;
            welcomeHouse.textContent = user.house + '学院 · 五年级';
        }
    });

    apiGet('/api/statistics').then(result => {
        if (result.success) {
            document.getElementById('stat-total').textContent = result.total;
            document.getElementById('stat-submitted').textContent = result.submitted;
            document.getElementById('stat-pending').textContent = result.pending;
            document.getElementById('stat-avg').textContent = result.avg_score;
        }
    });

    apiGet('/api/assignments').then(result => {
        if (result.success) {
            const assignments = result.assignments;
            
            const recentList = document.getElementById('recent-assignments');
            const deadlineList = document.getElementById('deadline-assignments');
            
            if (recentList) {
                const recent = assignments.slice(0, 4);
                recentList.innerHTML = recent.map(a => createAssignmentItem(a)).join('');
            }

            if (deadlineList) {
                const pending = assignments.filter(function(a) { return a.status === 'pending'; });
                const sorted = pending.sort(function(a, b) { return new Date(a.deadline) - new Date(b.deadline); }).slice(0, 3);
                deadlineList.innerHTML = sorted.map(a => createAssignmentItem(a)).join('');
            }
        }
    });
}

function createAssignmentItem(assignment) {
    var statusClass = 'status-pending';
    var statusText = '待提交';
    
    if (assignment.submitted) {
        if (assignment.score !== null) {
            statusClass = 'status-graded';
            statusText = '已批改 ' + assignment.score + '分';
        } else {
            statusClass = 'status-submitted';
            statusText = '已提交';
        }
    }

    return '<div class="assignment-item">' +
        '<div class="assignment-info">' +
        '<h3>' + assignment.title + '</h3>' +
        '<p>' + assignment.course + ' · ' + assignment.teacher + ' · ' + assignment.deadline + '</p>' +
        '</div>' +
        '<span class="assignment-status ' + statusClass + '">' + statusText + '</span>' +
        '</div>';
}

function setupAssignments() {
    var grid = document.getElementById('assignment-grid');
    if (!grid) return;

    var currentAssignments = [];

    apiGet('/api/assignments').then(function(result) {
        if (result.success) {
            currentAssignments = result.assignments;
            renderAssignments(currentAssignments);
        }
    });

    var filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            filterBtns.forEach(function(b) { b.classList.remove('active'); });
            this.classList.add('active');
            
            var filter = this.dataset.filter;
            var filtered = currentAssignments;
            
            if (filter === 'pending') {
                filtered = currentAssignments.filter(function(a) { return a.status === 'pending'; });
            } else if (filter === 'submitted') {
                filtered = currentAssignments.filter(function(a) { return a.submitted && a.score === null; });
            } else if (filter === 'graded') {
                filtered = currentAssignments.filter(function(a) { return a.score !== null; });
            }
            
            renderAssignments(filtered);
        });
    });

    function renderAssignments(assignments) {
        grid.innerHTML = assignments.map(function(a) { return createAssignmentCard(a); }).join('');
        
        document.querySelectorAll('.assignment-card-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                var aid = parseInt(this.dataset.aid);
                openSubmitModal(aid);
            });
        });
    }

    function createAssignmentCard(assignment) {
        var scoreHtml = '';
        var btnHtml = '';
        
        if (assignment.score !== null) {
            scoreHtml = '<div class="assignment-card-score">' + assignment.score + '</div>';
        }
        
        if (!assignment.submitted) {
            btnHtml = '<button class="assignment-card-btn" data-aid="' + assignment.id + '">🦉 提交作业</button>';
        } else if (assignment.score === null) {
            btnHtml = '<button class="assignment-card-btn" disabled>⏳ 批改中...</button>';
        } else {
            btnHtml = '<button class="assignment-card-btn" disabled>✅ 已完成</button>';
        }

        return '<div class="assignment-card">' +
            '<div>' +
            '<h3 class="assignment-card-title">' + assignment.title + '</h3>' +
            '<p class="assignment-card-meta">📚 ' + assignment.course + '</p>' +
            '<p class="assignment-card-meta">👨‍🏫 ' + assignment.teacher + '</p>' +
            '<p class="assignment-card-meta">📅 截止: ' + assignment.deadline + '</p>' +
            '</div>' +
            scoreHtml +
            btnHtml +
            '</div>';
    }

    var modalClose = document.getElementById('modal-close');
    if (modalClose) {
        modalClose.addEventListener('click', closeModal);
    }
    
    var cancelSubmit = document.getElementById('cancel-submit');
    if (cancelSubmit) {
        cancelSubmit.addEventListener('click', closeModal);
    }
    
    var confirmSubmit = document.getElementById('confirm-submit');
    if (confirmSubmit) {
        confirmSubmit.addEventListener('click', async function() {
            var content = document.getElementById('submit-content').value.trim();
            if (!content) {
                alert('请输入作业内容');
                return;
            }
            
            var result = await apiPost('/api/submit/' + window.submitAid, { content: content });
            
            if (result.success) {
                alert(result.message);
                closeModal();
                window.location.reload();
            } else {
                alert(result.message);
            }
        });
    }
}

function openSubmitModal(aid) {
    apiGet('/api/assignment/' + aid).then(function(result) {
        if (result.success) {
            var assignment = result.assignment;
            document.getElementById('modal-assignment-info').innerHTML =
                '<p><strong>课程:</strong> ' + assignment.course + '</p>' +
                '<p><strong>作业:</strong> ' + assignment.title + '</p>' +
                '<p><strong>老师:</strong> ' + assignment.teacher + '</p>' +
                '<p><strong>截止日期:</strong> ' + assignment.deadline + '</p>';
            
            document.getElementById('submit-content').value = '';
            document.getElementById('submit-modal').classList.add('active');
            
            window.submitAid = aid;
        }
    });
}

function closeModal() {
    var modal = document.getElementById('submit-modal');
    if (modal) {
        modal.classList.remove('active');
    }
}

function setupStatistics() {
    var scoreChartCanvas = document.getElementById('score-chart');
    var courseChartCanvas = document.getElementById('course-chart');
    
    if (!scoreChartCanvas) return;

    apiGet('/api/statistics').then(function(result) {
        if (result.success) {
            var stats = result;
            
            var statOverall = document.getElementById('stat-overall');
            if (statOverall) statOverall.textContent = stats.avg_score;
            
            var statCompleted = document.getElementById('stat-completed');
            if (statCompleted) statCompleted.textContent = Math.round((stats.submitted / stats.total) * 100) + '%';
            
            var statExcellent = document.getElementById('stat-excellent');
            if (statExcellent) statExcellent.textContent = stats.scores.filter(function(s) { return s >= 90; }).length;

            if (window.Chart) {
                new Chart(scoreChartCanvas, {
                    type: 'bar',
                    data: {
                        labels: ['魔药学', '变形术', '魔咒学', '黑魔法防御术', '草药学', '天文学'],
                        datasets: [{
                            label: '成绩',
                            data: stats.scores.length >= 6 ? stats.scores : stats.scores.concat(Array(6 - stats.scores.length).fill(null)),
                            backgroundColor: 'rgba(212, 175, 55, 0.7)',
                            borderColor: 'rgba(212, 175, 55, 1)',
                            borderWidth: 1,
                            borderRadius: 5
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                labels: { color: '#e8e8e8' }
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: 100,
                                ticks: { color: '#a0a0b0' },
                                grid: { color: 'rgba(255, 255, 255, 0.1)' }
                            },
                            x: {
                                ticks: { color: '#a0a0b0' },
                                grid: { display: false }
                            }
                        }
                    }
                });

                new Chart(courseChartCanvas, {
                    type: 'radar',
                    data: {
                        labels: ['魔药学', '变形术', '魔咒学', '黑魔法防御术', '草药学', '天文学'],
                        datasets: [{
                            label: '成绩',
                            data: stats.scores.length >= 6 ? stats.scores : stats.scores.concat(Array(6 - stats.scores.length).fill(50)),
                            backgroundColor: 'rgba(107, 91, 149, 0.2)',
                            borderColor: 'rgba(107, 91, 149, 1)',
                            borderWidth: 2,
                            pointBackgroundColor: 'rgba(212, 175, 55, 1)',
                            pointBorderColor: '#fff',
                            pointHoverBackgroundColor: '#fff',
                            pointHoverBorderColor: 'rgba(107, 91, 149, 1)'
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                labels: { color: '#e8e8e8' }
                            }
                        },
                        scales: {
                            r: {
                                angleLines: { color: 'rgba(255, 255, 255, 0.1)' },
                                grid: { color: 'rgba(255, 255, 255, 0.1)' },
                                pointLabels: { color: '#a0a0b0' },
                                ticks: { color: '#a0a0b0', backdropColor: 'transparent' },
                                suggestedMin: 0,
                                suggestedMax: 100
                            }
                        }
                    }
                });
            }

            var progressList = document.getElementById('progress-list');
            if (progressList) {
                apiGet('/api/assignments').then(function(assignmentsResult) {
                    if (assignmentsResult.success) {
                        var assignments = assignmentsResult.assignments;
                        progressList.innerHTML = assignments.map(function(a) {
                            var percent = a.submitted ? (a.score !== null ? 100 : 50) : 0;
                            return '<div class="progress-item">' +
                                '<div class="progress-header">' +
                                '<span class="progress-title">' + a.title + '</span>' +
                                '<span class="progress-percent">' + percent + '%</span>' +
                                '</div>' +
                                '<div class="progress-bar">' +
                                '<div class="progress-fill" style="width: ' + percent + '%"></div>' +
                                '</div>' +
                                '</div>';
                        }).join('');
                    }
                });
            }
        }
    });
}

function setupProfile() {
    apiGet('/api/user').then(function(result) {
        if (result.success) {
            var user = result.user;
            
            var profileName = document.getElementById('profile-name');
            if (profileName) profileName.textContent = user.name;
            
            var profileUsername = document.getElementById('profile-username');
            if (profileUsername) profileUsername.textContent = '@' + user.name;
            
            var profileHouse = document.getElementById('profile-house');
            if (profileHouse) profileHouse.textContent = user.house;
            
            var profileYear = document.getElementById('profile-year');
            if (profileYear) profileYear.textContent = user.year + '年级';
            
            var profileHouseDetail = document.getElementById('profile-house-detail');
            if (profileHouseDetail) profileHouseDetail.textContent = user.house;
            
            var profileEmail = document.getElementById('profile-email');
            if (profileEmail) profileEmail.textContent = user.email;
            
            var houseBadge = document.getElementById('house-badge');
            if (houseBadge) {
                var emoji = '🏠';
                if (user.house.indexOf('格兰芬多') !== -1) emoji = '🦁';
                else if (user.house.indexOf('斯莱特林') !== -1) emoji = '🐍';
                else if (user.house.indexOf('赫奇帕奇') !== -1) emoji = '🦡';
                else if (user.house.indexOf('拉文克劳') !== -1) emoji = '🦅';
                houseBadge.textContent = emoji;
            }
        }
    });
}
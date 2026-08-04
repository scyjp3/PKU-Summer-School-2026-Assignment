const API_BASE_URL = "https://pysummer.pkuai.cc/api/v1";

class CourseAPI {
    constructor() {
        this.token = localStorage.getItem('access_token');
    }

    setToken(token) {
        this.token = token;
        localStorage.setItem('access_token', token);
    }

    clearToken() {
        this.token = null;
        localStorage.removeItem('access_token');
    }

    async login(identifier, secret) {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ identifier, secret })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error?.message || '登录失败');
        }

        const data = await response.json();
        this.setToken(data.access_token);
        return data;
    }

    async getMe() {
        const response = await fetch(`${API_BASE_URL}/auth/me`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        });

        if (!response.ok) {
            throw new Error('获取用户信息失败');
        }

        return await response.json();
    }

    async getStudentInfo() {
        const response = await fetch(`${API_BASE_URL}/students/me`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        });

        if (!response.ok) {
            throw new Error('获取学生信息失败');
        }

        return await response.json();
    }

    async getAssignments() {
        const response = await fetch(`${API_BASE_URL}/assignments`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        });

        if (!response.ok) {
            throw new Error('获取作业列表失败');
        }

        return await response.json();
    }

    async getAssignment(assignmentId) {
        const response = await fetch(`${API_BASE_URL}/assignments/${assignmentId}`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        });

        if (!response.ok) {
            throw new Error('获取作业详情失败');
        }

        return await response.json();
    }

    async submitAssignment(assignmentId, text, file, llmChatLog) {
        const formData = new FormData();
        if (text) formData.append('text', text);
        if (file) formData.append('file', file);
        if (llmChatLog) formData.append('LLM_chat_log', llmChatLog);

        const response = await fetch(`${API_BASE_URL}/assignments/${assignmentId}/submissions`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${this.token}`
            },
            body: formData
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error?.message || '提交作业失败');
        }

        return await response.json();
    }

    async getSubmissions(assignmentId) {
        const response = await fetch(`${API_BASE_URL}/assignments/${assignmentId}/submissions`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        });

        if (!response.ok) {
            throw new Error('获取提交记录失败');
        }

        return await response.json();
    }

    async getGrades() {
        const response = await fetch(`${API_BASE_URL}/grades`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        });

        if (!response.ok) {
            throw new Error('获取成绩失败');
        }

        return await response.json();
    }

    async getStudentSummary() {
        const response = await fetch(`${API_BASE_URL}/students/me/summary`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        });

        if (!response.ok) {
            throw new Error('获取统计信息失败');
        }

        return await response.json();
    }

    async downloadFile(url) {
        const response = await fetch(`${API_BASE_URL}${url}`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        });

        if (!response.ok) {
            throw new Error('下载文件失败');
        }

        return response;
    }
}
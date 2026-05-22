# 应聘搭子 Web 应用

## 🎯 简介

**应聘搭子** - 你的面试战友，帮你回答面试问题。

专业不炫技，流畅顺口接地气，让你在面试中脱颖而出。

---

## 🚀 快速开始

### 方式一：本地使用

#### 1. 启动后端服务

确保后端服务在9000端口运行：

```bash
cd /workspace/projects
python src/main.py -p 9000
```

#### 2. 启动前端服务

```bash
cd /workspace/projects/web-partner
python start_web.py
```

#### 3. 打开浏览器

访问：`http://localhost:8001`

---

### 方式二：直接打开HTML文件

如果不想启动服务器，也可以直接双击打开HTML文件：

```bash
open web-partner/index.html
# 或
xdg-open web-partner/index.html
```

---

## 📱 界面预览

```
┌─────────────────────────────────────┐
│  🤝 应聘搭子                        │
│  你的面试战友，帮你回答面试问题       │
├─────────────────────────────────────┤
│                                     │
│  🤝 嘿，我是你的应聘搭子！            │
│                                     │
│  👤 自我介绍怎么做？                  │
│                                     │
│  🤝 行，我帮你组织一下...             │
│                                     │
├─────────────────────────────────────┤
│  [自我介绍] [为什么离职] [优点缺点]   │
├─────────────────────────────────────┤
│  [输入面试问题...]          [发送]   │
└─────────────────────────────────────┘
```

---

## ⚙️ 配置说明

### 修改API地址

如果后端服务不在本地，需要修改 `index.html` 中的API地址：

```javascript
// 找到这行代码，修改为你的后端地址
const API_URL = 'http://localhost:9000/chat';
```

### 修改端口

- 前端端口：修改 `start_web.py` 中的 `PORT = 8001`
- 后端端口：确保与 `index.html` 中的配置一致

---

## 🌐 公网部署

### 方案一：Nginx反向代理

#### 1. 安装Nginx

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx

# CentOS
sudo yum install nginx
```

#### 2. 配置Nginx

```nginx
server {
    listen 80;
    server_name your-domain.com;

    # 前端静态文件
    location / {
        root /path/to/web-partner;
        index index.html;
    }

    # 后端API代理
    location /api {
        proxy_pass http://127.0.0.1:9000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

#### 3. 启动服务

```bash
# 启动后端
python src/main.py -p 9000 &

# 启动Nginx
sudo nginx -t
sudo systemctl restart nginx
```

---

### 方案二：Docker部署

#### 1. 创建Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# 复制应用
COPY src/ ./src/
COPY web-partner/ ./web-partner/

# 安装依赖
RUN pip install flask flask-cors

# 暴露端口
EXPOSE 9000 8001

# 启动命令
CMD python src/main.py -p 9000 & python start_web.py
```

#### 2. 构建和运行

```bash
docker build -t interview-partner .
docker run -d -p 9000:9000 -p 8001:8001 interview-partner
```

---

## 📦 快捷问题

应用内置了4个快捷问题按钮：

1. **自我介绍** - 怎么做一个出彩的自我介绍
2. **为什么离职** - 如何巧妙回答离职原因
3. **优点缺点** - 如何扬长避短
4. **职业规划** - 如何展示职业发展野心

---

## 🔧 常见问题

### 1. 页面打不开

确保：
- 后端服务已启动（9000端口）
- 前端服务已启动（8001端口）
- 浏览器允许跨域请求

### 2. 发送消息没反应

检查浏览器控制台（F12）是否有错误信息：
- 常见错误：`Failed to fetch`
- 解决方案：确保后端服务正常运行

### 3. 回答内容不满意

应聘搭子使用AI模型生成回答，可以：
- 调整后端模型配置
- 修改提示词（参考 `INTERVIEW_PARTNER.md`）

---

## 📚 相关文件

- `index.html` - Web前端页面
- `start_web.py` - 启动脚本
- `README.md` - 使用说明

---

## 🤝 技术支持

如有问题，请检查：

1. 后端日志：`/workspace/projects/server.log`
2. 浏览器控制台：F12 → Console
3. 网络请求：F12 → Network

---

**祝你面试顺利！🎯**

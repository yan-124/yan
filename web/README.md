# IT面试助手 Web应用

一个漂亮的Web聊天界面，让用户可以通过浏览器使用IT面试助手。

## 🎯 功能特点

- ✅ 现代化聊天界面
- ✅ 移动端完美适配
- ✅ 快捷操作按钮
- ✅ 实时对话
- ✅ 打字动画效果
- ✅ 响应式设计

## 📁 文件结构

```
web/
├── index.html      # Web前端页面
├── start_web.py    # 启动脚本
└── README.md       # 使用说明
```

## 🚀 快速开始

### 方式一：本地使用

1. **启动后端服务**
   ```bash
   cd /workspace/projects
   python src/main.py -p 9000
   ```

2. **打开前端页面**
   
   直接在浏览器中打开 `web/index.html` 文件

3. **开始聊天**
   
   在输入框中输入问题，点击发送按钮

### 方式二：本地文件访问

1. 双击 `web/index.html` 文件
2. 浏览器会自动打开页面
3. 确保后端服务在 9000 端口运行

## 📱 界面预览

```
┌─────────────────────────────────┐
│  🤖 IT面试助手                   │
│  测开与安全工程领域的智能化平台    │
├─────────────────────────────────┤
│                                 │
│  👋 您好，我是IT面试助手          │
│                                 │
│  [用户] 你好                     │
│                                 │
│  [助手] 嘿，我是IT面试助手...     │
│                                 │
├─────────────────────────────────┤
│  [输入框...]              [发送]│
└─────────────────────────────────┘
```

## 🔧 配置说明

### API地址配置

如果需要修改API地址，编辑 `index.html` 文件，找到：

```javascript
const API_URL = 'http://localhost:9000/chat';
```

修改为你的后端服务地址。

## 🌐 公网部署

### 1. 服务器要求

- Linux服务器（阿里云/腾讯云等）
- Nginx安装
- 域名（可选）

### 2. 部署步骤

#### 步骤1：安装Nginx

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install nginx

# CentOS
sudo yum install nginx
```

#### 步骤2：配置Nginx

创建配置文件 `/etc/nginx/sites-available/it-interview`:

```nginx
server {
    listen 80;
    server_name your-domain.com;  # 你的域名或IP

    # 前端静态文件
    location / {
        root /var/www/it-interview;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    # 反向代理到后端API
    location /api/ {
        proxy_pass http://localhost:9000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 步骤3：启用配置

```bash
# 启用站点
sudo ln -s /etc/nginx/sites-available/it-interview /etc/nginx/sites-enabled/

# 测试配置
sudo nginx -t

# 重启Nginx
sudo systemctl restart nginx
```

#### 步骤4：部署前端文件

```bash
# 创建目录
sudo mkdir -p /var/www/it-interview

# 复制文件
sudo cp -r web/* /var/www/it-interview/

# 设置权限
sudo chmod -R 755 /var/www/it-interview
```

#### 步骤5：启动后端服务

```bash
cd /workspace/projects
nohup python src/main.py -p 9000 > /var/log/it-interview.log 2>&1 &
```

### 3. HTTPS配置（可选）

使用Let's Encrypt免费SSL证书：

```bash
# 安装certbot
sudo apt-get install certbot python3-certbot-nginx

# 获取证书
sudo certbot --nginx -d your-domain.com
```

## 📊 访问统计

部署完成后，你可以：

1. 查看Nginx访问日志
2. 使用百度统计/Google Analytics
3. 配置Google Tag Manager

## 🔒 安全建议

1. **配置防火墙**
   ```bash
   sudo ufw allow 80
   sudo ufw allow 443
   ```

2. **限制API访问**
   - 在后端添加API密钥验证
   - 使用Nginx限制IP访问

3. **定期更新**
   - 更新Nginx到最新版本
   - 更新Python依赖包

## 🐛 常见问题

### 1. 页面打不开

- 检查Nginx是否运行：`sudo systemctl status nginx`
- 检查端口是否冲突：`sudo netstat -tulpn | grep 80`

### 2. 消息发送失败

- 检查后端服务是否运行
- 检查API地址是否正确
- 查看浏览器控制台错误

### 3. 移动端显示异常

- 清除浏览器缓存
- 确保使用最新版本的Chrome/Safari

## 📞 获取帮助

如有问题，请提交Issue到GitHub仓库。

## 📄 License

MIT License

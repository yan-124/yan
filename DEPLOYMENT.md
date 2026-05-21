# IT面试助手 - 本地部署指南

## 📋 前提条件

### 环境要求
- Python 3.10+
- pip 或 uv 包管理器
- 4GB+ RAM
- 稳定的网络连接

### 依赖
- FastAPI
- LangChain
- LangGraph
- Uvicorn
- 其他依赖见 `pyproject.toml`

---

## 🚀 快速部署

### 方式一：使用 uv（推荐）

```bash
# 1. 进入项目目录
cd /path/to/it-interviewer

# 2. 安装依赖
uv sync

# 3. 启动服务
uv run python src/main.py -p 9000
```

### 方式二：使用 pip

```bash
# 1. 进入项目目录
cd /path/to/it-interviewer

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动服务
python src/main.py -p 9000
```

### 方式三：Docker 部署

```bash
# 1. 构建镜像
docker build -t it-interviewer .

# 2. 运行容器
docker run -d -p 9000:9000 it-interviewer
```

---

## 🌐 访问服务

服务启动后，可以通过以下方式访问：

### Web 界面
```
http://localhost:9000
```

### API 端点

#### 聊天接口
```bash
curl -X POST http://localhost:9000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "text": "我要练习测试开发面试",
    "session_id": "test-session-001"
  }'
```

#### 健康检查
```bash
curl http://localhost:9000/health
```

---

## ⚙️ 配置说明

### 修改端口

默认端口是 9000，可以通过 `-p` 参数修改：

```bash
python src/main.py -p 8080
```

### 修改模型配置

编辑 `config/agent_llm_config.json` 文件：

```json
{
    "config": {
        "model": "your-model-name",
        "temperature": 0.7,
        "max_completion_tokens": 10000
    },
    "sp": "your-system-prompt",
    "tools": []
}
```

### 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `COZE_WORKLOAD_IDENTITY_API_KEY` | API 密钥 | 必填 |
| `COZE_INTEGRATION_MODEL_BASE_URL` | 模型服务地址 | 必填 |

---

## 🛠️ 故障排查

### 服务启动失败

**错误：端口已被占用**
```bash
# 查看端口占用
lsof -i :9000

# 杀掉进程
kill -9 <PID>
```

**错误：缺少依赖**
```bash
uv sync
# 或
pip install -r requirements.txt
```

### 无法连接

1. 检查服务是否运行：
   ```bash
   ps aux | grep main.py
   ```

2. 检查防火墙：
   ```bash
   # 开放端口
   sudo ufw allow 9000
   ```

3. 检查日志：
   ```bash
   tail -f logs/app.log
   ```

---

## 🔒 安全建议

### 生产环境部署

1. **使用反向代理**
   ```bash
   # Nginx 配置
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://localhost:9000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

2. **配置 HTTPS**
   ```bash
   # 使用 Let's Encrypt
   sudo certbot --nginx -d your-domain.com
   ```

3. **设置访问限制**
   - 配置防火墙规则
   - 使用 API Key 认证
   - 限制 IP 访问

---

## 📊 监控与日志

### 日志位置
```
/app/work/logs/bypass/app.log
```

### 查看实时日志
```bash
tail -f /app/work/logs/bypass/app.log
```

### 日志轮转
- 单文件最大：100MB
- 保留份数：5份

---

## 🔄 更新与维护

### 更新代码
```bash
git pull origin main
uv sync
# 重启服务
```

### 备份配置
```bash
# 备份配置
cp -r config/ config.backup/

# 备份数据
tar -czf backup.tar.gz data/ logs/
```

---

## 💡 常见问题

### Q: 如何修改开场白？
A: 编辑 `config/agent_llm_config.json` 中的 `sp` 字段，修改"用户第一次进来"的提示语。

### Q: 支持哪些岗位？
A: 当前支持测试开发、安全工程（渗透测试、安全架构等）两大领域。

### Q: 如何添加新岗位？
A: 在 `config/agent_llm_config.json` 的 `sp` 字段中添加新的岗位题库。

### Q: 服务支持多少人同时使用？
A: 默认单进程运行，生产环境建议使用负载均衡或多实例部署。

---

## 📞 获取帮助

- GitHub Issues: https://github.com/yan-124/yan/issues
- 提交新 Issue 获取支持

---

**版本**: 1.0.0  
**最后更新**: 2026-05-22

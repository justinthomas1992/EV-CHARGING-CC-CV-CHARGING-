# FreeLLMAPI

Docker Compose setup for [FreeLLMAPI](https://github.com/tashfeenahmed/freellmapi), an OpenAI-compatible proxy over free LLM providers.

```bash
cd freellmapi
cp .env.example .env
sed -i "s/^ENCRYPTION_KEY=.*/ENCRYPTION_KEY=$(openssl rand -hex 32)/" .env
docker compose up -d
```

- Dashboard: http://localhost:3001 (add provider keys on the Keys page)
- API: http://localhost:3001/v1 (Bearer token = the unified API key shown in the dashboard header)
- Health: http://localhost:3001/api/ping

`.env` is gitignored; never commit your encryption key.

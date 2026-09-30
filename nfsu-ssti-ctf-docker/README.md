# NFSU SSTI CTF Lab

Deliberately vulnerable Flask/Jinja2 Server-Side Template Injection lab.

Server: `172.16.11.52`  
Port: `8090`  
Student URL: `http://172.16.11.52:8090`

## Deploy

```bash
docker compose up -d --build
```

Verify:

```bash
docker compose ps
curl http://172.16.11.52:8090/health
```

## Intended vulnerability

The `/render` endpoint passes user-controlled `name` to Jinja's `render_template_string()`.

Harmless SSTI test:

```text
{{7*7}}
```

Expected result contains `49`.

The intended flag retrieval is:

```text
{{ config["CHALLENGE_FLAG"] }}
```

Keep this lab on an isolated training network.

# Agno agents

[Agno](https://docs.agno.com/introduction) is an incredibly fast multi-agent framework, runtime and control plane.

```bash
fastapi dev src/agno_agent/server1.py
fastapi dev --port 7777 src/agno_agent/server2.py
# or in DEBUG mode
AGNO_DEBUG=True fastapi dev src/agno_agent/server1.py
```

This would make it accessible via:
* REST API: http://127.0.0.1:8000/docs
* Agent OS Config: http://127.0.0.1:8000/config
* [Agno OS UI](https://docs.agno.com/agent-os/introduction): https://os.agno.com/
* [Agent UI](https://docs.agno.com/basics/agent-ui/overview): http://127.0.0.1:3000/

Alternatively, run directly with python:
```bash
PYTHONPATH=src python src/agno_agent/server2.py
# or
PYTHONPATH=src python -m agno_agent.server2
````
This would make it accessible via:
* REST API:http://127.0.0.1:7777/docs
* etc

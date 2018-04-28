server-run:
	PYTHONPATH='./src' python src/client_server/server.py

client-run:
	PYTHONPATH='./src' python src/client_server/client.py

set-up:
	pip install -r requirements.txt
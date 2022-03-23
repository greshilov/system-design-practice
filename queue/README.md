# queue

## Installation
Install docker-compose:  

https://docs.docker.com/compose/install/

Install deps:
```
pip install -r requirements.txt
```

## How to start

Start postgres and redis:
```
docker-compose up
```

Create all tables (run once until cleanup):
```
python schema.py
```

Run manager/UI:
```
python manager.py
```

Run worker:
```
python worker.py
```

## How to cleanup and remove all database data
```
docker-compose down
```

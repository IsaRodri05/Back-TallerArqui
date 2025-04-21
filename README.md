# Back-TallerArqui

First execute backend in docker:

```bash
docker compose build
docker compose up
```

Now products back is in  [http://localhost:8001](http://localhost:8001).

and analyst back is in [http://localhost:8000](http://localhost:8000).

Second connect to db_analyst with credentials in compose (this is only for development and testing) and run the SQL script in /BACK-TALLERARQUI/backAnalyst/table.sql
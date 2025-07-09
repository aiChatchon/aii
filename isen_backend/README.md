# ISEN Backend

This backend uses FastAPI and MySQL via SQLAlchemy to store orders from Shopee.
A background scheduler runs every 30 minutes to pull new orders (mocked).

## Environment Variables

- `MYSQL_URL` – SQLAlchemy connection string for MySQL

## Development

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

The scheduler starts automatically when the app runs.

## Docker

Build and run:

```bash
docker build -t isen-backend .
docker run -e MYSQL_URL=... -p 8080:8080 isen-backend
```

## Streamlit Dashboard

Run the dashboard connecting to the API:

```bash
streamlit run streamlit_app.py --server.port 8501
```

from projeto.celery import app


@app.task
def debug_task():
    print("Olá")

from celery import Celery
from app.model import Question
from app.utils.redis_client import RedisClient
from app.utils.config import env

app = Celery('tasks', broker=f'redis://default:sOmE_sEcUrE_pAsS@redis:6379/0')

@app.task
def add(x, y):
    print(x + y)


@app.task
def answer_question(q_dict: dict):
    q = Question(**q_dict)
    r = RedisClient(env=env)
    for chunk in ["hihi", "yoyo"]:
        r.publish(q.user_id, {"question": q.question, "chunk": chunk})
    


if __name__ == "__main__":
    app.worker_main(
        argv=[
            "worker",
            f"--autoscale=4",
            "--loglevel=info",
            "--queues",
            "agent",
        ]
    )
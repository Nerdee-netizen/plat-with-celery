from celery import Celery
from app.model import Question

app = Celery('tasks', broker='redis://default:sOmE_sEcUrE_pAsS@redis:6379/0')
if __name__ == "__main__":
    q = Question(user_id='13',
                 question="What is the capital of France?", 
                 answer="Paris", 
                 category="Geography", 
                 difficulty=1)
    app.send_task('tasks.answer_question', args=[q.model_dump()], queue='agent')
pip3 install celery

```python
from celery import Celery

app = Celery('task', broker='redis://127.0.0.1/0')
app.task
def reverse(string):
    return string[::-1]



```

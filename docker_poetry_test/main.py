from fastapi import FastAPI
from docker_poetry_test.shemas import Numbers
from docker_poetry_test.functions import sum_numbers

app = FastAPI()


@app.get('/sum')
def sum_num(numbers: Numbers):
    return sum_numbers(numbers.a, numbers.b)
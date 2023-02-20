from fastapi import FastAPI
from shemas import Numbers
from functions import sum_numbers

app = FastAPI()


@app.get('/sum')
def sum_num(numbers: Numbers):
    return sum_numbers(numbers.a, numbers.b)
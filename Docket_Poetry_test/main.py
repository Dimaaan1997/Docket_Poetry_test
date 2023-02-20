from fastapi import FastAPI
from Docket_Poetry_test.shemas import Numbers
from Docket_Poetry_test.functions import sum_numbers

app = FastAPI()


@app.get('/sum')
def sum_num(numbers: Numbers):
    return sum_numbers(numbers.a, numbers.b)
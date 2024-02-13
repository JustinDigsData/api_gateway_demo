from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumAdd(BaseModel):
    num1: int | float
    num2: int | float


@app.get('/get/helloworld')
async def get_helloworld():
    return {'message': 'Hello, world!'}


@app.post('/post/add')
async def post_add_numbers(nums: NumAdd):
    return {'num1': nums.num1, 
            'num2': nums.num2,
            'sum': nums.num1 + nums.num2
            }

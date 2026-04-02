from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('students.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def home():
    return{'message':'Student Managment System API'}


@app.get("/view")
def view():
    data = load_data()

    return data

@app.get('/student/{student_id}')
def search_student(student_id: str = Path(..., description='ID of the student in DB', examples='S001')):
    data = load_data()

    for student in data:
        if student["sid"] == student_id:
            return student
        
    raise HTTPException(status_code=404 ,detail='Student Not found')

@app.get('/sort')
def sort_students(
    sort_by: str = Query(..., description='Sort by course, age, enrollment_year'),
    order: str= Query('asc', description='asc or desc')):

    valid_fields = ['course', 'age', 'enrollment_year']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail = f'Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail= 'invalid order select between asc or desc')
    
    data = load_data()

    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=sort_order) 
    
    return sorted_data
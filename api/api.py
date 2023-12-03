from fastapi import FastAPI, HTTPException, status, Request
from typing import Optional
import json, random, time
from functools import wraps

"""
    Hello everyone, this is my first project in API. 
    The goal to create a API resume that return pieces of information when accessing the API
    
    # To run the app enter this command in the terminal
    # uvicorn main:app --reload to run the server 
    # main - is the name of the file py and app is the name of the variable in the main py
    # https://fastapi.tiangolo.com/#run-it
"""

MAX_LIMIT = 10
SECONDS = 60

# Reading the JSON data
with open ("./resume.json") as file:
    data = json.load(file)

app = FastAPI()

def rate_limited(max_calls: int, time_frame: int):
    """Limits the request on the API 

    Args:
        max_calls (int): Maximum number of calls allowed 
        time_frame (int): The time frame (in seconds) for which the limit is applied
    """
    
    def decorator(func):
        calls = []
        
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            now = time.time()
            calls_in_time_frame = [call for call in calls if call > now - time_frame]
            if len(calls_in_time_frame) >= max_calls:
                raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rates limit exceed")
            calls.append(now)
            return await func(request, *args, **kwargs)
        
        return wrapper
    
    return decorator

@app.get("/")
@rate_limited(max_calls=MAX_LIMIT, time_frame=SECONDS)
async def read_root(request: Request):
    return {"message": "Welcome to my API Resume"}

@app.get("/random")
@rate_limited(max_calls= MAX_LIMIT, time_frame=SECONDS)
async def read_random(request: Request):
    num = random.randint(0, len(data)-1)
    if num > len(data):
        return {"message": "Data was out of range!"}
    return list(data.values())[num]

@app.get("/resume")
@rate_limited(max_calls= MAX_LIMIT, time_frame=SECONDS)
async def read_resource(request: Request, type: Optional[str] = None):
    """ Route that returns a data.
    Args:
        type (str): Optional defaults to None, type = [ info, socials, license, skills, projects, certifications, about-me ]
    Returns:
        array: returns an array of data. can be futher access using its id to return its value
    """
    if not type:
        return {"resume": data}  
    
    if type in data:
        return { type: data[type]}
    return {"message": "This type doesn't exist"}

# Sections of the API with filters

@app.get("/work-exp")
@rate_limited(max_calls= MAX_LIMIT, time_frame=SECONDS)
async def work_exp(request: Request, exp_id: Optional[int] = None):
    if not exp_id:
        return {"work-experience": data["work-experience"]}
    
    for work in data["work-experience"]:
        if exp_id == work["id"]:
            return { "work-experience": work}
    return { "message": f"Id {exp_id} doesn't exist!"}
    

@app.get("/filter-project")
@rate_limited(max_calls= MAX_LIMIT, time_frame=SECONDS)
async def read_proj(request: Request, project_id: Optional[int] = None):
    if not project_id:
        return {"projects": data["projects"]}
    
    for project in data["projects"]:
        if project_id == project["id"]:
            return {"project": project}
    return { "message": f"Id number {project_id} doesn't exist!"}
    

@app.get("/filter-cert")
@rate_limited(max_calls= MAX_LIMIT, time_frame=SECONDS)
async def read_cert(request: Request, cert_id: Optional[int] = None):
    if not cert_id:
        return {"certifications": data["certifications"] }
    
    for cert in data["certifications"]:
        if cert_id == cert["id"]:
            return {"certification": cert}
    return { "message": f"Id number {cert_id} doesn't exist!"}
    

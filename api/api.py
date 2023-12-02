from fastapi import FastAPI
from typing import Optional
import json, random

"""
    Hello everyone, this is my first project in API. 
    The goal to create a API resume that return pieces of information about who accesses the API
    
    # To run the app enter this command in the terminal
    # uvicorn main:app --reload to run the server 
    # main - is the name of the file py and app is the name of the variable in the main py
    # https://fastapi.tiangolo.com/#run-it
"""

# Reading the JSON data
with open ("./resume.json") as file:
    data = json.load(file)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to my API Resume"}

@app.get("/random")
async def read_random():
    num = random.randint(0, len(data)-1)
    if num > len(data):
        return {"message": "Data was out of range!"}
    return list(data.values())[num]

@app.get("/resume")
async def read_resource(type: Optional[str] = None):
    """ Route that returns a data.
    Args:
        type (str): Optional defaults to None, type = [ info, socials, license, skills, projects, certifications, about-me ]
    Returns:
        array: returns an array of data. can be futher access using its id to return its value
    """
    if not type:
        return {"message": "This type doesn't exist"}  
    
    if type in data:
        return { type: data[type]}
    return {"message": "This type doesn't exist"}

# Sections of the API with filters

@app.get("/work-exp")
async def work_exp(exp_id: Optional[int] = None):
    if not exp_id:
        return {"work-experience": data["work-experience"]}
    
    for work in data["work-experience"]:
        if exp_id == work["id"]:
            return { "work-experience": work}
    return { "message": f"Id {exp_id} doesn't exist!"}
    

@app.get("/filter-project")
async def read_proj(project_id: Optional[int] = None):
    if not project_id:
        return {"projects": data["projects"]}
    
    for project in data["projects"]:
        if project_id == project["id"]:
            return {"project": project}
    return { "message": f"Id number {project_id} doesn't exist!"}
    

@app.get("/filter-cert")
async def read_cert(cert_id: Optional[int] = None):
    if not cert_id:
        return {"certifications": data["certifications"] }
    
    for cert in data["certifications"]:
        if cert_id == cert["id"]:
            return {"certification": cert}
    return { "message": f"Id number {cert_id} doesn't exist!"}
    

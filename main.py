from fastapi import FastAPI
import json
import random

"""
    Hello everyone, this is my first project in API. 
    The goal to create a API resume that return pieces of information about who accesses the API
    
"""

# To run the app enter this command in the terminal
# uvicorn main:app --reload to run the server 
# main - is the name of the file py and app is the name of the variable in the main py
# https://fastapi.tiangolo.com/#run-it
# Reading the JSON data
# Accessing the dictionary in the list
# print(list(data.values())[0])

with open (".public/resume.json") as file:
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
async def read_resource(type: str | None = None):
    """ Route that returns a data.

    Args:
        type (str): Optional
            info
            socials
            license
            skills
            projects
            certifications
            about-me

    Returns:
        array: returns an array of data. can be futher access using its key to return its value
    """
    if type:
        if type in data:
            return { type: data[type]}
        return {"message": "This type doesn't exist"}
    return { "resume": data }
    # return { "message": "The information doesn't exist"}

# Sections of the API with filters

@app.get("/work-exp")
async def work_exp(exp_id: int | None = None):
    if exp_id:
        for work in data["work-experience"]:
            if exp_id == work["id"]:
                return { "work-experience": work}
        return { "message": f"Id {exp_id} doesn't exist!"}
    return {"work-experience": data["work-experience"]}

@app.get("/filter-project")
async def read_proj(project_id: int | None = None):
    if project_id:
        for project in data["projects"]:
            if project_id == project["id"]:
                return {"project": project}
        return { "message": f"Id number {project_id} doesn't exist!"}
    return {"projects": data["projects"]}

@app.get("/filter-cert")
async def read_cert(cert_id: int | None = None):
    if cert_id:
        for cert in data["certifications"]:
            if cert_id == cert["id"]:
                return {"certification": cert}
        return { "message": f"Id number {cert_id} doesn't exist!"}
    return {"certifications": data["certifications"] }
# @app.get("/filter")
# async def read_filter(type: str, id: int | None = None):
#     if type:
#         if id:
#             return { type: data[type]}
#         else:
#             for item in data[type]:
#                 if id == item["id"]:
#                     return { type: item}
#         return { "message": f"Id number {id} in {type} doesn't exist!"}    
        
#     else:
#          return { "message": "Please enter the type to filter" }   
        
    
# def check_id(type, item_id):
#     if item_id == None:
#         return True
#     else:
#         for item in data[type]:
#             if item_id == item["id"]:
#                 return {"certification": item}
#         return { "message": f"Id number {item_id} in {type} doesn't exist!"}


# Testing github uploading my first project

# import uvicorn

# if __name__ == "__main__":
#   uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)
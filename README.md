# API Resume Documentation

## Description
Hello, This is my API Resume. This is my project that I created while learning coding with Python. The goal is to implement the REST and create a simply API that returns JSON data using my Resume. 

## Usage

### Get a Random Information

Returns a randomly selected information from the resume.

<strong>Example Request:</strong>
```
https://api-resume-flores.vercel.app/random
```

<strong>Example Response:</strong>
```json
{
    "name": "Eiron Ross Flores",
    "contact": "09494780589",
    "address": "Angat, Bulacan",
    "email": "eironflores27@gmail.com",
    "education": [
        {
            "school": "Pamantasan ng Lungsod ng Manila",
            "degree": "Bachelor of Science in Electrical Engineering",
            "date-graduated": "April 2018",
            "is-graduated": "True"
        }
    ]
}
```

### Filter Resume

Returns part of the resume filtered by type

<li>
          type (Optional): Filter by type. Choice of <code>info</code>,
          <code>work-experience</code>, <code>skills</code>,
          <code>socials</code>, <code>license</code>,
          <code>certifications</code>, <code>projects</code>,
          <code>about-me</code>
</li>
<br/>

<strong>Example Request:</strong>
```
https://api-resume-flores.vercel.app/resume?types=socials
```

<strong>Example Response:</strong>
```json
{
    "socials": {
        "linkedin": "https://linkedin.com/in/eironross",
        "github": "https://github.com/eironross"
    }
}
```

### Filter Work Experience

Returns a list of work experience can be filtered by id

<li>exp_id (Optional): Filter by id. Choice of 1</li>
<br/>

<strong>Example Request</strong>
```
https://api-resume-flores.vercel.app/work-exp?exp_id=1
```


<strong>Example Response</strong>
```json
{
    "work-experience": {
        "id": 1,
        "job": {
            "position": "Assistant Energy Trader",
            "company": "GNPower Kauswagan Ltd. Co.",
            "address": "Mariveles, Bataan",
            "job-descriptions": {
                "item-1": "Built a Market Data downloader using Python via Selenium to save time in gathering data.",
                "item-2": "Created a Reporting Program using Excel VBA, reduced time in creating reports",
                "item-3": "Built a market data compiler using Python to be used in compiling data and analysis",
                "item-4": "Monitors the Real-Time Dispatch, Compliances, and Market Prices in MPI.",
                "item-5": "Submission of documents for the Reportorial Requirements and Compliance Post-Evaluation Management Systems (CPEMS).",
                "item-6": "Assist in coordinating with the Operations & Maintenance (O&M), Market Operators, and System Operators and preparation of any-trading related data and documents",
                "item-7": "Assist in coordination with the Buyers on their Nomination (Daily, Weekly, Monthly, and Realtime)."
            },
            "start-date": "March 19, 2018",
            "end-start": "August 31, 2023",
            "years-accumulated": "4.5 years",
            "currently-at-the-company": "False"
        }
    }
}
```

### Filter Projects

Returns a list of projects can be filtered by id.

<li>project_id (Optional): Filter by id. Choice of 1 to 5</li>
<br/>

<strong>Example Request</strong>
```
https://api-resume-flores.vercel.app/filter-project?project_id=1
```

<strong>Example Response</strong>
```json
{
    "project": {
        "id": 1,
        "project-name": "API Resume",
        "description": "An API based resume which can returns info of my resume base on the request from the client",
        "tech": "FastAPI",
        "created-year": "2023"
    }
}
```

### Filter Certifications

Returns a list of certifications can be filtered by id

<li>cert_id (Optional): Filter by id. Choice of 1 to 4  
</li>
<br/>

<strong>Example Request</strong>
```
https://api-resume-flores.vercel.app/filter-cert?cert_id=1
```

<strong>Example Response</strong>
```json
{
    "certification": {
        "id": 1,
        "title": "100 Days of Code: The Complete Python Pro Bootcamp for 2023",
        "issued-by": "Udemy",
        "issued-date": "November 2023",
        "credential-id": "UC-25955a6a-cce4-41cb-8f22-7d4a48dbab0e"
    }
}
```


## Project Status

The API project can be improve by adding proper routing, query parameters, and improving the structure of the JSON data.

## Author

Created by Eiron Ross Flores. \
November 2023

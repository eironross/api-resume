import uvicorn
from os import getenv

if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    uvicorn.run("api.api:app", host="127.1.1.1", port=port, reload=True)
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from random import randint

app = FastAPI()

@app.get("/create_names/{number_of_names}")
def create_names(number_of_names: int):
    f = open('./names.txt', 'r')
    lines = f.readlines()
    names_lst = []
    for i in range(0, number_of_names):
        # Get prefix
        prefix_idx = randint(0, len(lines) - 1)
        prefix = lines[prefix_idx].split('.')[-1].strip()

        # Get suffix
        suffix_idx = randint(0, len(lines) - 1)
        suffix = lines[suffix_idx].split('.')[-1].strip()

        names_lst.append(prefix + suffix)

    return JSONResponse(names_lst)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
from fastapi import FastAPI

app = FastAPI()


@app.get("/vtuber/general/{vtuber_id}")
async def general_info(vtuber_id: str):
  result = vtuber_id
  return(result)
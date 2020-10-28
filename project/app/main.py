from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import getdata


app = FastAPI(
    title='Labs 28 Human Rights First-B DS API',
    description='Returns police incident data in JSON format.',
    version='0.6',
    docs_url='/',
)

app.include_router(getdata.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

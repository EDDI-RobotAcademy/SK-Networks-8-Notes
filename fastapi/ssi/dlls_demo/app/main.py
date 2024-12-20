from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os

from config.cors_config import CorsConfig
from ensemble_method.controller.ensemble_method_controller import ensembleMethodRouter
from feature_engineering.controller.feature_engineering_controller import featureEngineeringRouter

load_dotenv()

app = FastAPI()

CorsConfig.middlewareConfig(app)
#APIRouter로 작성한 Router를 
app.include_router(featureEngineeringRouter)
app.include_router(ensembleMethodRouter)


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
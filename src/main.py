import uvicorn

# noinspection PyPackageRequirements
from decouple import config

if __name__ == "__main__":
    uvicorn.run(
        config("APP_PATH"), host=config("HOST"), port=config("PORT"), reload=True
    )

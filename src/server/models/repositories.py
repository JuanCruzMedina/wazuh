from pydantic import BaseModel, Field


class GetAllResult(BaseModel):
    """
    Class that represents the result of getting a list of items from a repository.
    """

    total_items: int = Field(default=0, ge=0)
    data: list = Field(default=[])

    class Config:
        schema_extra = {
            "total_items": 28,
            "data": [
                {"user_id": 1, "id": 4, "title": "et porro tempora", "completed": True},
                {
                    "user_id": 1,
                    "id": 15,
                    "title": "ab voluptatum amet voluptas",
                    "completed": True,
                },
                {
                    "user_id": 1,
                    "id": 16,
                    "title": "accusamus eos facilis sint et aut voluptatem",
                    "completed": True,
                },
            ],
        }

    def __init__(self, **data):
        """
        Initialize the object with only the data attribute, to calculate the total_items property based on it
        :param data: data collection
        """
        data["total_items"] = len(data.get("data", []))
        super().__init__(**data)

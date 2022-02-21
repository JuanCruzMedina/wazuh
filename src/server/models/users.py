from pydantic import BaseModel


class Geo(BaseModel):
    """
    Class representing a geographic Coordinate.
    """
    lat: float
    lng: float

    class Config:
        schema_extra = {
            "lat": "-37.3159",
            "lng": "81.1496"
        }


class Address(BaseModel):
    """
    Class that represents an address.
    """
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo

    class Config:
        schema_extra = {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }}


class Company(BaseModel):
    """
    Class that represents a company.
    """

    name: str
    catchPhrase: str
    bs: str

    class Config:
        schema_example = {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }


class User(BaseModel):
    """
    Class that represents a user.
    """

    id: int
    name: str
    username: str
    email: str
    address: Address
    website: str
    company: Company

    class Config:
        schema_example = {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }

# WAZUH

---

Resolution of technical evaluation

## Technologies

- **Python** >= 3.9 
- Uvicorn
- FastApi
- Requests
- Python Decouple
- **Code formatter**: Black

## Instructions

**Run the api**

- Create virtual environment
- Install dependencies on virtual environment
- Activate virtual environment
- In terminal:
```commandline
uvicorn src.server.app:app -reload
```

**For run the main.py file**
- Copy the example file '.env_example' as '.env' at the project level.
- Sets the value corresponding to the variables.
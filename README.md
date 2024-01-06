# Taptic - Interview Assistant

## Installation
Create and activate a virtual environment in the project's root directory using: 
```
$ python3 -m venv venv
$ source venv/bin/activate
```
If you're on Windows, you might be able to create a virtual environment using the following commands in the command line 
```
$ python -m venv venv 
$ venv\Scripts\activate.bat
```

Install the relevant packages using
```
$ pip install -r requirements.txt
````
If that does not work, use
```
$ python3 -m pip install -r requirements.txt
```
## Running the app
Go to `secret_key.py` and and replace `openapi_key` with your own OpenAI API key:
```
openapi_key = "" # replace this with your own key, say "sk-assdfdsfdsgd"
serpapi_key = ""
```

Start the app using
```
$ streamlit run main.py
```
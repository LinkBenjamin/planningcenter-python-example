# How to use this repository

I'm assuming that you already have python installed on your computer.  Any python 3.x should work, but I've personally tested with 3.12.4.

1. Set up your venv.
    - `python -m venv .venv`
    - `source .venv/bin/activate` (or `source .venv/Scripts/activate` in Windows Python)
2. Install dependencies.
    - `pip install -r requirements.txt`
3. Create a `keys.py` file in your project root folder.
4. In `keys.py`, create two string variables (get their contents from the project doc on the "General Info" tab):
    - `CLIENT_ID =`
    - `SECRET =`
5. Now you should be able to run `python main.py` and you should get back the results of the api call!


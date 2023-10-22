# Weather App.
 Built Using 
 - ReactJS
 - Django
 - DjangoRestFramework
 - Openweather API

## Setup Guidelines

- Clone the repository.
- create .env file and copy the keys from `.env.example`. You will need the API key from https://openweather.org. Fill the relevant DB values with the keys.
- create a virtual python environment and install the neccessary packages using the given `src/requirements.txt`
- cd into src.
- run the command `python3 manage.py migrate`
- After successful migration, start the server using `python3 manage.py runserver`
- The website should be available at http://127.0.0.1:8000/
- Start entering correct city names and see the Weather!

## Challenges I faced while creating this project


## Snapshot of the App
![image](./src/frontend/src/assets/Screenshot%202023-10-22%20194310.png)
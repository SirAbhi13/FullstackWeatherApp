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
- Install the node modules. cd into `src/frontend`. Use the command `npm install`.
- After successful migration, start the server using `python3 manage.py runserver`
- The website should be available at http://127.0.0.1:8000/
- Start entering correct city names and see the Weather!

## Challenges I faced while creating this project

### Frontend
- Since I had never learned or used JS before, making the frontend for this project was a big challenge.
- I was able to make something but a lot of things could be improved and there are concepts that I haven't even touched.
- I learned about states and how a frontend is able to process data from backend.

### Backend
- Tried to follow a modular approach to break the api and the data part into different apps.
- Since the function was to make a basic api call, there was no need for supplement files and logic was handled in views itself.
- In my attempt to make it the most polished app, I tried few things as packaging the project, integrating sessions, but was out of depth of my knowledge to achieve those.
- Designing this app was helpful as it helped me identify pain points and where I can improve more.

## Snapshot of the App
![image](./src/frontend/src/assets/Screenshot%202023-10-22%20194310.png)
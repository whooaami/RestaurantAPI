# INFORCE PYTHON TASK

Restaurant service using Django REST framework.

## Client server logic

<img width="694" alt="client-server" src="https://user-images.githubusercontent.com/86779145/233807174-c14ab08f-e158-4d87-995d-ba2378052e51.png">

## Database architecture 

<img width="779" alt="db" src="https://user-images.githubusercontent.com/86779145/233808120-fc2feea5-d9ba-4db3-bfd3-f03a90f6c5f2.png">

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. 

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/v1/employee` | GET | READ | Get all employees
`api/v1/employee/<int:pk>` | GET | READ | Get a single employee
`api/v1/employee`| POST | CREATE | Create a new employee
`api/v1/employee/<int:pk>` | PUT | UPDATE | Update a employee
`api/v1/employee/<int:pk>` | DELETE | DELETE | Delete a employee
`api/v1/menu` | GET | READ | Get all menus
`api/v1/menu/<int:pk>` | GET | READ | Get a single menu
`api/v1/restaurant/<int:pk>/menus/`| POST | CREATE | Upload a new menu for restaurant
`api/v1/restaurant/<int:restaurant_id>/menu/` | GET | READ | Get current day menu
`api/v1/menu/<int:pk>` | PUT | UPDATE | Update a meu
`api/v1/menu/<int:pk>` | DELETE | DELETE | Delete a menu
`api/v1/restaurant` | GET | READ | Get all restaurants
`api/v1/restaurant/<int:pk>` | GET | READ | Get a single restaurant
`api/v1/restaurant/`| POST | CREATE | Create a new restaurant
`api/v1/restaurant/<int:pk>` | PUT | UPDATE | Update a restaurant
`api/v1/restaurant/<int:pk>` | DELETE | DELETE | Delete a restaurant
`api/v1/votes/<int:menu_id>/results/` | GET | READ | Get results for current day

## Installation

1) Clone my [repository](https://github.com/whooaami/RestaurantAPI) to install project:

```bash
git clone https://github.com/whooaami/RestaurantAPI
```

2) Open this project in your IDE.

3) Create virtual environment:
```bash
python3.9 -m venv .venv
```

4) Activate virtual environment:
```bash
source .venv/bin/activate
```

5) Install all required libraries:
```bash
pip install -r requirements.txt
```

6) To run server:
```bash
python manage.py runserver
```

7) To run tests:
```bash
pytest
```
8) To run docker:
```bash
docker-compose -d --build
```

9) To make migrations on docker:
```bash
docker-compose exec web python manage.py migrate --noinput
```

## Use
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation), or we can use [Postman](https://www.postman.com/)

First, we have to start up Django's development server.
```
python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
http  http://127.0.0.1:8000/api/v1/employee/
```
we get:
```
{
    "detail": "Authentication credentials were not provided."
}
```
Instead, if we try to access with credentials:
```
http http://127.0.0.1:8000/api/v1/movies/3 "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
```
we get the employee with id = 3

## Create users and Tokens

First we need to create a user, so we can log in
```
http POST http://127.0.0.1:8000/api/v1/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```

After we create an account we can use those credentials to get a token

To get a token first we need to request
```
http http://127.0.0.1:8000/api/v1/auth/token/ username="username" password="password"
```
after that, we get the token
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA2MjIxLCJqdGkiOiJjNTNlNThmYjE4N2Q0YWY2YTE5MGNiMzhlNjU5ZmI0NSIsInVzZXJfaWQiOjN9.Csz-SgXoItUbT3RgB3zXhjA2DAv77hpYjqlgEMNAHps"
}
```
We got two tokens, the access token will be used to authenticated all the requests we need to make, this access token will expire after some time.
We can use the refresh token to request a need access token.

requesting new access token
```
http http://127.0.0.1:8000/api/v1/auth/token/refresh/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA"
```
and we will get a new access token
```
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
}
```

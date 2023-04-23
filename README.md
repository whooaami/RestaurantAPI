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

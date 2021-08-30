### Paranuara Challenge
Paranuara is a class-m planet. Those types of planets can support human life, for that reason, the president of Checktoporov decides to send
some people to colonize this new planet and
reduce the number of people in their own country. After 10 years, the new president wants to know how the new colony is growing and wants
some information about his citizens. Hence he hired you to build a rest API to provide the desired information.
The government from Paranuara will provide you two JSON files (located in the resource folder) which will provide information about all the
citizens in Paranuara (name, age, friends list, fruits and vegetables they like to eat...) and all founded companies on that planet.
Unfortunately, the systems are not that evolved yet, thus you need to clean and organize the data before use.
For example, instead of providing a list of fruits and vegetables their citizens like, they are providing a list of favorite food, and you will need to
split that list (please, check below the options for fruits and vegetables).

New Features

Your API must provide these endpoints:
Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any
employees.
Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common who have brown eyes and
are still alive.
Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: {"username":
"Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}

Delivery

Your solution must provide tasks to install dependencies, build the system and run. Solutions that do not fit these criteria will not be accepted as
a solution. Assume that we have already installed in our environment Java, Ruby, Node.js, Python, MySQL, MongoDB, and Redis; any other
technologies required must be installed in the install dependencies task. Moreover well tested and designed systems are one of the main criteria
of this assessment

Evaluation criteria

- Solutions written in Python would be preferred.
- Installation instructions that work.
- During installation, we may use different companies.json or people.json files.
- The API must work.
- Tests


### How to install
- Install docker

- Install docker-compose

### How to run
```docker-compose build```

```docker-compose up```


### How to populate see data
```docker-compose run app python manage.py populate_companies```

```docker-compose run app python manage.py populate_people```

Need to populate companies first

### How to replace seed data
Please replace resources/companies.json or people.json before running `docker-compose build`


### How to test
```docker-compose run app python manage.py test```

### API documentation
Browse http://localhost:8000/swagger/ for api testing


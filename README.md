# Python Back-end Assignment: Movie List

## The task
The task is to write a Python application which serves a page on localhost:8000/movies/. This
page should contain a plain list of all movies from the Ghibli API. For each movie the people that
appear in it should be listed.

## Requirements
The application is running on Python 3.8.5 using the Django 3.1 framework. 
The external lib requests 2.24 is also required.

## Running the app
First, the installation ob the above libraries is required. 
Then, you can active the endpoint by accessing the movie_list document and run the command:

```python manage.py runserver```

Then, by going with your browser to localhost:8000/movies/, you should see the required list.

## Tests
Among others, the following tests were performed:
- Herokuapp's server response has a different status code than 200
- The last time the page was loaded was more/less then a minute ago
- Herokuapp's server response contains characters/movies that already exist at our database
- Deletion of exist movie/character at our database before accessing the page

## Future tests
- Accessing the page with different timezones
- Get contradicting information from Herokuapp's server 
- Scalability test

## Final notes
- Some console logs were added and are written in the console
- the setting DEBUG is set to True for your convenience
- the admin username is 'admin' as well as the password
from django.shortcuts import render
import requests
from .models import Film, Person, LastUpdated
import datetime
import logging


def film_people_list(request):
    """Main function. Activated when entering the url"""
    logging.getLogger().setLevel(logging.INFO)
    check_flag = check_last_updated()
    if check_flag:
        get_films()
        get_people()
    return render(request=request,
                  template_name="main/home.html",
                  context={"films": Film.objects.all})


def get_films():
    """getting films data from the external server"""
    logging.info("Fetching films info from external server")
    try:
        r = requests.get('https://ghibliapi.herokuapp.com/films')
    except ConnectionError as e:
        logging.warning("Fail fetching films data from server: " + e)
        return
    if not r.status_code == 200:
        logging.warning("Fail fetching films data from server. status code: " + str(r.status_code))
        return
    logging.info("Films info fetched successfully")
    for film in r.json():
        heroku_id = film['id']
        title = film['title']
        if not Film.objects.filter(heroku_id__exact=heroku_id):
            new_q = Film(heroku_id=heroku_id, title=title)
            new_q.save()
            logging.info('the movie ' + title + ' was added')
    return


def get_people():
    """getting characters data from the external server"""
    logging.info("Fetching characters info from external server")
    try:
        r = requests.get('https://ghibliapi.herokuapp.com/people')
    except ConnectionError as e:
        logging.warning("Fail fetching characters data from server: " + e)
        return
    if not r.status_code == 200:
        logging.warning("Fail fetching characters data from server. status code: " + str(r.status_code))
        return
    logging.info("Characters info fetched successfully")
    for person in r.json():
        heroku_id = person['id']
        name = person['name']
        films = person['films']
        if not Person.objects.filter(heroku_id__exact=heroku_id):
            person_in_db = Person(heroku_id=heroku_id, name=name)
            person_in_db.save()
            logging.info('the character ' + name + ' was added')
        else:
            person_in_db = Person.objects.filter(heroku_id__exact=heroku_id)[0]
        for film in films:
            film_id = film.rsplit('/films/', 1)[-1]
            film_in_db = Film.objects.filter(heroku_id__exact=film_id)
            if not film_in_db:
                logging.warning('warning. film id' + film_id + 'Does not exist')
            if person_in_db not in film_in_db[0].person_set.all():
                person_in_db.films.add(film_in_db[0])
    return


def check_last_updated():
    """checking if the last update time of the internal db was over a minute ago"""
    if not LastUpdated.objects.all():
        LastUpdated.objects.create(time = datetime.datetime.now())
    last_updated = LastUpdated.objects.get(pk=1)
    last_updated_utc = last_updated.time.replace(tzinfo=None)
    time_diff_sec = (datetime.datetime.utcnow() - last_updated_utc).total_seconds()
    logging.info("Last time updated: " + str(time_diff_sec) + " seconds ago")
    if time_diff_sec > 60:
        last_updated.save()
        return True
    else:
        return False

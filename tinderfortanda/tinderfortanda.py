import json
from collections import defaultdict
from typing import DefaultDict, List

venues = []

people = []

swiperinos: DefaultDict[int, List[int]] = defaultdict(list)

approved_users: DefaultDict[int, List[int]] = defaultdict(list)

def load():
    venues.append(dict(
        id=1,
        name='Lucky Egg',
        location=' 27 Warner St, Fortitude Valley',
        wage='$24/hr',
        hours='5pm - 9pm',
        description='Front of House'
    ))
    venues.append(dict(
        id=2,
        name='The Met',
        location=' 256 Wickham St, Fortitude Valley',
        wage='$27/hr',
        hours='12am - 3am',
        description='Bartender'
    ))
    venues.append(dict(
        id=3,
        name='West End Charcoal',
        location=' 56 Russell St, West End',
        wage='$29/hr',
        hours='7pm - 11pm',
        description='Bartender'
    ))
    venues.append(dict(
        id=4,
        name='The Wickham',
        location=' 308 Wickham St, Fortitude Valley',
        wage='$27/hr',
        hours='1am - 4am',
        description='Bartender'
    ))
    venues.append(dict(
        id=5,
        name='Bloodhound Bar',
        location=' 454 Brunswick St, Fortitude Valley ',
        wage='$31/hr',
        hours='11pm - 4am',
        description='Bartender'
    ))

    people.append(dict(
        id=101,
        name='Bennyflick Coppersplash',
        photo='http://benedictcumberbatch.co.uk/wordpress/wp-content/gallery/spencer-hart-samsung-galaxy-note-party/spencer-hart-samsung-hq3.jpg',
        pay_range='$700/hr - $750/hr',
        hours='5 - 7',
        location='Fortitude Valley',
        experience='Face painter'
    ))

    people.append(dict(
        id=102,
        name='Milly Blob',
        photo='https://s-media-cache-ak0.pinimg.com/originals/0a/b9/53/0ab953a8e043745e762df743da98b88b.jpg',
        pay_range='$20/hr - $30/hr',
        hours='3 - 5',
        location='Brisbane',
        experience='Bartender',
    ))

    people.append(dict(
        id=103,
        name='Sam Pumpernickle',
        photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlxA_iNoxGGM3NxIXfmJkMkelqcnU1NEeGWf8U7luYm1n0knDRlQ',
        pay_range='$20/hr - $30/hr',
        hours='4 - 6',
        location='Brisbane',
        experience='Bartender',
    ))
    people.append(dict(
        id=104,
        name='Tom Cruise',
        photo='https://media1.popsugar-assets.com/files/thumbor/D8_H1hKqyOkHP2sMvJV4kXmXurg/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2010/07/27/4/192/1922398/60992755/i/Pictures-Tom-Cruise-Cameron-Diaz-Promoting-Knight-Day-Mexico-City.jpg',
        pay_range='$20/hr - $30/hr',
        hours='4 - 6',
        location='Brisbane',
        experience='Bartender',
    ))
index = 0

pindex = 0


def is_venue(id):
    return id <= 100


def get_next_venue(user_id):
    global index

    index += 1
    return json.dumps(venues[index % len(venues)])


def get_next_person(venue_id):
    global pindex
    pindex += 1
    user_list= swiperinos[venue_id]
    if len(user_list)==0:
        return '{"message"="none"}'
    return json.dumps(user_list[pindex % len(user_list)])


def swipe_right(my_id, id):
    if is_venue(my_id):
        approved_user_list = approved_users[id]
        approved_user_list.append(my_id)
        approved_users[id] = approved_user_list

    else:
        user_list = swiperinos[id]
        user_list.append(my_id)
        swiperinos[id] = user_list ## adding a person to the list of people who have swiped right to the venue


def swipe_left(my_id, id):
    pass

def get_matched_venues(id):
    return json.dumps(approved_users[id])
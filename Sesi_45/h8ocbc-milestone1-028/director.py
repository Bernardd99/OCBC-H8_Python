"""
This is the director module and supports all the REST actions for the
director data
"""

from flask import make_response, abort
from config import db
from models import Director, DirectorSchema, Movie

def read_all():
    """
    This function responds to a request for /api/director
    with the complete lists of director
    :return:        json string of list of director
    """
     # Create the list of people from our data
    director = Director.query.order_by(Director.id).limit(10)

    # Serialize the data for the response
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data

def read_one(id):
    """
    This function responds to a request for /api/director/{id}
    with one matching director from people
    :param id:   Id of director to find
    :return:            director matching id
    """
    # Build the initial query
    director = (
        Director.query.filter(Director.id == id)
        .outerjoin(Movie)
        .one_or_none()
    )

    # Did we find a director?
    if director is not None:

        # Serialize the data for the response
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"Director not found for Id: {id}")

def create(director):
    """
    This function creates a new director in the director structure
    based on the passed in director data
    :param director:  director to create in director structure
    :return:        201 on success, 406 on director exists
    """

    name = director.get("name")
    uid = director.get("uid")

    existing_director = (
        Director.query
        .filter(Director.uid == uid)
        .one_or_none()
    )

    # Can we insert this director?
    if existing_director is None:

        # Create a director instance using the schema and the passed in director
        schema = DirectorSchema()
        new_director = schema.load(director, session=db.session)

        # Add the director to the database
        db.session.add(new_director)
        db.session.commit()

        # Serialize and return the newly created director in the response
        data = schema.dump(new_director)

        return data, 201

    # Otherwise, nope, director exists already
    else:
        abort(409, f"Director {name} with {uid} exists already")

def update(id, director):
    """
    This function updates an existing person in the people structure
    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    # Get the person requested from the db into session
    update_director = Director.query.filter(
        Director.id == id
    ).one_or_none()

    # Did we find an existing person?
    if update_director is not None:

        # turn the passed in person into a db object
        schema = DirectorSchema()
        update = schema.load(director, session=db.session)

        # Set the id to the person we want to update
        update.id = update_director.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_director)

        return data, 200

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Person not found for Id: {id}")

def delete(id):
    """
    This function deletes a person from the people structure
    :param person_id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    director = Director.query.filter(Director.id == id).one_or_none()

    # Did we find a person?
    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(f"Director {id} deleted", 200)

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Director not found for Id: {id}")

def read_all_directing():
    """
    This function responds to a request for /api/director/directing
    with the complete lists of director in Directing department
    :return:        json string of list of director in Directing department
    """
     # Create the list of people from our data
    director = Director.query.filter(Director.department == "Directing").order_by(Director.id).limit(5)

    # Serialize the data for the response
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data

def read_all_gender():
    """
    This function responds to a request for /api/director/gender
    with the complete lists of director with 2 as a gender
    :return:        json string of list of director with 2 as a gender
    """
     # Create the list of people from our data
    director = Director.query.filter(Director.gender == 2).order_by(Director.id).limit(5)

    # Serialize the data for the response
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data
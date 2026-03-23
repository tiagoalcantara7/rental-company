import logging


def has_permission(x) -> bool:
    """This function is responsible for validating the user's option"""

    logging.debug("Starting validation to find out if the user is an adult")

    while x != "y" and x != "n":
        logging.warning("User placing an invalid option")

        print("Invalid option")
        x = input("Do you have parental permission? y/n: ").lower().strip()

    if x == "y":
        logging.info("client has parental permission ✅")

        return True

    logging.warning("the client does not have parental consent")
    return False


def finalize_film_transaction(obj):
    """This function is responsible for completing the film rental process"""

    logging.info("Finalizing the film transaction")

    return f"""

Movie: {obj.name}
Price: ${obj.price:.2f}
Expiration: {obj.expiration} days
Rating: {obj.rating}
Duration: {obj.duration} minutes \n
You rented the movie {obj.name}, return it in {obj.expiration} days

"""


def finalize_show_transaction(obj):
    """This function is responsible for completing the series rental process"""

    logging.info("Finalizing the show transaction")

    return f"""

TV Show: {obj.name}
Price: ${obj.price:.2f}
Expiration: {obj.expiration} days
Rating: {obj.rating}
Seasons: {obj.seasons} Seasons \n
You rented the series {obj.name}, return it in {obj.expiration} days

"""

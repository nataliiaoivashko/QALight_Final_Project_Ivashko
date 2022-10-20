import datetime
import logging
import random
import string
from time import sleep


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_num_len(frn=1, ton=9):
    """Generate random number"""
    return str(random.randint(frn, ton))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout=5, period=0.5):
    """Reties until OK"""

    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.error(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_decorator(original_function):
    """Logging actions using docstrings"""

    log = logging.getLogger("[LogDecorator]")

    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        log.info(f"{original_function.__doc__}")
        return result

    return wrapper


class User:

    def __init__(self, firstname="", lastname="", email="", password="", confirm_password=""):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def fill_data(self, firstname="", lastname="", email="", password="", confirm_password=""):
        """Fill user with sample data and values if provided"""
        # random_user from conftest file
        user = random_str()
        self.firstname = f"{user}{random_num()}" if not firstname else firstname
        self.lastname = f"{user}{random_num()}" if not lastname else lastname
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password
        self.confirm_password = self.password if not confirm_password else confirm_password

    def fill_data1(self, firstname="", lastname="", email="", password=""):
        """Fill user with sample data, HOWEVER password is INCORRECT ENTRY"""
        # random_user1 from conftest file
        user = random_str()
        self.firstname = f"{user}{random_num()}" if not firstname else firstname
        self.lastname = f"{user}{random_num()}" if not lastname else lastname
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(3)}{random_num_len()}" if not password else password  # too short password

    def fill_data2(self, firstname="", lastname="", email="", password=""):
        """Fill user with existing account data"""
        # existing_user from conftest file
        self.firstname = "Nataliia" if not firstname else firstname
        self.lastname = "Ivashko" if not lastname else lastname
        self.email = "nataliiaoivashko@gmail.com" if not email else email
        self.password = "1qaz!QAZ" if not password else password

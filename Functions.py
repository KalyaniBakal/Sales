import datetime
import random
import string


def generate_past_date(end_date=datetime.date.today(), days_back=365):
    start_date = end_date - datetime.timedelta(days=days_back)
    return generate_random_date(start_date, end_date)


# Generate a random date for today
def generate_present_date():
    return datetime.date.today()

def generate_random_future_date(start_date, end_date):
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)
    random_date = start_date + datetime.timedelta(days=random_days)
    return random_date

def generate_future_date(start_date=datetime.date.today(), days_forward=365):
    end_date = start_date + datetime.timedelta(days=days_forward)
    return generate_random_date(start_date, end_date)

def generate_random_date(start_date, end_date):
    if start_date > end_date:
        raise ValueError("start_date must be earlier than or equal to end_date")

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def generate_unique_phone_number():
    return ''.join(random.choices(string.digits, k=10))

def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))  # Random string of letters
random_name = generate_random_name()

def generate_random_description(length=100):
    return ''.join(random.choices(string.ascii_letters, k=length))  # Random string of letters
random_name = generate_random_name()

def generate_random_4_digit_time():
    hour = random.randint(0, 11)  # Random hour between 00 and 11 (12-hour format)
    minute = random.randint(0, 59)  # Random minute between 00 and 59
    return f"{hour:02d}{minute:02d}"


def generate_random_email(domain="example.com"):
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = f"{username}@{domain}"
    return email

def generate_full_address():
    house_number = random.randint(1, 999)
    street_name = ''.join(random.choices(string.ascii_letters, k=10))
    city = random.choice(["Monzon", "Huesca", "Zaragoza", "Barcelona", "Madrid"])
    country = random.choice(["Spain", "France", "Germany", "Italy", "Portugal"])
    return f"{house_number} {street_name} Street, {city}, {country}"



import datetime

def add_gigasecond(birth_date):
	gigasecond_date = birth_date + datetime.timedelta(seconds=1000000000)

	return gigasecond_date
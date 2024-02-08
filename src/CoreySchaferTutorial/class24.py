import datetime

# Data e hora atual
now = datetime.now()
print("Data e hora atual:", now)

# Data e hora específicas
specific_date = datetime(2023, 5, 17, 12, 30, 0)
print("Data e hora específicas:", specific_date)

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond
print("Ano:", year)
print("Mês:", month)


formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Data formatada:", formatted_date)


date_string = "2023-05-17 12:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Data interpretada:", parsed_date)


from datetime import timedelta

# Cria um timedelta de 10 dias
delta = timedelta(days=10)
print("Timedelta:", delta)


future_date = now + delta
print("Data futura:", future_date)

past_date = now - delta
print("Data passada:", past_date)


import pytz

# Obtém um objeto de fuso horário para UTC
utc = pytz.utc

# Converte um datetime ingênuo para um datetime com fuso horário
aware_datetime = utc.localize(now)
print("Datetime ciente:", aware_datetime)

# Converte um datetime com fuso horário para outro fuso horário
eastern = pytz.timezone('US/Eastern')
eastern_datetime = aware_datetime.astimezone(eastern)
print("Datetime no fuso horário Eastern:", eastern_datetime)

# str() vs repr()

a = [1,2,3,4]
b = 'sample string'

print (str(a))
print (repr(a))

print (str(b))
print (repr(b))

from datetime import datetime, timedelta, timezone

# Obtém a data e hora atuais em UTC
utc_now = datetime.now(timezone.utc)

# Define o fuso horário desejado (UTC-3)
utc_offset = timedelta(hours=-3)
local_time = utc_now.replace(tzinfo=timezone.utc) + utc_offset

print("Data e hora UTC:", utc_now)
print("Data e hora local (UTC-3):", local_time)
import datetime as dt
from datetime import timedelta

# date_str = "21/12/2025"
# date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
# print(date_obj)
last_run = dt.datetime.strptime("17/04/2026", "%d/%m/%Y")
print(last_run)
if dt.datetime.now() > last_run + timedelta(days=7):
    print("It's time to run the scraper!")
    


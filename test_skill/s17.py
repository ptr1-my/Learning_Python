from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%A, %d of %B on %Y, %I:%M:%S %p")
print(formatted_date)
from datetime import datetime
# guar dando hora  e data 
today = datetime.now()
day = today.day
month = today.month
year = today.year
print ("hoje ", today, " dia ", day, "/", month, "/", year)
print ("hora ", today.hour, "| min ", today.minute, "| seg ", today.second)
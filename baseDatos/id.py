from datetime import datetime
import uuid

id = uuid.uuid4()
# current date and time
now = datetime.now()


#Tiempo apartir del 2020 cuando inicio el juego
secondYears_50=50*365*24*60*60
timeApartir2020=now.timestamp()-secondYears_50
redondeo_4=int(timeApartir2020*1000.0)
#redondeo_4/=1000.0
print(redondeo_4)
print(id)


#20473835751    20473894672
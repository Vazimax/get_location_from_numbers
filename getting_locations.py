from test import number
from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers

get_info = phonenumbers.parse(number,'CH')

print(geocoder.description_for_number(get_info,'en'))

service_number = phonenumbers.parse(number,'RO')
print(carrier.name_for_number(service_number,'en'))


#Track phone numbers location using python
#code by SecretBeast_bg01


import  phonenumbers  as  ph#pip install phonenumbers
from  phonenumbers  import  carrier
from  phonenumbers  import  geocoder
from  phonenumbers  import  timezone

number  =  "+916756797670"#Enter the number you want to track
number  =  ph . parse ( number )
print ( timezone . time_zones_for_number ( number ))
print ( carrier . name_for_number ( number ,  "en" ))
print ( geocoder . description_for_number ( number ,  "en" ))

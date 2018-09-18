import mlab
from register import Register
mlab.connect()

r = Register(fullname="Dương thê bách", email="thebach1997@gmail.com", username="thebach", password="1")
print(r.fullname)
print(r.email)
print(r.username)
print(r.password)

r.save()
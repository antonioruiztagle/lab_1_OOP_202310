from user import User

u = User("username", "password")
print(u.show_username("password"))
print(u.show_username(" "))
#print(u.__password)
u.password = "nueva_clave"
#print(u.password)
print(u.change_passwrod("pass", "nueva_clave"))
print(u.change_passwrod("password", "nueva_clave"))
print(u.show_password("username"))

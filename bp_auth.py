from models import Owners, session #Need the Users model to create and search for users
#need the session to add users to our db



#Create Login function
#get email and password from user
#check database for owner with the given email
#if you find an owner, check if the found owners password is the same as the given password
#if so return user
def login():
  print("----------- Login -------------")
  email = input("Email: ")
  password = input("Password: ")
  
  user = session.query(Owners).filter_by(email=email).first() #query db for owner with given email
  
  if user and user.password == password: #if we found a user and the passwords match
      print("Successfully logged in")
      print(f"Welcome back {user.name}!")
      return user
  else:
      print("Invalid username or password.")

#Create Register function
#get all info required to create an owner from the user
#try and create an Owner from the info (will fail if email is already in user)
#if you succeed return user
#except error and print message
def register():
  print("---------------- ")
#step 1: get info from user
  name = input("Name: ")
  email = input("Email: ")
  phone = input("Phone: ")
  password = input("Password: ")
  
#step 2: try and create the user
  try:
      new_owner = Owners(name=name, email=email, phone=phone, password=password) #new owner object/instance
#step 3: add and commit the new owner to the db
      session.add(new_owner)
      session.commit()
#step 4: print success message and return the new owner
      print(f"Welcome {name}!")
      return new_owner
#step 5: except error and print message
  except Exception as e:
      print(f"Issue creating this account{e}")
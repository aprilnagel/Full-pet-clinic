from models import Owners, session

#View profile function
#displays the current users info
# def view_owner(current_user):
#   print("Name: ",current_user.name)
#   print("Email: ",current_user.email)
#   print("Phone: ",current_user.phone)

def view_owner(current_user):
  current_user.display()
  
#Update profile function
#dsiplays current user info
#allows user to update any of the fields
#commits changes 
#shows changes and returns update current_user

def update_owner(current_user):
    current_user.display()
    print("Enter new info. Leave blank to keep current info.")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    password = input("password: ")
    
    #checking to see if the user entered new info. If they don't, the if statement will not run and the current info will stay the same
    if name:
        current_user.name = name
    if email:
        current_user.email = email
    if phone:
        current_user.phone = phone
    if password:
        current_user.password = password
    
    session.commit() #commit changes to db
    print("Profile updated successfully!")
    current_user.display() #show updated info
    return current_user
    
    

#Update profile function
#Ask user to confirm they want to delete
#if so delete the current user from the session
#commits changes 
#call main() to start the program over

def delete_owner(current_user):
    choice = input("TO CONFIRM: Do you want to delete your account? (y/n): ")
    if choice.lower() == 'y':
        session.delete(current_user)
        session.commit()
        print("Account deleted successfully.") 
        return None
    else:
        print("Account deletion canceled. Back to menu.")
        return current_user
#using the while loop in front_end.py to call main() again if we want to once we delete the user. it will loop back to the login/register menu.
        
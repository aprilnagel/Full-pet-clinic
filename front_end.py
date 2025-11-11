#DONT FORGET TO IMPORT FUNCTIONS AFTER YOU MAKE THEM
from models import Owners, session
from bp_auth import register, login
from bp_owners import view_owner, update_owner, delete_owner
from bp_pets import view_pets, create_pet, update_pet, delete_pet
from bp_appointment import create_appointment, view_appointments, reschedule_appointment, complete_appointment


def welcome_menu():
    current_user = None
    while True:
        print("""
--------- Welcome to Pet Clinic --------
        1.) Login
        2.) Register
""")
        choice = input("select (1 or 2) or quit: ")
        if choice == '1':
            #login function
            current_user = login() #this function returns the logged in user/owner object
            #should set the current user on successful login
            return current_user

        elif choice == '2':
            #register function
            current_user = register() #this function creates and returns a new user/owner object
            #should set the current user on successful register
            return current_user

        elif choice == 'quit':
            return
        else:
            print("Invalid response please try again.")

def owner_menu(current_user):
    while True:
        print("""
    1.) View Profile
    2.) Update Profile
    3.) Delete Profile
    4.) Back""")
        choice = input("choose 1-3: ")
        if choice == '1':
            #view profile funtion should display the current users info
            view_owner(current_user)
        elif choice == '2':
            #update profile function, and returns the updated user
            #on success, should set current_user to the user that is returned
            current_user = update_owner(current_user)
        elif choice == '3':
            #delete the current users account
            current_user = delete_owner(current_user)
            main() #call main to start program over if we delete the user
            return current_user
        elif choice == '4':
            return current_user#Goes back to main menu
        else:
            print("Invalid Selection.")

def pets_menu(current_user):
    while True:
        print("""
1.) View my Pets
2.) Create Pet
3.) Update Pet
4.) Delete Pet
5.) Back""")
        choice = input("choose 1-5: ")
        if choice == '1':
            #function that displays the current user's pets
            view_pets(current_user)
        elif choice == '2':
            #function to create a new pet linked to the current user, add to db
            create_pet(current_user)
        elif choice == '3':
            #function to update a particular pet 
            update_pet(current_user)
        elif choice == '4':
            #function to delete a particuler pet
            delete_pet(current_user)
        elif choice == '5':
            return
        else:
            print("Invalid Selection.")

def appointments_menu(current_user):
    while True:
        print("""
1.) Schedule Appointment
2.) View Appointments
3.) Reschedule Appointment
4.) Complete Appointment
5.) Back
""")
        choice = input("choose 1-5: ")
        if choice == '1':
            #Function to create a new appointment between one of the user's pets
            #and one of the vets
            create_appointment(current_user)
        elif choice == '2':
            #View current user's appointments
            view_appointments(current_user)
        elif choice == '3':
            #Reschedule appointment (change the date)
            reschedule_appointment(current_user)
        elif choice == '4':
            #Complete appointment (change status to complete)
            complete_appointment(current_user)
        elif choice =='5':
            return


def main():
    
    current_user = welcome_menu() 

    #After you test you login and register functions, it might be more efficient
    #to set current_user to a user in your db so you don't have to log in everytime
    #you want to test something.
    
    if current_user:
        while True and current_user:#If we have a current user, show main menu when we delete an owner. The while loop will exit if current_user is None
            print("""
        --------- Pet Clinic --------
        1.) Manage Profile
        2.) My Pets
        3.) My Appointments
        """)
            choice = input("choose 1-3: ")
            if choice == '1':
                owner_menu(current_user)
            elif choice == '2':
                pets_menu(current_user)
            elif choice == '3':
                appointments_menu(current_user)
            else:
                print("Invalid Selection.")
    

main()
    

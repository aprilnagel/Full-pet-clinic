from models import Pets, session

#view pets function
#Takes in current user
#Loops over all of the current users pets (use the .pets relationship attribute to get list of pets)
#prints the pets info
def view_pets(current_user):
    print("--------- My Pets ---------------")
    for pet in current_user.pets:
        pet.display()
#Create pets function
#gets pets info from user
#create Pets() from the info
#print new pet

def create_pet(current_user):
    name = input("Pet's name: ")
    species = input("Pet's species: ")
    breed = input("Pet's breed (optional): ")
    age = input("Pet's age (optional): ")
    
    
    new_pet = Pets(
        name=name,
        species=species,
        breed=breed if breed else None,
        age=age if age else None,
        owner_id=current_user.id
    )
    #add to the table
    session.add(new_pet)
    session.commit()
    print("SUCCESS! New pet created:")
    new_pet.display()

#Update pets function
#display current users pets
#allow them to select a pet BY NAME
#query that pet from the database
#get updated info from the user
#set that pets info to the new info
#commit changes
#print new pet info

def update_pet(current_user):
    view_pets(current_user) #calling the view pets function to show current pets
    choice = input("Enter the name of the pet you want to update: ")#must query the pet name in the db next
    pet = session.query(Pets).where(Pets.name.ilike(choice), Pets.owner_id == current_user.id).first() #searching for pet by name and owner id to ensure correct pet is selected
    if pet:
        print ("UPDATE PET INFO: Leave blank to keep current info.")
        name = input("Name: ")
        species = input("Species: ")
        breed = input("Breed: ")
        age = input("Age: ")
        if name:
            pet.name = name
        if species:
            pet.species = species
        if breed:
            pet.breed = breed
        if age:
            pet.age = age
        session.commit()
        print(f"SUCCESS! {pet.name} has been updated:")
        pet.display()
    else:
        print("Pet not found.")

#Delete pets function
#display current users pets
#allow them to select a pet BY NAME
#query that pet from the database
#Ask user if they are sure they want to delete this pet
#delete pet from the session
#commit changes

def delete_pet(current_user):
    view_pets(current_user) #calling the view pets function to show current pets
    choice = input("Enter the name of the pet you want to delete: ")#must query the pet name in the db next
    pet = session.query(Pets).where(Pets.name.ilike(choice), Pets.owner_id == current_user.id).first() #searching for pet by name and owner id to ensure correct pet is selected
    if pet:
        confirm = input(f"Are you sure you want to delete your pet {pet.name}? (y/n): ")
        if confirm.lower() == 'y':
            session.delete(pet)
            session.commit()
            print(f"Record removed. {pet.name} has been deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("Pet not found.")





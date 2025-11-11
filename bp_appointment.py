from models import Owners, Pets, Vets, session, Appointments
from datetime import datetime

#IMPORTANT when creating an appointment, it is required to convert the date string
# "YYYY-MM-DD" int a python date object

date_format = "%Y-%m-%d" #This will be used to format your date

#Syntax for date conversion

# new_date = datetime.strptime("Date String", date_format)
#example
today = datetime.strptime("2025-08-08", date_format)


#Create new appointment
#display pets
#Choose the pet you wish to create an appointment for
#query them out of the db using their name
#display vets
#Choose the vet you with to create an appointment with
#Query them out of the db
#Gather the rest of the info for the appointment
#Convert the date string to python date object
#Create the Appointment() (remind you'll need the pet id and the vet id)
def create_appointment(current_user):
    print("Who is this appointment for?")
    for pet in current_user.pets:
        pet.display()
    choice = input("Enter the pet's name: ")
    
    pet = session.query(Pets).where(Pets.name.ilike(choice), Pets.owner_id == current_user.id).first()
    if pet:
        print(f"Creating appointment for {pet.name}")
        
        vets = session.query(Vets).all()
        for vet in vets:
            print("--------Available Vets:-------")
            vet.display()
        vet_name = input("Enter the vet's name you'd like to see: ")
        vet = session.query(Vets).where(Vets.name.ilike(vet_name)).first()
        if vet:
            appointment_date = input(f"When would you like to {pet.name}'s appointment with {vet.name} (YYYY-MM-DD): ")
            notes = input(f"What is the reason for {pet.name}'s appointment?: ")
            date_obj = datetime.strptime(appointment_date, date_format) #convert date string to date object
            
            new_appointment = Appointments(
                pet_id = pet.id,
                vet_id = vet.id,
                appointment_date = date_obj,
                notes = notes,
                status = 'Scheduled'
            )
            session.add(new_appointment)
            session.commit()
            print(f"Appointment for {pet.name} with {vet.name} on {appointment_date} has been scheduled.")
            return
        else:
            print("Vet not found.")
    else:
        print("Pet not found.")

# view appointments
def view_appointments(current_user):
  for pet in current_user.pets:
    print(f"{pet.name}'s appointments")
    for appointment in pet.appointments:
      print("-----------------------")
      appointment.display()
#Reschedule appointments
#Show appointments with ids (Loop over current user pets, loop over each pets appointments e.g nested loop)
#Select an appointment by id
#ask user for new date
#convert date
#update the appointment date
def reschedule_appointment(current_user):
  view_appointments(current_user)
  choice = input("Select appointment by id: ")
  appointment = session.get(Appointments, choice)
  if appointment and appointment.pet.owner_id ==current_user.id:
    new_date = input("Enter new date: (YYY-MM-DD)")
    new_date = datetime.strptime(new_date, date_format)
    
    appointment.appointment_date = new_date
    session.commit()
    print(f"Rescheduled appointment for {new_date}")
  else:
    print("Invalid Selection.")


#Complete appointments
#Show appointments with ids (Loop over current user pets, loop over each pets appointments e.g nested loop)
#query the appointment by id
#change appointment.status to 'complete"
#print success message

def complete_appointment(current_user):
    view_appointments(current_user)
    choice = input("Select appointment by id to complete: ")
    appointment = session.get(Appointments, choice)
    if appointment and appointment.pet.owner_id ==current_user.id:
        appointment.status = 'Complete'
        session.commit()
        print("-----------------------")
        print(f"Appointment {appointment.id} marked as complete.")
    else:
        print("Invalid Selection.")

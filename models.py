from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean, Text, DateTime
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column
from datetime import datetime, date

Base = declarative_base()
engine = create_engine('sqlite:///pet_clinic.db')
Session = sessionmaker(bind=engine)
session = Session()

class Owners(Base):
    __tablename__ = 'owners'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    
    pets: Mapped[list["Pets"]] = relationship("Pets", back_populates="owner")
    
    def display(self):
        print("--------- My Info ---------------")
        print("Name: ",self.name)
        print("Email: ",self.name)
        print("Phone: ",self.name)
    

class Pets(Base):
    __tablename__ = 'pets'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    species: Mapped[str] = mapped_column(String(30), nullable=False)
    breed: Mapped[str] = mapped_column(String(50), nullable=True)
    age: Mapped[str] = mapped_column(String(15), nullable=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'), nullable=False)
    
    
    owner: Mapped["Owners"] = relationship("Owners", back_populates="pets")
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="pet")
    
    def display(self):
        print("--------- Pet Info ---------------")
        print("Name: ",self.name)
        print("Species: ",self.species)
        print("Breed: ",self.breed)
        print("Age: ",self.age)
        print("Owner ID: ",self.owner_id)
        
        
class Vets(Base):
    __tablename__ = 'vets'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    specialization: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="vet")
    
    def display(self):
        print("--------- Vet Info ---------------")
        print("Name: ",self.name)
        print("Specialization: ",self.specialization)
        print("Email: ",self.email)
        
#---------------Association Table-----------------
#---------------Many to Many Relationship between Pets and Vets through Appointments-----------------
class Appointments(Base):
    __tablename__ = 'appointments'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'), nullable=False)
    vet_id: Mapped[int] = mapped_column(Integer, ForeignKey('vets.id'), nullable=False)
    appointment_date: Mapped[date] = mapped_column(Date, nullable=False)
    notes: Mapped[Text] = mapped_column(Text(200), nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default='Scheduled')
    
    pet: Mapped["Pets"] = relationship("Pets", back_populates="appointments")
    vet: Mapped["Vets"] = relationship("Vets", back_populates="appointments")
    
    def display(self):
        print("--------- Appointment Info ---------------")
        print("Pet ID: ",self.pet_id)
        print("Vet Name: ",self.display())
        print("Appointment Date: ",self.appointment_date)
        print("Notes: ",self.notes)
        print("Status: ",self.status)


#---------------Creating Owners-----------------
# owner1 = Owner(name="John Doe", phone="123-456-7890", email="john.doe@example.com")
# owner2 = Owner(name="Jane Smith", phone="987-654-3210", email="jane.smith@example.com")
# owner3 = Owner(name="Alice Johnson", phone="555-123-4567", email="alice.johnson@example.com")
# owner4 = Owner(name="Bob Brown", phone="444-555-6666", email="bob.brown@example.com")
# owner5 = Owner(name="April Nagel", phone="222-333-4444", email="april.nagel@example.com")
# session.add_all([owner1, owner2, owner3, owner4, owner5])
# session.commit()

#---------------Creating Pets-----------------
# pet1 = Pet(name="Buddy", species="Dog", breed="Golden Retriever", age=3, owner_id=1)
# pet2 = Pet(name="Mittens", species="Cat", breed="Siamese", age=2, owner_id=2)
# pet3 = Pet(name="Charlie", species="Dog", breed="Beagle", age=4, owner_id=2)
# pet4 = Pet(name="Luna", species="horse", breed="Thoroughbred", age=5, owner_id=3)
# pet5 = Pet(name="Max", species="Cat", breed="American Shorthair", age=3, owner_id=5)
# pet6 = Pet(name="Chance", species="Horse", breed="Quarter Horse", age=32, owner_id=5)
# pet7 = Pet(name="Libby", species="Dog", breed="The Best Mut In The World", age=13, owner_id=5)
# pet8 = Pet(name="Lily", species="Dog", breed="Setter Mix", age="6 months", owner_id=5)
# session.add_all([pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8])
# session.commit()

#---------------Creating Vets-----------------
# vet1 = Vets(name="Dr. Emily Carter", specialization="General Veterinary Medicine", email="emily.carter@example.com")
# vet2 = Vets(name="Dr. Michael Smith", specialization="Surgery", email="michael.smith@example.com")
# vet3 = Vets(name="Dr. Sarah Johnson", specialization="Dermatology", email="sarah.johnson@example.com")
# vet4 = Vets(name="Dr. David Lee", specialization="Dentistry", email="david.lee@example.com")
# session.add_all([vet1, vet2, vet3, vet4])
# session.commit()

#---------------Creating Appointments-----------------
# appointment1 = Appointments(pet_id=1, vet_id=1, appointment_date=datetime(2026, 7, 10, 10, 0), notes="Regular check-up", status="Scheduled")
# appointment2 = Appointments(pet_id=2, vet_id=2, appointment_date=datetime(2024, 7, 11, 14, 30), notes="Vaccination", status="Completed")
# appointment3 = Appointments(pet_id=3, vet_id=1, appointment_date=datetime(2025, 12, 12, 9, 0), notes="Skin allergy treatment", status="Scheduled")
# appointment4 = Appointments(pet_id=8, vet_id=3, appointment_date=datetime(2024, 8, 15, 11, 0), notes="Dental cleaning", status="Cancelled")
# appointment5 = Appointments(pet_id=8, vet_id=4, appointment_date=datetime(2024, 9, 20, 16, 0), notes="Dental cleaning", status="Completed")
# appointment6 = Appointments(pet_id=4, vet_id=2, appointment_date=datetime(2025, 11, 7, 13, 0), notes="Neutering surgery", status="Scheduled")
# appointment7 = Appointments(pet_id=5, vet_id=1, appointment_date=datetime(2026, 1, 5, 15, 30), notes="Annual vaccination", status="Scheduled")
# appointment8 = Appointments(pet_id=6, vet_id=3, appointment_date=datetime(2024, 10, 22, 10, 0), notes="Hoof trimming", status="Completed")
# appointment9 = Appointments(pet_id=7, vet_id=4, appointment_date=datetime(2026, 3, 18, 9, 30), notes="Dental check-up", status="Scheduled")
# session.add_all([appointment1, appointment2, appointment3, appointment4, appointment5, appointment6, appointment7, appointment8, appointment9])
# session.commit()


 #Add to the bottom of page
# Base.metadata.drop_all(bind=engine) #Add to the bottom of page
Base.metadata.create_all(bind=engine) #Add to the bottom of page
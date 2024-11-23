from abc import ABC, abstractmethod

# Abstract observer: This class ensures all observers implement the 'update' method.
class Observer(ABC):
    @abstractmethod
    def update(self, flat_number, status):
        """
        Abstract method that needs to be implemented by all observers.
        It gets called when the subject (Community) updates its state.
        """
        pass

# Subject class: Community manages the flats and the list of observers.
class Community:
    def __init__(self):
        self.houses = {}  # Dictionary to hold details about flats.
        self.observers = []  # List to maintain all attached observers.

    # Method to add a new flat to the community.
    def add_flat(self, flat_number, bhk_type):
        """
        Adds a new flat with its BHK type to the community.
        Initial status is set to 'unoccupied'.
        After adding the flat, all observers are notified.
        """
        self.houses[flat_number] = {"bhk": bhk_type, "status": "unoccupied", "occupant": None}
        self.notify_observers(flat_number)

    # Method to update occupancy of a flat.
    def update_occupancy(self, flat_number, occupant_details=None):
        """
        Updates the occupancy status of the flat.
        If 'occupant_details' is provided, the flat becomes 'occupied'.
        Otherwise, the status is changed to 'unoccupied'.
        """
        if flat_number in self.houses:
            self.houses[flat_number]["status"] = "occupied" if occupant_details else "unoccupied"
            self.houses[flat_number]["occupant"] = occupant_details
            self.notify_observers(flat_number)

    # Attach (register) an observer to the community.
    def attach(self, observer):
        """
        Registers an observer, which will get notified of any changes in the community.
        """
        self.observers.append(observer)

    # Detach (remove) an observer from the community.
    def detach(self, observer):
        """
        Removes an observer from the notification list.
        """
        self.observers.remove(observer)

    # Notify all observers of any change in the community (like occupancy change).
    def notify_observers(self, flat_number):
        """
        Notifies all attached observers about the change in the specified flat.
        """
        for observer in self.observers:
            observer.update(flat_number, self.houses[flat_number])

# Observer: AvailabilityTracker keeps track of unoccupied flats.
class AvailabilityTracker(Observer):
    def __init__(self, community):
        self.community = community

    def update(self, flat_number, flat_details):
        """
        Receives updates from the community about changes in the status of flats.
        It prints whether a flat has become occupied or is still available.
        """
        print(f"Availability Tracker: Flat {flat_number} is now {flat_details['status']}.")

    def get_available_flats(self, bhk_type):
        """
        Returns a list of all available flats of a specific BHK type.
        """
        available_flats = [flat for flat, details in self.community.houses.items()
                           if details['bhk'] == bhk_type and details['status'] == 'unoccupied']
        return available_flats

# Observer: OccupancyTracker monitors who occupies a flat.
class OccupancyTracker(Observer):
    def __init__(self, community):
        self.community = community

    def update(self, flat_number, flat_details):
        """
        Receives updates from the community about the occupancy of flats.
        If a flat is occupied, it prints the occupant's details.
        If unoccupied, it notes that the flat is vacant.
        """
        occupant = flat_details['occupant']
        if flat_details['status'] == 'occupied':
            print(f"Occupancy Tracker: Flat {flat_number} is occupied by {occupant['name']}.")
        else:
            print(f"Occupancy Tracker: Flat {flat_number} is now unoccupied.")

    def get_occupant_details(self, flat_number):
        """
        Returns details of the occupant of a given flat.
        """
        flat_details = self.community.houses.get(flat_number)
        return flat_details['occupant'] if flat_details else None

# Observer: PaymentTracker tracks maintenance payments for occupied flats.
class PaymentTracker(Observer):
    def __init__(self, community):
        self.community = community
        self.payments = {}  # Dictionary to track payment status.

    def update(self, flat_number, flat_details):
        """
        Receives updates about flat occupancy.
        If a flat is occupied, a payment request is generated.
        If the flat becomes unoccupied, it removes the payment requirement.
        """
        if flat_details['status'] == 'occupied':
            print(f"Payment Tracker: Flat {flat_number} needs to pay monthly maintenance.")
            self.payments[flat_number] = False  # Payment due.
        else:
            if flat_number in self.payments:
                del self.payments[flat_number]  # Remove payment tracking for unoccupied flats.

    # Method to mark maintenance payment as complete.
    def pay_maintenance(self, flat_number):
        """
        Marks the maintenance payment for a flat as done.
        """
        if flat_number in self.payments:
            self.payments[flat_number] = True
            print(f"Payment Tracker: Flat {flat_number} has paid the maintenance fee.")

# Creating the community and the three observers.
community = Community()
availability_tracker = AvailabilityTracker(community)
occupancy_tracker = OccupancyTracker(community)
payment_tracker = PaymentTracker(community)

# Attach the observers to the community.
community.attach(availability_tracker)
community.attach(occupancy_tracker)
community.attach(payment_tracker)

# Add new flats to the community.
community.add_flat(101, "2BHK")
community.add_flat(102, "3BHK")

# Update the occupancy of a flat.
community.update_occupancy(101, {"name": "John Doe", "contact": "555-1234"})

# Display available 2BHK flats.
print("Available 2BHK flats:", availability_tracker.get_available_flats("2BHK"))

# Get details of the occupant of flat 101.
print("Occupant of flat 101:", occupancy_tracker.get_occupant_details(101))

# Pay maintenance for flat 101.
payment_tracker.pay_maintenance(101)

# Update the occupancy of flat 101 to unoccupied.
community.update_occupancy(101)

# Check if flat 101 has paid maintenance after it was vacated.
print(f"Flat 101 maintenance paid: {payment_tracker.payments.get(101, 'N/A')}")

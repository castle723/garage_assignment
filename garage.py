class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets and self.parkingSpaces:
            ticket = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self.currentTicket[ticket] = {"paid": False, "parking_space": parking_space}
            return f"Please take ticket {ticket}. You are assigned parking space {parking_space}."
        else:
            return "Sorry, the garage is full."

    def payForParking(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.currentTicket and not self.currentTicket[ticket]["paid"]:
            payment = input("Enter the payment amount: ")
            if payment:
                self.currentTicket[ticket]["paid"] = True
                print(f"Your ticket {ticket} has been paid. You have 15 minutes to leave.")
            else:
                print("Payment was not provided.")
        else:
            print("Invalid ticket number or the ticket has already been paid.")

    def leaveGarage(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.currentTicket:
            if self.currentTicket[ticket]["paid"]:
                self.parkingSpaces.append(self.currentTicket[ticket]["parking_space"])
                self.tickets.append(ticket)
                del self.currentTicket[ticket]
                print("Thank you, have a nice day!")
            else:
                payment = input("Please pay for parking: ")
                if payment:
                    self.currentTicket[ticket]["paid"] = True
                    self.parkingSpaces.append(self.currentTicket[ticket]["parking_space"])
                    self.tickets.append(ticket)
                    del self.currentTicket[ticket]
                    print("Thank you, have a nice day!")
                else:
                    print("Payment was not provided.")
        else:
            print("Invalid ticket number.")


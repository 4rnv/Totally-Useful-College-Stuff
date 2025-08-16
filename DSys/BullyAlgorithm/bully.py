import random
import time

class Server:
    def __init__(self, id, is_coordinator=False):
        self.id = id
        self.is_coordinator = is_coordinator
        self.alive = True  # All servers start as active
        self.tickets = {"User1": None, "User2": None}  # Stores user ticket status

    def start_election(self, servers):
        print(f"\nServer {self.id} detected coordinator failure! Starting election.")
        higher_servers = [s for s in servers if s.id > self.id and s.alive]

        if not higher_servers:
            print(f"Server {self.id} becomes the new coordinator.")
            self.is_coordinator = True
            self.announce_victory(servers)
        else:
            for s in higher_servers:
                print(f"Server {self.id} → Sending election message to Server {s.id}")
            time.sleep(1)
            # Wait for responses
            for s in higher_servers:
                if s.alive:
                    print(f"Server {s.id} → Responding to election message from Server {self.id}")
                    s.start_election(servers)
                    return  # Stop election since higher server is taking over

    def announce_victory(self, servers):
        print(f"\nServer {self.id} is the new coordinator! Announcing to all servers.")
        for s in servers:
            if s.alive and s.id != self.id:
                s.is_coordinator = False
                print(f"Server {s.id} acknowledges Server {self.id} as the new coordinator.")

    def book_ticket(self, user):
        if self.is_coordinator:
            if self.tickets[user] is None:
                self.tickets[user] = "Booked"
                print(f"✅ {user}'s ticket has been booked by Server {self.id}.")
            else:
                print(f"⚠️ {user} already has a booked ticket!")
        else:
            print(f"❌ Server {self.id} cannot book tickets. Not the coordinator!")

    def cancel_ticket(self, user):
        if self.is_coordinator:
            if self.tickets[user] == "Booked":
                self.tickets[user] = None
                print(f"❌ {user}'s ticket has been cancelled by Server {self.id}.")
            else:
                print(f"⚠️ {user} has no ticket to cancel!")
        else:
            print(f"❌ Server {self.id} cannot cancel tickets. Not the coordinator!")

# Create 10 servers, with Server 10 as the initial coordinator
servers = [Server(i, is_coordinator=(i == 10)) for i in range(1, 11)]

# Coordinator (Server 10) handles ticket booking
coordinator = servers[-1]  # Server 10
coordinator.book_ticket("User1")
coordinator.book_ticket("User2")

# Simulate Coordinator Failure
coordinator.alive = False
print("\n[ALERT] Coordinator (Server 10) has failed!")

# Start election from a random active server
initiator = random.choice(servers[:-1])  # Any server except 10
initiator.start_election(servers)

# Find the new coordinator
new_coordinator = next((s for s in servers if s.is_coordinator), None)

# New coordinator handles ticket operations
new_coordinator.cancel_ticket("User1")
new_coordinator.book_ticket("User2")

# Simulate Server 10 Rebooting
time.sleep(2)
coordinator.alive = True  # Server 10 reboots
print("\n[INFO] Server 10 has rebooted!")

# Server 10 checks and reclaims coordinator role if necessary
current_coordinator = next((s for s in servers if s.is_coordinator), None)

if current_coordinator and current_coordinator.id != 10:
    print("\nServer 10 detects a different coordinator. It starts a new election.")
    coordinator.start_election(servers)

# Server 10 now handles ticket operations again
coordinator.book_ticket("User1")
coordinator.cancel_ticket("User2")
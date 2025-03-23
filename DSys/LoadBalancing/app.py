# 2 servers
# Each server has max capacity of 3
# 1 load balancer with queue of 10
# If both servers max their capacity the task is added to the queue of load balancer
# 2 clients randomly sending infinite requests to loadbalancer
# Load balancer randomly assigns task to server with less connections
# Server performs task for random amount of time

import time
from queue import Queue
import random
import threading

class Server:
    def __init__(self, id, capacity):
        self.id : str = id
        self.capacity: int = int(capacity)
        self.inuse : int = 0

    def perform_task(self, task):
        rando = random.randint(1, 5)
        self.inuse += 1
        print(f'Server {self.id} is performing task {task} for {rando} seconds.')
        time.sleep(rando)
        self.inuse -= 1
        return True

def assign_task(server : Server, task):
    if server.perform_task(task):
        print(f'Task {task} performed successfully by server {server.id}')

def load_balancer(server1: Server, server2: Server, task_queue: Queue):
    while True:
        if not task_queue.empty():
            task = task_queue.get()
            available1 = server1.capacity - server1.inuse
            available2 = server2.capacity - server2.inuse
            if available1 > available2:
                assign_task(server1, task)
            elif available2 > available1:
                assign_task(server2, task)
            else:
                chosen_server = random.choice([server1, server2])
                assign_task(chosen_server, task)
            task_queue.task_done()
        else:
            print('No tasks in the queue. Load balancer is waiting...')
            time.sleep(1)

def client(task_queue : Queue):
    while True:
        task = random.randint(1, 100)
        if not task_queue.full():
            task_queue.put(task)
            print(task_queue.queue)
            print(f'Client added task {task} to the queue.')
        else:
            print(task_queue.queue)
            print('Queue is full, client is waiting.')
        time.sleep(random.uniform(1, 4))

server1 = Server("E", 3)
server2 = Server("A", 3)
task_queue = Queue(maxsize=10)

client_thread = threading.Thread(target=client, args=(task_queue,), daemon=True)
load_balancer_thread = threading.Thread(target=load_balancer, args=(server1, server2, task_queue), daemon=True)
client_thread.start()
load_balancer_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Simulation ended.")
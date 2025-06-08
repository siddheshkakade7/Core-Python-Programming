import threading
def print_numbers():
    for i in range(5):
        print(f"Thread 1 :{i}")

def print_letters():
    for letter in 'ABCDE':
        print(f"Thread 2:{letter}")

# Creating two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start thread
thread1.start()
thread2.start()

# Wait fot both threads to finish
thread1.join()
thread2.join()

print("Both threads have been finished.")
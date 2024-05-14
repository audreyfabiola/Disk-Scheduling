import sys

#     | --------------------------------------|
#     |               FCFS                    |
#     |---------------------------------------|

def FCFS(initial_position, requests):
    head_movements = 0
    head = initial_position

     # Calculate head movements
    for request in requests:
        distance = abs(request - head)
        head_movements += distance
        head = request  # Set position to the next cylinder 
    
    return head_movements

def FCFS_optimized(initial_position, requests):
    # Sort the requests 
    requests.sort()
    
    head_movements = 0
    head = initial_position

    # Calculate head movements
    for request in requests:
        distance = abs(request - head)
        head_movements += distance
        head = request   # Set position to the next cylinder 
    
    return head_movements

#     | --------------------------------------|
#     |               SCAN                    |
#     |---------------------------------------|

def SCAN(initial_position, requests, direction="left"):
    disk_size = 5000  
    head_movements = 0
    head = initial_position

    # Cylinder positions according to direction
    left_requests = [0] if direction == "left" else []
    right_requests = [disk_size - 1] if direction == "right" else []

    # Dividing the requests to either left or right
    for request in requests:
        if request < head:
            left_requests.append(request)
        elif request > head:
            right_requests.append(request)

    # Picking the request direction
    runs = [left_requests[::-1], right_requests] if direction == "left" else [right_requests, left_requests[::-1]]

    # Calculate head movements
    for requests in runs:
        for current_track in requests:
            distance = abs(current_track - head)
            head_movements += distance
            head = current_track

    return head_movements

def SCAN_optimized(initial_position, requests, direction="left"):
    disk_size = 5000  
    head_movements = 0
    head = initial_position

     # Cylinder positions according to direction
    left_requests = [0] if direction == "left" else []
    right_requests = [disk_size - 1] if direction == "right" else []

    # Dividing the requests to either left or right
    for request in requests:
        if request < head:
            left_requests.append(request)
        elif request > head:
            right_requests.append(request)

    # Sort the requests 
    left_requests.sort()
    right_requests.sort()

    # Picking the request direction
    runs = [left_requests[::-1], right_requests] if direction == "left" else [right_requests, left_requests[::-1]]

    # Calculate head movements
    for requests in runs:
        for current_track in requests:
            distance = abs(current_track - head)
            head_movements += distance
            head = current_track

    return head_movements


#     | --------------------------------------|
#     |               C-SCAN                  |
#     |---------------------------------------|

def CSCAN(initial_position, requests):
    disk_size = 5000
    head_movements = 0
    head = initial_position

    # Cylinder positions according to direction
    left_requests = [0]
    right_requests = [disk_size - 1]

    # Dividing the requests to either left or right
    for request in requests:
        if request < head:
            left_requests.append(request)
        else:
            right_requests.append(request)

    # Process the right requests
    for current_track in right_requests:
        head_movements += abs(current_track - head)
        head = current_track

    # Go to the beginning of disk
    head_movements += (disk_size - 1)
    head = 0

    # Process the left requests
    for current_track in left_requests:
        head_movements += abs(current_track - head)
        head = current_track

    return head_movements

def CSCAN_optimized(initial_position, requests):
    disk_size = 5000
    head_movements = 0
    head = initial_position

    # Cylinder positions according to direction
    left_requests = [0]
    right_requests = [disk_size - 1]

    # Dividing the requests to either left or right
    for request in requests:
        if request < head:
            left_requests.append(request)
        else:
            right_requests.append(request)

    # Sort the requests 
    left_requests.sort()
    right_requests.sort()

    # Process the right requests
    for current_track in right_requests:
        head_movements += abs(current_track - head)
        head = current_track

     # Go to the beginning of disk
    head_movements += (disk_size - 1)
    head = 0

    # Process the left requests
    for current_track in left_requests:
        head_movements += abs(current_track - head)
        head = current_track

    return head_movements

if __name__ == "__main__":
    # Read requests from txt file
    with open("cylinder_requests.txt", "r") as file:
        requests = [int(line.strip()) for line in file]
    
    # Initial disk setup
    initial_position = requests[0]
    requests = requests[1:]
    
    # Task 1 (Before Optimization)
    print("\nTask 1 (Before Optimization):")
    print("FCFS total head movements:", FCFS(initial_position, requests))
    print("SCAN total head movements:", SCAN(initial_position, requests, direction="left"))
    print("C-SCAN total head movements:", CSCAN(initial_position, requests))

    # Task 2 (Optimized)
    print("\nTask 2 (Optimized):")
    print("FCFS total head movements:", FCFS_optimized(initial_position, requests))
    print("SCAN total head movements:", SCAN_optimized(initial_position, requests, direction="left"))
    print("C-SCAN total head movements:", CSCAN_optimized(initial_position, requests))
    
    # Program termination
    sys.exit(1)
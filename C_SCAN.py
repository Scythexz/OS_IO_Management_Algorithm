class DiskArm:
    def __init__(self, initial_position, disk_size):
        """
        Initializes the disk arm with its initial position and disk size.
        """
        self.position = initial_position
        self.disk_size = disk_size
        self.total_head_movement = 0

    def calculate_head_movement(self, requests):
        """
        Processes the requests using the C-SCAN algorithm, calculates total head movement,
        and returns the order of requests served.
        """
        requests.append(self.disk_size - 1)  # Add the last track of the disk
        requests.append(0)  # Add the first track for circular behavior
        requests.sort()  # Sort all requests

        # Split the requests into two groups: 
        # those greater than or equal to the current position, and the rest
        higher = [r for r in requests if r >= self.position]
        lower = [r for r in requests if r < self.position]

        # C-SCAN visits the higher tracks first, then wraps to the beginning
        order_of_service = higher + lower

        # Calculate total head movement
        for request in order_of_service:
            movement = abs(self.position - request)
            self.total_head_movement += movement
            self.position = request
        
        return order_of_service


def main():
    print("I/O Management Simulation Using C-SCAN Scheduling Algorithm")
    
    # Input the initial position of the disk arm
    initial_position = int(input("Enter the initial position of the disk arm: "))
    
    # Input the disk size (total number of tracks)
    disk_size = int(input("Enter the disk size (total number of tracks): "))
    
    # Input the sequence of track requests
    requests = list(map(int, input("Enter the sequence of track requests (space-separated): ").split()))
    
    # Create an instance of the DiskArm class
    disk_arm = DiskArm(initial_position, disk_size)
    
    # Process the requests and calculate the total head movement
    order_of_service = disk_arm.calculate_head_movement(requests)
    
    # Output results
    print("\nOrder of Requests Served:")
    print(" -> ".join(map(str, order_of_service)))
    
    print("\nTotal Head Movement:")
    print(disk_arm.total_head_movement)


if __name__ == "__main__":
    main()

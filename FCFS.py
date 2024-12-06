class DiskArm:
    def __init__(self, initial_position):
        """
        Initializes the disk arm with its initial position.
        """
        self.position = initial_position
        self.total_head_movement = 0

    def calculate_head_movement(self, requests):
        """
        Processes the requests using the FCFS algorithm, calculates total head movement,
        and returns the order of requests served.
        """
        order_of_service = []
        for request in requests:
            # Calculate head movement for the current request
            movement = abs(self.position - request)
            self.total_head_movement += movement
            
            # Move the disk arm to the requested track
            self.position = request
            order_of_service.append(request)
        return order_of_service


def main():
    print("I/O Management Simulation Using FCFS Scheduling Algorithm")
    
    # Input the initial position of the disk arm
    initial_position = int(input("Enter the initial position of the disk arm: "))
    
    # Input the sequence of track requests
    requests = list(map(int, input("Enter the sequence of track requests (space-separated): ").split()))
    
    # Create an instance of the DiskArm class
    disk_arm = DiskArm(initial_position)
    
    # Process the requests and calculate the total head movement
    order_of_service = disk_arm.calculate_head_movement(requests)
    
    # Output results
    print("\nOrder of Requests Served:")
    print(" -> ".join(map(str, order_of_service)))
    
    print("\nTotal Head Movement:")
    print(disk_arm.total_head_movement)


if __name__ == "__main__":
    main()
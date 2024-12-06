class DiskArm:
    def __init__(self, initial_position):
        """
        Initializes the disk arm with its initial position.
        """
        self.position = initial_position
        self.total_head_movement = 0

    def calculate_head_movement(self, requests):
        """
        Processes the requests using the C-LOOK algorithm, calculates total head movement,
        and returns the order of requests served.
        """
        requests.sort()  # Sort all requests in ascending order

        # Split requests into two groups:
        # those greater than or equal to the current position, and the rest
        higher = [r for r in requests if r >= self.position]
        lower = [r for r in requests if r < self.position]

        # C-LOOK serves the higher requests first, then jumps to the smallest request
        order_of_service = higher + lower

        # Calculate total head movement
        for request in order_of_service:
            movement = abs(self.position - request)
            self.total_head_movement += movement
            self.position = request
        
        return order_of_service


def main():
    print("I/O Management Simulation Using C-LOOK Scheduling Algorithm")
    
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

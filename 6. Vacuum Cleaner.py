class VacuumCleaner:
    def __init__(self):
        self.location = 0  # 0 represents location A, 1 represents location B
        self.environment = ['Dirty', 'Dirty']  # Initial dirt condition in both locations

    def sense(self):
        """Returns the dirt condition of the current location."""
        return self.environment[self.location]

    def clean(self):
        """Cleans the current location."""
        self.environment[self.location] = 'Clean'
        print(f"Cleaned location {self.location}")

    def move(self):
        """Moves the vacuum cleaner to the other location."""
        if self.location == 0:
            print("Moving to location B")
            self.location = 1
        else:
            print("Moving to location A")
            self.location = 0

    def run(self):
        """Executes the vacuum cleaner's cleaning strategy."""
        print("Starting vacuum cleaner...")
        
        # Loop until all locations are clean
        for _ in range(2):  # In this simple example, we only need 2 iterations to clean both locations
            dirt_condition = self.sense()
            if dirt_condition == 'Dirty':
                print(f"Location {self.location} is dirty.")
                self.clean()
            else:
                print(f"Location {self.location} is already clean.")
            
            print("Moving to next location...")
            self.move()
        
        print("Cleaning complete!")
        print(f"Final environment state: {self.environment}")

if __name__ == "__main__":
    vacuum = VacuumCleaner()
    vacuum.run()

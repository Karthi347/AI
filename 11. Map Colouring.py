# Define the map and constraints
class MapColoringCSP:
    def __init__(self, regions, colors, neighbors):
        self.regions = regions
        self.colors = colors
        self.neighbors = neighbors
        self.assignment = {region: None for region in self.regions}
    
    def is_valid(self, region, color):
        for neighbor in self.neighbors[region]:
            if self.assignment[neighbor] == color:
                return False
        return True
    
    def select_unassigned_region(self):
        for region in self.regions:
            if self.assignment[region] is None:
                return region
        return None
    
    def backtracking_search(self):
        if all(self.assignment[region] is not None for region in self.regions):
            return self.assignment
        
        region = self.select_unassigned_region()
        for color in self.colors:
            if self.is_valid(region, color):
                self.assignment[region] = color
                result = self.backtracking_search()
                if result:
                    return result
                self.assignment[region] = None
        
        return None

# Example usage
if __name__ == "__main__":
    regions = ["A", "B", "C", "D", "E"]
    colors = ["Red", "Green", "Blue"]
    neighbors = {
        "A": ["B", "C", "D"],
        "B": ["A", "C", "E"],
        "C": ["A", "B", "D", "E"],
        "D": ["A", "C", "E"],
        "E": ["B", "C", "D"]
    }

    csp = MapColoringCSP(regions, colors, neighbors)
    solution = csp.backtracking_search()
    if solution:
        print("Solution found:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")

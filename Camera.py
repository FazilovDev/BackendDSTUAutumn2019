class Camera:
    def __init__(self, id):
        self.id = id
        self.density = 0
        self.densities = []

    
    def get_id(self):
        return self.id
    
    def add_density(self, density):
        if (len(self.densities) == 2):
            self.density = self.densities[0] + self.densities[1]
        self.densities = []
        self.densities.append(density)

    def get_density(self):
        return self.density

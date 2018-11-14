class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        print(obstacles)
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(8)] for _ in range(6)]
        self.map[5][7] = 1  # Источники света
        self.map[3][2] = 1  # Источники света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)



class MappingAdapter:
    def __init__(self, adapter):
        self.adapter = adapter

    def lighten(self, grid):
        for i in grid:
            print(i)
        self.grid = grid
        dim = (len(grid[0]), len(grid))
        lights = self.get_map_items('lights', dim)
        obstacles = self.get_map_items('obstacles', dim)
        self.adapter.set_dim(dim,)
        self.adapter.set_lights(lights)
        self.adapter.set_obstacles(obstacles)
        return self.adapter.generate_lights()

    def get_map_items(self, items, dim):
        mark = 1 if items == 'lights' else None
        mark = -1 if items == 'obstacles' else mark
        if mark is not None:
            return [(y, x) for x in range(dim[1]) for y in range(dim[0]) if self.grid[x][y] == mark]





def main():
    print(123)
    system = System()
    dim = (3, 3)
    light_mapper = Light(dim)
    adapter = MappingAdapter(light_mapper)

    system.get_lightening(adapter)
    print(system.lightmap)


if __name__ == "__main__":
    main()

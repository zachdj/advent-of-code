from pathlib import Path


class Sensor:
    def __init__(self, x, y, range_):
        self.x = x
        self.y = y
        self.range = range_

    def covers_cell(self, x, y):
        return (abs(self.x - x) + abs(self.y - y)) <= self.range

    def cells_on_radius(self, lim=4_000_000):
        """Generator for cells along the radius of this sensor"""
        # four points just outside the radius
        top_x, top_y = self.x, self.y - self.range - 1
        bottom_x, bottom_y = self.x, self.y + self.range + 1
        left_x, left_y = self.x - self.range - 1, self.y
        right_x, right_y = self.x + self.range + 1, self.y

        # from top to right
        point_x, point_y = top_x, top_y
        while point_x <= right_x:
            if point_x in range(lim + 1) and point_y in range(lim + 1):
                yield point_x, point_y
            point_x += 1
            point_y += 1

        # from bottom to right
        point_x, point_y = bottom_x, bottom_y
        while point_x <= right_x:
            if point_x in range(lim + 1) and point_y in range(lim + 1):
                yield point_x, point_y
            point_x += 1
            point_y -= 1

        # from top to left
        point_x, point_y = top_x, top_y
        while point_x >= left_x:
            if point_x in range(lim + 1) and point_y in range(lim + 1):
                yield point_x, point_y
            point_x -= 1
            point_y += 1

        # from bottom to left
        point_x, point_y = bottom_x, bottom_y
        while point_x >= left_x:
            if point_x in range(lim + 1) and point_y in range(lim + 1):
                yield point_x, point_y
            point_x -= 1
            point_y -= 1


def task1(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    target_y = 2_000_000
    non_beacon_cells = set()
    beacons_on_y = set()
    for line in puzzle:
        colon_idx = line.index(":")
        sensor_x, sensor_y = (int(coord) for coord in line[len("Sensor at x="):colon_idx].split(", y="))
        beacon_x, beacon_y = (int(coord) for coord in line[colon_idx + 1 + len(" closest beacon is at x="):].split(", y="))
        dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        if beacon_y == target_y:
            beacons_on_y.add(f"{beacon_x}_{beacon_y}")

        # scan row
        for x in range(sensor_x - dist, sensor_x + dist):
            dist_to_cell = abs(sensor_x - x) + abs(sensor_y - target_y)
            if dist_to_cell <= dist:
                non_beacon_cells.add(f"{x}_{target_y}")

    print(f"Part 1 solution: {len(non_beacon_cells) - len(beacons_on_y)}")


def task2(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    lim = 4_000_000
    # lim = 20
    sensors = []
    for line in puzzle:
        colon_idx = line.index(":")
        sensor_x, sensor_y = (int(coord) for coord in line[len("Sensor at x="):colon_idx].split(", y="))
        beacon_x, beacon_y = (int(coord) for coord in
                              line[colon_idx + 1 + len(" closest beacon is at x="):].split(", y="))
        dist_covered = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        sensors.append(Sensor(sensor_x, sensor_y, dist_covered))

    for idx, s in enumerate(sensors):
        # search the radius of all sensors
        for candidate_x, candidate_y in s.cells_on_radius(lim=lim):
            # check if point is covered by another sensor
            covered = False
            for sensor in sensors:
                covered = covered or sensor.covers_cell(candidate_x, candidate_y)

            if not covered:
                print(candidate_x, candidate_y)
                print(f"Task 2 solution: {4_000_000 * candidate_x + candidate_y}")
                print("Happy Haul-in Days!")
                exit(0)

        print(f"Done with sensor {idx+1}")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day15.txt"
    task1(input_path)
    task2(input_path)

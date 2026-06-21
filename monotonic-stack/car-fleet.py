class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse = True)
        times = []
        for i in range(len(position)):
            times.append((target-cars[i][0])/cars[i][1])
        fleets = 0
        max_time_so_far = 0
        for time in times:
            if time > max_time_so_far:
                fleets += 1
                max_time_so_far = time
        return fleets

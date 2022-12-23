from typing import List


class SolutionMaximumUnitsTruck:
    def maximumUnits(self, box_types: List[List[int]], truck_size: int) -> int:
        box_types.sort(key=lambda x: x[1], reverse=True)
        for box in box_types:
            pass


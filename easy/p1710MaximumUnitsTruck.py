from typing import List


class SolutionMaximumUnitsTruck:
    def maximum_units(self, box_types: List[List[int]], truck_size: int) -> int:
        # sorting in based on units per box in descending order
        box_types.sort(key=lambda x: x[1], reverse=True)

        unit_count = 0

        # loading boxes onto truck
        for box_type in box_types:
            box_count = min(box_type[0], truck_size)  # to ensure number of boxes on the truck should not
            # exceed truckSize
            unit_count = unit_count + box_count * box_type[1]
            truck_size = truck_size - box_count
            if truck_size == 0:
                break

        return unit_count

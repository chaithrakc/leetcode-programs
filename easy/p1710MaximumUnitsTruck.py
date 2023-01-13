from typing import List


class SolutionMaximumUnitsTruck:
    def maximum_units(self, box_types: List[List[int]], truck_size: int) -> int:

        # sorting in based on units per box in descending order
        box_types.sort(key=lambda x: x[1], reverse=True)

        boxes_loaded = 0
        max_units = 0

        # iterating over each box
        for box_type in box_types:
            num_boxes = box_type[0]
            num_units_per_box = box_type[1]
            # loading boxes onto truck
            for box in range(num_boxes):
                if boxes_loaded >= truck_size:  # number of boxes on the truck should not exceed truckSize
                    return max_units
                boxes_loaded = boxes_loaded + 1
                max_units = max_units + num_units_per_box

        # use case: number of boxes provided are less than truck size
        return max_units







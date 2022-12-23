from typing import List

import pytest

from easy.p1710MaximumUnitsTruck import SolutionMaximumUnitsTruck

max_units_truck = [
    ([[1, 3], [2, 2], [3, 1]], 4, 8),
    ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91),
]


class TestSolutionMaximumUnitsTruck:
    solution = SolutionMaximumUnitsTruck()

    @pytest.mark.parametrize('box_types, truck_size, max_units', max_units_truck)
    def test_maximum_units(self, box_types: List[List[int]], truck_size: int, max_units: int):
        assert self.solution.maximumUnits(box_types, truck_size) == max_units

"""Example array problem template.

Problem: Find the two numbers that add up to a target value.
"""

from typing import List, Optional, Tuple


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Return indices of the two numbers that add up to target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return None


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))

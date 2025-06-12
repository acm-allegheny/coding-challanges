"""Second coding challange."""

from typing import List

"""
---------------------------
Description of the problem.
---------------------------

In the second challange you need to use your programming skills a little more! Implement a function
that returns the largest member of a list. This is a common python exercise that will take you to the next
step to think as a programmer. To make this task even harder you ARE NOT allowed to use the max() built-in
function.

NOTE: We only work with a list that contains 3 integer numbers, so implement your algorithm based on that fact!
"""

def problem_solution(list: List[int]):
    last_elem = list[-1]
    for num in list:
        for sec_num in list:
            if num > sec_num:
                return num
            elif num < sec_num:
                return sec_num
            else:
                return last_elem

if __name__ == "__main__":
    my_list = [110, 200, 30]
    solution = problem_solution(my_list)
    print(solution)

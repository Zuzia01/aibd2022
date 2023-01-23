import pytest
from app import bubblesort

In1 = [1, 2, 3, 4, 5]
Out1 = [1, 2, 3, 4, 5]

In2 = [0, -4, 6, 10, -1]
Out2 = [-4, -1, 0, 6, 10]

In3 = [10, 40, 25, 74, 33]
Out3 = [10, 25, 33, 40, 74]

In4 = [6, 8, 1, 5, 6, 5, 4]
Out4 = [1, 4, 5, 5, 6, 6, 8]

In5 = [8, 1, 8, 4, 4, 3, 4, 8, 4, 2, 1, 3, 2, 4, 8, 4, 5, 2, 1, 3]
Out5 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 8, 8, 8, 8]

test_data = [(In1,Out1),(In2,Out2),(In3,Out3),(In4,Out4),(In5,Out5)]

@pytest.mark.parametrize('unsorted, expected', test_data)
def test_bubblesort(unsorted,expected):
    output = bubblesort(unsorted)
    assert output == expected
    

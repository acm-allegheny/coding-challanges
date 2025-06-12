import pytest
from code.q_01 import *

def test_first_name():
    """Test case for the first_name function."""
    usr_first_name = first_name()
    assert type(usr_first_name) is str

def test_first_name_count():
    f_name = first_name()
    assert len(f_name) > 0


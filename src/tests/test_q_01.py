import pytest
from code.q_01 import *

def test_first_name():
    """Test case for the first_name function."""
    usr_first_name = first_name()
    assert type(usr_first_name) is str

def test_first_name_count():
    f_name = first_name()
    assert len(f_name) > 0

def test_second_name():
    usr_second_name = last_name()
    assert type(usr_second_name) is str

def test_second_name_count():
    s_name = last_name()
    assert len(s_name) > 0
 

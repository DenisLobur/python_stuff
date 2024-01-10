from name_function import get_formatted_name


def test_first_last_name():
    """Do names like Jim Bim work?"""
    formatted_name = get_formatted_name("jim", "bim")
    assert formatted_name == "Jim Bim"


def test_with_middle_name():
    formatted_name = get_formatted_name("jim", "bim", "jose")
    assert formatted_name == "Jim Jose Bim"


def test_going_fail():
    """A test that always fails"""
    assert 1 == 2

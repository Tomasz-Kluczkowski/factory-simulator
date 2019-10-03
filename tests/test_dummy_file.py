from dummy_package.dummy_file import dummy_function_to_test


def test_dummy_function_less_or_equal():
    assert dummy_function_to_test(10) == 'less than or equal to ten'


# def test_dummy_function_greater():
#     assert dummy_function_to_test(11) == 'greater than ten'

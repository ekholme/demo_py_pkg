from demo_py_pkg import demo_py_pkg

def test_demo_py_pkg():
    assert demo_py_pkg.add_numbers(1, 2) == 3
    assert demo_py_pkg.subtract_numbers(1, 2) == -1
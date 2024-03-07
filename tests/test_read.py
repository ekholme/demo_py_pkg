from demo_py_pkg import read
import polars as pl

def test_read_csv():
    demo = read.read_csv("tests/demo_df.csv")
    assert isinstance(demo, pl.DataFrame)

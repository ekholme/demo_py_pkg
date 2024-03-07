import polars as pl

def read_csv(filename):
   """Read a CSV file into a Polars DataFrame.

   Just a wrapper around polars.read_csv() for illustration purposes (to include a dependency in the example pkg)

   Parameters
   ----------
   filename: str
      The name of the CSV file to read

   Returns
   -------
   DataFrame
      A Polars DataFrame

   Examples
   --------
   >>> df = read.read_csv("data.csv")
   """
   return pl.read_csv(filename)
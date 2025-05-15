import pathlib
p = pathlib.Path("/Users/takeo/Downloads").glob("*.csv") 
print(p)
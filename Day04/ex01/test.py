from FileLoader import FileLoader
from YoungestFellah import youngest_fellah


loader = FileLoader()
data = loader.load("../athlete_events.csv")
loader.display(data, 5)
print(youngest_fellah(data, 1988))

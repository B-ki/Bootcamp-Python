from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport


loader = FileLoader()
data = loader.load("../athlete_events.csv")
loader.display(data, 5)
print(proportion_by_sport(data, 2004, 'Tennis', 'F'))

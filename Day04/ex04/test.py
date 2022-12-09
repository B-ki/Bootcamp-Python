from FileLoader import FileLoader
from MyPlotLib import histogram


loader = FileLoader()
data = loader.load("../athlete_events.csv")
histogram(data, 'Weight')

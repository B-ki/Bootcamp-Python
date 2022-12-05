from datetime import datetime
kata = (2019, 9, 25, 3, 30)
time = datetime(*kata)
print(time.isoformat(" ", "minutes"))

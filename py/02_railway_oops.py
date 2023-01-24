#import pandas as pd

#pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
KiranApplication = RailwayForm()
KiranApplication.name = "Kiran"
KiranApplication.train = "Rajdhani Express"
KiranApplication.printData()

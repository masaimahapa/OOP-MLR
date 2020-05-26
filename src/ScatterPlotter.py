import matplotlib.pyplot as plt
from .Plotter import Plotter

class ScatterPlotter(Plotter):
    def __init__(self, y, y_pred):
        super().__init__(y, y_pred)
    def plot(self):
        plt.scatter(self.y_pred, self.residuals )
        #plt.scatter(self.y, self.y_pred)
        plt.title('Predictions vs actual values')
        plt.ylabel('residuals')
        plt.xlabel('predictions')

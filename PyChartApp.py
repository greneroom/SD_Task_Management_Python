from bokeh._glyph_functions import circle
from bokeh.models import HBox
from matplotlib import pyplot as plt
import seaborn as sns
import time
from ProcessManager import ProcessManager

__author__ = 'davidabrahams & tomheale'

class PyChartApp:

    def __init__(self):
        self.proc_manager = ProcessManager()

    def plot(self):
        plt.clf()
        data = self.proc_manager.data
        keys = data.keys()
        indices_to_remove = []
        vals = []
        for i, k in enumerate(keys):
            cpu, ram =  data[k]
            if cpu < 1.0:
                indices_to_remove.append(i)
            else:
                vals.append(cpu)
        for i in reversed(indices_to_remove):
            keys.pop(i)
        print(plt.pie(vals, labels=keys))
        plt.show()

    def update(self):
        self.proc_manager.update()

if __name__ == '__main__':
    p = PyChartApp()
    while True:
        p.update()
        p.plot()
        time.sleep(0.1)

import matplotlib.pyplot as plt
from collections import Counter

class Visualizer:
    def __init__(self, entries):
        self.entries = entries

    def plot_level_counts(self, show=True, savepath=None):
        counts = Counter(e.level for e in self.entries)
        levels = list(counts.keys())
        values = [counts[l] for l in levels]
        plt.figure(figsize=(6,4))
        plt.bar(levels, values)
        plt.title('Log entries by level')
        plt.xlabel('Level')
        plt.ylabel('Count')
        if savepath:
            plt.savefig(savepath, bbox_inches='tight')
        if show:
            plt.show()
        plt.close()

"""
Practice: Matplotlib & Seaborn
"""
import matplotlib.pyplot as plt
import seaborn as sns

def plot_demo():
    # Line plot
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], marker='o')
    plt.title("Line Chart")
    plt.xlabel("X")
    plt.ylabel("Y")

    # Scatter plot
    plt.subplot(1, 2, 2)
    x = [1, 2, 3]
    y = [2, 4, 1]
    plt.scatter(x, y, color='red')
    plt.title("Scatter Plot")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.tight_layout()
    plt.savefig("plot.png")  # saves instead of showing (for non-interactive envs)
    print("Plot saved as 'plot.png'")

if __name__ == "__main__":
    plot_demo()

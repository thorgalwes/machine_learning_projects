# Hands on Machine Learning: Chapter 4 – Training Models

# Python STL
import sys
from packaging import version
from pathlib import Path

# Packages
import sklearn
import matplotlib.pyplot as plt

# Assert versions
assert sys.version_info >= (3, 7) # python 3.7
assert version.parse(sklearn.__version__) >= version.parse("1.0.1") # scikitlearn 1.0.1

# matplotlib configuration
plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

# Paths
IMAGES_PATH = Path() / "images" / "training_linear_models"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

# Linear Regression
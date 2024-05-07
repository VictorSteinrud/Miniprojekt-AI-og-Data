import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True)
X = MinMaxScaler().fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise

print(y)

import matplotlib.pyplot as plt


def plot_digits(X, title, nrows=10, ncols=10):
    """Helper function to plot digits."""
    fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10, 10), subplot_kw={'xticks':[], 'yticks':[]})
    for i, ax in enumerate(axs.flat):
        ax.imshow(X[i].reshape(16, 16), cmap='Greys', interpolation='nearest')
        ax.axis('off')
    plt.suptitle(title, fontsize=24)
    plt.show()

# Plot the uncorrupted test images
plot_digits(X_test, "Uncorrupted test images")

# Plot the noisy test images
plot_digits(X_test_noisy, "Noisy test images")


from sklearn.decomposition import PCA, KernelPCA

pca = PCA(n_components=32, random_state=42)
kernel_pca = KernelPCA(
    n_components=400,
    kernel="rbf",
    gamma=1e-3,
    fit_inverse_transform=True,
    alpha=5e-3,
    random_state=42,
)

pca.fit(X_train_noisy)
_ = kernel_pca.fit(X_train_noisy)
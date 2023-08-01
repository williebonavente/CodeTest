import numpy as np
import matplotlib.pyplot as plt

def pca(data):
  """
  Performs principal component analysis on a dataset.

  Args:
    data: The dataset to be analyzed.

  Returns:
    The principal components of the dataset.
  """

  covariance = np.cov(data.T)
  eigenvalues, eigenvectors = np.linalg.eig(covariance)
  principal_components = eigenvectors.T

  return principal_components


if __name__ == "__main__":
  data = np.random.randn(100, 3)
  principal_components = pca(data)

  plt.plot(principal_components[:, 0], principal_components[:, 1], "o")
  plt.show()

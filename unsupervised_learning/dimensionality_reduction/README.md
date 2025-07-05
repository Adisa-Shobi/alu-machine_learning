# dimensionality_reduction
This directory contains work with decomposition and reducing dimensions:

## Mandatory Tasks:

| Task # | Task Name | Description | File |
|--------|-----------|-------------|------|
| 0 | PCA | Write a function that performs PCA (principal components analysis) on a dataset using var, the fraction of the variance that the PCA transformation should maintain. | [0-pca.py](/unsupervised_learning/dimensionality_reduction/0-pca.py) |
| 1 | PCA v2 | Write a function that performs PCA (principal components analysis) on a dataset using ndim, the new dimensionality of the transformed data. | [1-pca.py](/unsupervised_learning/dimensionality_reduction/1-pca.py) |

## Advanced Tasks:

| Task # | Task Name | Description | File |
|--------|-----------|-------------|------|
| 2 | Initialize t-SNE | Write a function that initializes all variables required to calculate the P affinities in t-SNE. | [2-P_init.py](/unsupervised_learning/dimensionality_reduction/2-P_init.py) |
| 3 | Entropy | Write a function that calculates the Shannon entropy and P affinities relative to a data point. | [3-entropy.py](/unsupervised_learning/dimensionality_reduction/3-entropy.py) |
| 4 | P affinities | Write a function that calculates the symmetric P affinities of a data set. | [4-P_affinities.py](/unsupervised_learning/dimensionality_reduction/4-P_affinities.py) |
| 5 | Q affinities | Write a function that calculates the Q affinities. | [5-Q_affinities.py](/unsupervised_learning/dimensionality_reduction/5-Q_affinities.py) |
| 6 | Gradients | Write a function that calculates the gradients of Y. | [6-grads.py](/unsupervised_learning/dimensionality_reduction/6-grads.py) |
| 7 | Cost | Write a function that calculates the cost of the t-SNE transformation. | [7-cost.py](/unsupervised_learning/dimensionality_reduction/7-cost.py) |
| 8 | t-SNE | Write a function that performs a t-SNE transformation and finds the optimized low dimensional transformation of the dataset. | [8-tsne.py](/unsupervised_learning/dimensionality_reduction/8-tsne.py) |

### test_files directory
The test_files directory contains all files used to test output locally.

### data directory
The data directory contains datasets to test the code with.
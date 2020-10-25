# Clustering Repository

## Learning Goals

1. Be able to discuss and discover use cases for clustering across multiple industries.

2. Be able to recognize of common clustering algorithms.

3. General understanding of how the k-means clustering algorithm works.

4. Ability to implement k-means clustering in python.

5. Ability to make use of clusters discovered later down the data science pipeline.


## Vocabulary

### Euclidean Distance

The shortest distance between two points in n-dimensional space, a.k.a. L2 distance.


### Manhattan Distance

The distance between two points is the sum of the absolute differences of their Cartesian coordinates. Also known as: taxicab metric, rectilinear distance, snake distance, city block distance, or Manhattan length.

### Cosine Similarity

Cosine Similarity measures the cosine of the angle between two vectors to define similarity between two vectors. It is a measure of orientation and not magnitude: two vectors with the same orientation, i.e. parallel, have a cosine similarity of 1 indicating they are maximally "similar". Two vectors oriented at 90° relative to each other, i.e. perpendicular or orthogonal, have a similarity of 0 and are considered maximally "dissimilar". If two vectors diametrically opposed (180∘) have a similarity of -1. The cosine similarity is particularly used where the outcome is neatly bounded in [0,1].

### Sparse vs. Desnse Matrix

A sparse matrix is a matrix in which most of the elements are zero. By contrast, if most of the elements are nonzero, then the matrix is considered dense.

The number of zero-valued elements divided by the total number of elements (e.g., m × n for an m × n matrix) is called the sparsity of the matrix (which is equal to 1 minus the density of the matrix). Using those definitions, a matrix will be sparse when its sparsity is greater than 0.5.

### Manhattan (Taxicab) vs Euclidean Distance
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Manhattan_distance.svg/1200px-Manhattan_distance.svg.png">

In taxicab geometry, the red, yellow, and blue paths all have the same shortest path length of 12. In Euclidean geometry, the green line has length 6√2≈8.49 and is the unique shortest path.

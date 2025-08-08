from common import *

ITERATIONS = 10
TOLERANCE = 1e-4
NSAMPLES = NSIZE
NFEATURES = 256
K = 20

@pytest.mark.parametrize(
    "pkgid", IDS, ids=IDS
)
class TestKmeans:
    def test_kmeans(self, benchmark, pkgid):
        initialize_package(pkgid)
        pkg = PKGDICT[pkgid]
        kmean_class = { "dpnp" : kmeans_dpnp , "numpy" : kmeans_numpy, \
         "cupy" : kmeans_cupy , "arrayfire" : kmeans_af }
        obj = kmean_class[pkg.__name__]()

        benchmark.extra_info["description"] = f"{NSAMPLES}x{NFEATURES} over {K} centers"
        result = benchmark.pedantic(
            target=obj.kmeans,
            rounds=ROUNDS,
            iterations=1
        )

class kmeans_numpy:
    def __init__(self):
        self.data = np.random.random((NSAMPLES, NFEATURES))
        self.centroid_indices = np.random.choice(self.data.shape[0], K, replace=False)

    def initialize_centroids(self):
        """
        Randomly initializes k centroids from the data points.

        Args:
            data (np.ndarray): The input data points (n_samples, n_features).
            k (int): The number of clusters.

        Returns:
            np.ndarray: Initial centroids (k, n_features).
        """

        return self.data[self.centroid_indices, :]

    def assign_to_clusters(self, centroids):
        """
        Assigns each data point to the closest centroid.

        Args:
            data (np.ndarray): The input data points (n_samples, n_features).
            centroids (np.ndarray): The current centroids (k, n_features).

        Returns:
            np.ndarray: An array of cluster assignments for each data point (n_samples,).
        """
        distances = np.sqrt(((self.data[:,np.newaxis,:] - centroids[np.newaxis,:,:])**2).sum(axis=2))
        cluster_assignments = np.argmin(distances, axis=1)
        return cluster_assignments

    def update_centroids(self, cluster_assignments):
        """
        Recalculates the centroids based on the mean of the assigned data points.

        Args:
            data (np.ndarray): The input data points (n_samples, n_features).
            cluster_assignments (np.ndarray): An array of cluster assignments.
            k (int): The number of clusters.

        Returns:
            np.ndarray: Updated centroids (k, n_features).
        """
        new_centroids = np.zeros((K, self.data.shape[1]))
        for i in range(K):
            points_in_cluster = self.data[cluster_assignments == i]
            if len(points_in_cluster) > 0:
                new_centroids[i] = np.mean(points_in_cluster, axis=0)
        return new_centroids

    def kmeans(self):
        """
        Performs the K-Means clustering algorithm.

        Args:
            data (np.ndarray): The input data points (n_samples, n_features).
            k (int): The number of clusters.
            max_iterations (int): Maximum number of iterations to run the algorithm.
            tolerance (float): The tolerance for convergence (change in centroids).

        Returns:
            tuple: A tuple containing:
                - np.ndarray: Final centroids (k, n_features).
                - np.ndarray: Final cluster assignments for each data point (n_samples,).
        """
        centroids = self.initialize_centroids()
        cluster_assignments = None

        for i in range(ITERATIONS):
            old_centroids = np.copy(centroids)

            # E-step: Assign points to clusters
            cluster_assignments = self.assign_to_clusters(centroids)

            # M-step: Update centroids
            centroids = self.update_centroids(cluster_assignments)

            # Check for convergence
            if np.linalg.norm(centroids - old_centroids) < TOLERANCE:
                break

        return centroids, cluster_assignments
    

class kmeans_dpnp:
    def __init__(self):
        self.data = dpnp.random.random((NSAMPLES, NFEATURES))
        self.centroid_indices = dpnp.array(np.random.choice(self.data.shape[0], K, replace=False).tolist())

    def initialize_centroids(self):
        return self.data[self.centroid_indices, :]

    def assign_to_clusters(self, centroids):
        distances = dpnp.sqrt(((self.data[:,dpnp.newaxis,:] - centroids[dpnp.newaxis,:,:])**2).sum(axis=2))
        cluster_assignments = dpnp.argmin(distances, axis=1)
        return cluster_assignments

    def update_centroids(self, cluster_assignments):
        new_centroids = dpnp.zeros((K, self.data.shape[1]))
        for i in range(K):
            points_in_cluster = self.data[cluster_assignments == i]
            if len(points_in_cluster) > 0:
                new_centroids[i] = dpnp.mean(points_in_cluster, axis=0)
        return new_centroids

    def kmeans(self):
        centroids = self.initialize_centroids()
        cluster_assignments = None
        for i in range(ITERATIONS):
            old_centroids = dpnp.copy(centroids)

            # E-step: Assign points to clusters
            cluster_assignments = self.assign_to_clusters(centroids)

            # M-step: Update centroids
            centroids = self.update_centroids(cluster_assignments)

            # Check for convergence
            if dpnp.linalg.norm(centroids - old_centroids) < TOLERANCE:
                break

        return centroids, cluster_assignments
    
class kmeans_cupy:
    def __init__(self):
        self.data = cupy.random.random((NSAMPLES, NFEATURES))
        self.centroid_indices = cupy.random.choice(self.data.shape[0], K, replace=False)
        cupy.cuda.runtime.deviceSynchronize()

    def initialize_centroids(self):
        return self.data[self.centroid_indices, :]

    def assign_to_clusters(self, centroids):
        distances = cupy.sqrt(((self.data[:,cupy.newaxis,:] - centroids[cupy.newaxis,:,:])**2).sum(axis=2))
        cluster_assignments = cupy.argmin(distances, axis=1)
        return cluster_assignments

    def update_centroids(self, cluster_assignments):
        new_centroids = cupy.zeros((K, self.data.shape[1]))
        for i in range(K):
            points_in_cluster = self.data[cluster_assignments == i]
            if len(points_in_cluster) > 0:
                new_centroids[i] = cupy.mean(points_in_cluster, axis=0)
        return new_centroids

    def kmeans(self):
        centroids = self.initialize_centroids()
        cluster_assignments = None

        for i in range(ITERATIONS):
            old_centroids = cupy.copy(centroids)

            # E-step: Assign points to clusters
            cluster_assignments = self.assign_to_clusters(centroids)

            # M-step: Update centroids
            centroids = self.update_centroids(cluster_assignments)

            # Check for convergence
            if cupy.linalg.norm(centroids - old_centroids) < TOLERANCE:
                break

        cupy.cuda.runtime.deviceSynchronize()
        return centroids, cluster_assignments
    
class kmeans_af:
    def __init__(self):
        self.data = af.Array(np.random.random((NSAMPLES, NFEATURES)).flatten().tolist(), shape=(NSAMPLES, NFEATURES))
        self.centroid_indices = af.Array(np.random.choice(self.data.shape[0], K, replace=False).tolist())

        af.eval(self.data)
        af.eval(self.centroid_indices)
        af.sync()

    def initialize_centroids(self):
        """
        Randomly initializes k centroids from the data points.

        Args:
            data (np.ndarray): The input data points (n_samples, n_features).
            k (int): The number of clusters.

        Returns:
            np.ndarray: Initial centroids (k, n_features).
        """

        return self.data[self.centroid_indices, :]
        # return af.lookup(self.data, self.centroid_indices, axis=0)

    def assign_to_clusters(self, centroids):
        """
        Assigns each data point to the closest centroid.

        Args:
            data (np.ndarray): The input data points (n_samples, n_features).
            centroids (np.ndarray): The current centroids (k, n_features).

        Returns:
            np.ndarray: An array of cluster assignments for each data point (n_samples,).
        """
        dist = (af.moddims(self.data, (NSAMPLES, 1, NFEATURES)) - af.moddims(centroids, (1, K, NFEATURES)))**2
        distances = af.sqrt(af.sum(dist, axis=2))
        cluster_assignments = af.where(distances == af.tile(af.min(distances, axis=1), (1, K)))
        # cluster_assignments = af.range((NSAMPLES, K))[distances == af.min(distances, axis=1)]
        
        return cluster_assignments

    def update_centroids(self, cluster_assignments):
        """
        Recalculates the centroids based on the mean of the assigned data points.

        Args:
            data (np.ndarray): The input data points (n_samples, n_features).
            cluster_assignments (np.ndarray): An array of cluster assignments.
            k (int): The number of clusters.

        Returns:
            np.ndarray: Updated centroids (k, n_features).
        """
        new_centroids = af.constant(0, (K, self.data.shape[1]))
        for i in range(K):
            points_in_cluster = self.data[:, af.where(cluster_assignments == i)]
            if len(points_in_cluster) > 0:
                new_centroids[i] = af.mean(points_in_cluster, axis=0)
        return new_centroids

    def kmeans(self):
        """
        Performs the K-Means clustering algorithm.

        Args:
            data (np.ndarray): The input data points (n_samples, n_features).
            k (int): The number of clusters.
            max_iterations (int): Maximum number of iterations to run the algorithm.
            tolerance (float): The tolerance for convergence (change in centroids).

        Returns:
            tuple: A tuple containing:
                - np.ndarray: Final centroids (k, n_features).
                - np.ndarray: Final cluster assignments for each data point (n_samples,).
        """
        centroids = self.initialize_centroids()
        cluster_assignments = None

        for i in range(ITERATIONS):
            old_centroids = af.copy_array(centroids)

            # E-step: Assign points to clusters
            cluster_assignments = self.assign_to_clusters(centroids)

            # M-step: Update centroids
            centroids = self.update_centroids(cluster_assignments)

            # Check for convergence
            if af.norm(centroids - old_centroids) < TOLERANCE:
                break

        af.eval(centroids)
        af.eval(cluster_assignments)
        af.sync()
        return centroids, cluster_assignments
from common import *

INPUT_SIZE = 28 * 28
HIDDEN_SIZE = 1000
OUTPUT_SIZE = 10
LEARNING_RATE = 0.01
ITERATIONS = 10
BATCH_SIZE = 2560
SAMPLES = 25600

@pytest.mark.parametrize(
    "pkgid", IDS, ids=IDS
)
class TestNeuralNetwork:
    def test_neural_network(self, benchmark, pkgid):
        initialize_package(pkgid)
        pkg = PKGDICT[pkgid]
        nn = { "dpnp" : NeuralNetwork_dpnp , "numpy" : NeuralNetwork_numpy, \
         "cupy" : NeuralNetwork_cupy , "arrayfire" : NeuralNetwork_af }
        
        obj = nn[pkg.__name__]()

        benchmark.extra_info["description"] = f"{INPUT_SIZE}x{HIDDEN_SIZE}x{OUTPUT_SIZE} trained with {SAMPLES:.2e} samples"
        result = benchmark.pedantic(
            target=obj.train,
            rounds=ROUNDS,
            iterations=1
        )


class NeuralNetwork_numpy:
    def __init__(self):
        self.input_size = INPUT_SIZE
        self.hidden_size = HIDDEN_SIZE
        self.output_size = OUTPUT_SIZE
        self.learning_rate = LEARNING_RATE

        # Initialize weights and biases
        # He initialization (for ReLU) is often a good choice
        self.W1 = np.random.randn(self.input_size, self.hidden_size) * np.sqrt(2. / self.input_size)
        self.b1 = np.zeros((1, self.hidden_size))
        self.W2 = np.random.randn(self.hidden_size, self.output_size) * np.sqrt(2. / self.hidden_size)
        self.b2 = np.zeros((1, self.output_size))

        self.X_train = np.random.rand(SAMPLES,INPUT_SIZE)
        self.y_train = np.zeros((SAMPLES * OUTPUT_SIZE))
        self.y_train[np.arange(SAMPLES) * OUTPUT_SIZE + np.floor(np.random.rand(SAMPLES) * OUTPUT_SIZE).astype(int)] = 1
        self.y_train = self.y_train.reshape((SAMPLES, OUTPUT_SIZE))

    def relu(self, x):
        return np.maximum(0, x)

    def relu_derivative(self, x):
        return (x > 0).astype(float)

    def softmax(self, x):
        exp_scores = np.exp(x - np.max(x, axis=1, keepdims=True)) # Subtract max for numerical stability
        return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    def forward(self, X):
        # Hidden layer
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.relu(self.z1)

        # Output layer
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.softmax(self.z2)
        return self.a2

    def backward(self, X, y, output):
        # Calculate gradients for the output layer
        error_output = output - y # Derivative of cross-entropy loss w.r.t. softmax input
        dW2 = np.dot(self.a1.T, error_output)
        db2 = np.sum(error_output, axis=0, keepdims=True)

        # Calculate gradients for the hidden layer
        error_hidden = np.dot(error_output, self.W2.T) * self.relu_derivative(self.z1)
        dW1 = np.dot(X.T, error_hidden)
        db1 = np.sum(error_hidden, axis=0, keepdims=True)

        # Update weights and biases
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1

    def train(self):
        X_train = self.X_train
        y_train = self.y_train
    
        num_samples = X_train.shape[0]

        for epoch in range(ITERATIONS):
            # Shuffle data for each epoch
            X_shuffled = X_train
            y_shuffled = y_train

            for i in range(0, num_samples, BATCH_SIZE):
                X_batch = X_shuffled[i:i + BATCH_SIZE, :]
                y_batch = y_shuffled[i:i + BATCH_SIZE, :]

                # Forward pass
                output = self.forward(X_batch)

                # Backward pass and update weights
                self.backward(X_batch, y_batch, output)

    def predict(self, X):
        return np.argmax(self.forward(X), axis=1)
    

class NeuralNetwork_dpnp:
    def __init__(self):
        self.input_size = INPUT_SIZE
        self.hidden_size = HIDDEN_SIZE
        self.output_size = OUTPUT_SIZE
        self.learning_rate = LEARNING_RATE

        # Initialize weights and biases
        # He initialization (for ReLU) is often a good choice
        self.W1 = dpnp.random.randn(self.input_size, self.hidden_size) * np.sqrt(2. / self.input_size)
        self.b1 = dpnp.zeros((1, self.hidden_size))
        self.W2 = dpnp.random.randn(self.hidden_size, self.output_size) * np.sqrt(2. / self.hidden_size)
        self.b2 = dpnp.zeros((1, self.output_size))

        self.X_train = dpnp.random.rand(SAMPLES, INPUT_SIZE)
        self.y_train = dpnp.zeros((SAMPLES * OUTPUT_SIZE))
        self.y_train[dpnp.arange(SAMPLES) * OUTPUT_SIZE + dpnp.floor(dpnp.random.rand(SAMPLES) * OUTPUT_SIZE).astype(int)] = 1
        self.y_train = self.y_train.reshape((SAMPLES, OUTPUT_SIZE))

    def relu(self, x):
        return dpnp.maximum(0, x)

    def relu_derivative(self, x):
        return (x > 0).astype(float)

    def softmax(self, x):
        exp_scores = dpnp.exp(x - dpnp.max(x, axis=1, keepdims=True)) # Subtract max for numerical stability
        return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    def forward(self, X):
        # Hidden layer
        self.z1 = dpnp.dot(X, self.W1) + self.b1
        self.a1 = self.relu(self.z1)

        # Output layer
        self.z2 = dpnp.dot(self.a1, self.W2) + self.b2
        self.a2 = self.softmax(self.z2)
        return self.a2

    def backward(self, X, y, output):
        # Calculate gradients for the output layer
        error_output = output - y # Derivative of cross-entropy loss w.r.t. softmax input
        dW2 = dpnp.dot(self.a1.T, error_output)
        db2 = dpnp.sum(error_output, axis=0, keepdims=True)

        # Calculate gradients for the hidden layer
        error_hidden = dpnp.dot(error_output, self.W2.T) * self.relu_derivative(self.z1)
        dW1 = dpnp.dot(X.T, error_hidden)
        db1 = dpnp.sum(error_hidden, axis=0, keepdims=True)

        # Update weights and biases
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1

    def train(self):
        X_train = self.X_train
        y_train = self.y_train

        num_samples = X_train.shape[0]

        for epoch in range(ITERATIONS):
            # Shuffle data for each epoch
            X_shuffled = X_train
            y_shuffled = y_train

            for i in range(0, num_samples, BATCH_SIZE):
                X_batch = X_shuffled[i:i + BATCH_SIZE, :]
                y_batch = y_shuffled[i:i + BATCH_SIZE, :]

                # Forward pass
                output = self.forward(X_batch)

                # Backward pass and update weights
                self.backward(X_batch, y_batch, output)

    def predict(self, X):
        return dpnp.argmax(self.forward(X), axis=1)
    
class NeuralNetwork_cupy:
    def __init__(self):
        self.input_size = INPUT_SIZE
        self.hidden_size = HIDDEN_SIZE
        self.output_size = OUTPUT_SIZE
        self.learning_rate = LEARNING_RATE

        # Initialize weights and biases
        # He initialization (for ReLU) is often a good choice
        self.W1 = cupy.random.randn(self.input_size, self.hidden_size) * np.sqrt(2. / self.input_size)
        self.b1 = cupy.zeros((1, self.hidden_size))
        self.W2 = cupy.random.randn(self.hidden_size, self.output_size) * np.sqrt(2. / self.hidden_size)
        self.b2 = cupy.zeros((1, self.output_size))

        self.X_train = cupy.random.rand(SAMPLES, INPUT_SIZE)
        self.y_train = cupy.zeros((SAMPLES * OUTPUT_SIZE))
        self.y_train[cupy.arange(SAMPLES) * OUTPUT_SIZE + cupy.floor(cupy.random.rand(SAMPLES) * OUTPUT_SIZE).astype(int)] = 1
        self.y_train = self.y_train.reshape((SAMPLES, OUTPUT_SIZE))

        cupy.cuda.runtime.deviceSynchronize()

    def relu(self, x):
        return cupy.maximum(0, x)

    def relu_derivative(self, x):
        return (x > 0).astype(float)

    def softmax(self, x):
        exp_scores = cupy.exp(x - cupy.max(x, axis=1, keepdims=True)) # Subtract max for numerical stability
        return exp_scores / cupy.sum(exp_scores, axis=1, keepdims=True)

    def forward(self, X):
        # Hidden layer
        self.z1 = cupy.dot(X, self.W1) + self.b1
        self.a1 = self.relu(self.z1)

        # Output layer
        self.z2 = cupy.dot(self.a1, self.W2) + self.b2
        self.a2 = self.softmax(self.z2)
        return self.a2

    def backward(self, X, y, output):
        # Calculate gradients for the output layer
        error_output = output - y # Derivative of cross-entropy loss w.r.t. softmax input
        dW2 = cupy.dot(self.a1.T, error_output)
        db2 = cupy.sum(error_output, axis=0, keepdims=True)

        # Calculate gradients for the hidden layer
        error_hidden = cupy.dot(error_output, self.W2.T) * self.relu_derivative(self.z1)
        dW1 = cupy.dot(X.T, error_hidden)
        db1 = cupy.sum(error_hidden, axis=0, keepdims=True)

        # Update weights and biases
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1

    def train(self):
        X_train = self.X_train
        y_train = self.y_train

        num_samples = X_train.shape[0]

        for epoch in range(ITERATIONS):
            # Shuffle data for each epoch
            X_shuffled = X_train
            y_shuffled = y_train

            for i in range(0, num_samples, BATCH_SIZE):
                X_batch = X_shuffled[i:i + BATCH_SIZE, :]
                y_batch = y_shuffled[i:i + BATCH_SIZE, :]

                # Forward pass
                output = self.forward(X_batch)

                # Backward pass and update weights
                self.backward(X_batch, y_batch, output)

        cupy.cuda.runtime.deviceSynchronize()

    def predict(self, X):
        return cupy.argmax(self.forward(X), axis=1)
    

class NeuralNetwork_af:
    def __init__(self):
        self.input_size = INPUT_SIZE
        self.hidden_size = HIDDEN_SIZE
        self.output_size = OUTPUT_SIZE
        self.learning_rate = LEARNING_RATE

        # Initialize weights and biases
        # He initialization (for ReLU) is often a good choice
        self.W1 = af.randn((self.input_size, self.hidden_size)) * np.sqrt(2. / self.input_size)
        self.b1 = af.constant(0, (1, self.hidden_size))
        self.W2 = af.randn((self.hidden_size, self.output_size)) * np.sqrt(2. / self.hidden_size)
        self.b2 = af.constant(0, (1, self.output_size))

        self.X_train = af.randu((SAMPLES, INPUT_SIZE))
        self.y_train = af.constant(0, (SAMPLES, OUTPUT_SIZE))
    
        self.y_train = af.constant(0, (SAMPLES, OUTPUT_SIZE))
        self.y_train[af.iota(SAMPLES), af.floor(af.randu(SAMPLES) * OUTPUT_SIZE)] = 1

        af.eval(self.X_train)
        af.eval(self.y_train)
        af.eval(self.W1)
        af.eval(self.W2)
        af.eval(self.b1)
        af.eval(self.b2)
        af.sync()

    def relu(self, x):
        selection = x > 0
        return af.select(x, 0, selection)

    def relu_derivative(self, x):
        return af.cast(x > 0, getattr(af, DTYPE))

    def softmax(self, x):
        exp_scores = af.exp(x - af.max(x, axis=1)) # Subtract max for numerical stability
        return exp_scores / af.sum(exp_scores, axis=1)

    def forward(self, X):
        # Hidden layer
        self.z1 = af.matmul(X, self.W1) + self.b1
        self.a1 = self.relu(self.z1)

        # Output layer
        self.z2 = af.matmul(self.a1, self.W2) + self.b2
        self.a2 = self.softmax(self.z2)
        return self.a2

    def backward(self, X, y, output):
        # Calculate gradients for the output layer
        error_output = output - y # Derivative of cross-entropy loss w.r.t. softmax input
        dW2 = af.matmul(self.a1.T, error_output)
        db2 = af.sum(error_output, axis=0)

        # Calculate gradients for the hidden layer
        error_hidden = af.matmul(error_output, self.W2.T) * self.relu_derivative(self.z1)
        dW1 = af.matmul(X.T, error_hidden)
        db1 = af.sum(error_hidden, axis=0)

        # Update weights and biases
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1

    def train(self):
        X_train = self.X_train
        y_train = self.y_train

        num_samples = X_train.shape[0]

        for epoch in range(ITERATIONS):
            # Shuffle data for each epoch
            X_shuffled = X_train
            y_shuffled = y_train

            for i in range(0, num_samples, BATCH_SIZE):
                X_batch = X_shuffled[i:i + BATCH_SIZE,:]
                y_batch = y_shuffled[i:i + BATCH_SIZE,:]

                # Forward pass
                output = self.forward(X_batch)

                # Backward pass and update weights
                self.backward(X_batch, y_batch, output)

        af.eval(self.W2)
        af.eval(self.b2)
        af.eval(self.W1)
        af.eval(self.b1)
        af.sync()

    def predict(self, X):
        return af.where(X == af.tile(af.max(self.forward(X), axis=1), (1, X.shape[1])))
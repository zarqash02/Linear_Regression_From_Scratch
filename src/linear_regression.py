import csv

class LinearRegression:
    def __init__(self):
        self.m = 0
        self.b = 0

    def load_data(self, file_path):
        X, Y = [], []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                X.append(float(row[0]))
                Y.append(float(row[1]))
        return X, Y

    def predict(self, x):
        return self.m * x + self.b

    def compute_cost(self, X, Y):
        total_error = 0
        n = len(X)
        for i in range(n):
            y_pred = self.predict(X[i])
            total_error += (Y[i] - y_pred) ** 2
        return total_error / n

    def fit(self, X, Y, learning_rate=0.0001, epochs=1000):
        n = len(X)
        for epoch in range(epochs):
            dm = 0
            db = 0
            for i in range(n):
                x = X[i]
                y = Y[i]
                y_pred = self.predict(x)
                error = y_pred - y
                dm += error * x
                db += error
            self.m -= (learning_rate * dm) / n
            self.b -= (learning_rate * db) / n
            if epoch % 100 == 0:
                cost = self.compute_cost(X, Y)
                print(f"Epoch {epoch}: Cost = {cost:.4f}, m = {self.m:.4f}, b = {self.b:.4f}")

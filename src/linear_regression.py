"""
linear_regression.py

Implements linear regression using gradient descent, from scratch — no external libraries.
"""

import csv

def load_data(filename='dataset.csv'):
    """
    Loads dataset from a CSV file.
    
    Parameters:
        filename (str): Path to the CSV file
        
    Returns:
        tuple: Two lists, x_values and y_values
    """
    x = []
    y = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            x.append(float(row['x']))
            y.append(float(row['y']))
    return x, y

def compute_cost(x, y, m, b):
    """
    Computes Mean Squared Error cost.
    
    Parameters:
        x (list): Input features
        y (list): Target values
        m (float): Slope
        b (float): Intercept
        
    Returns:
        float: Cost
    """
    n = len(x)
    total_error = 0
    for i in range(n):
        y_pred = m * x[i] + b
        error = y[i] - y_pred
        total_error += error ** 2
    return total_error / n

def gradient_descent(x, y, m, b, learning_rate):
    """
    Performs one step of gradient descent.
    
    Parameters:
        x (list): Input features
        y (list): Target values
        m (float): Current slope
        b (float): Current intercept
        learning_rate (float): Step size
        
    Returns:
        tuple: Updated values of m and b
    """
    n = len(x)
    m_grad = 0
    b_grad = 0

    for i in range(n):
        y_pred = m * x[i] + b
        error = y_pred - y[i]
        m_grad += x[i] * error
        b_grad += error

    m -= (learning_rate * m_grad) / n
    b -= (learning_rate * b_grad) / n

    return m, b

def train(x, y, epochs=1000, learning_rate=0.01):
    """
    Trains the linear regression model using gradient descent.
    
    Parameters:
        x (list): Input features
        y (list): Target values
        epochs (int): Number of iterations
        learning_rate (float): Step size
        
    Returns:
        tuple: Final values of m and b
    """
    m = 0
    b = 0
    for epoch in range(epochs):
        cost = compute_cost(x, y, m, b)
        if epoch % 100 == 0:
            print(f"Epoch {epoch}: Cost = {cost:.4f}, m = {m:.4f}, b = {b:.4f}")
        m, b = gradient_descent(x, y, m, b, learning_rate)
    return m, b

if __name__ == "__main__":
    x, y = load_data()
    m, b = train(x, y)
    print(f"📈 Final Model: y = {m:.2f}x + {b:.2f}")
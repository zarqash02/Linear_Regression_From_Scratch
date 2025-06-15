# 📈 Linear Regression from Scratch

👋 A small project where I built a linear regression algorithm — no NumPy, no Scikit-learn, just pure Python — to explore gradient descent and cost minimization from the ground up.

---

## 🚀 How to Run

> Make sure Python (3.7+) is installed. No external libraries are needed unless you want to visualize the output.

```bash
# Clone the repo
git clone https://github.com/zarqash02/Linear_Regression_From_Scratch.git
cd Linear_Regression_From_Scratch

# Generate the dataset
python src/generate_dataset.py

# Train the model
python src/linear_regression.py


---


📂 Project Structure

├── data/                  # Generated dataset CSV
├── notebooks/             # Jupyter notebooks and output visuals
│   └── model_output.png   # Sample regression plot
├── src/                   # Core logic for data gen and training
│   ├── generate_dataset.py
│   └── linear_regression.py
├── .gitignore
├── LICENSE
├── README.md
└── .gitattributes


---


🚀 Features
Generates a toy dataset using: y = 2x + 3 + noise

Implements gradient descent from scratch

Calculates Mean Squared Error (MSE)

Plots actual data vs predicted line using matplotlib (in notebook)

No ML libraries used — everything is written manually


---


🧠 What I Learned
How gradient descent actually updates weights step-by-step

Building machine learning logic from scratch (no black boxes!)

The role of cost functions

Core math behind linear regression


---


## 📸 Sample Output

Here's a quick look at the model’s predictions vs actual data:  
The red line shows the model's predicted regression line after training on noisy data.

![Model Output](https://raw.githubusercontent.com/zarqash02/Linear_Regression_From_Scratch/main/notebooks/model_output.png)


---


🤔 Why I Made This
As an AI student, I wanted to:

Get hands-on with core ML concepts

Understand what libraries like sklearn do behind the scenes

Strengthen my fundamentals before diving into deep learning


---


🧑‍💻 Author
Made with ❤️ by Zarqash


---


🪪 License
This project is licensed under the MIT License

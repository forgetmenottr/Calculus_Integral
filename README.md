# 🎬 Calculus Project



## ✨ Project Overview

This project is a final assignment for a **Calculus** course. It utilizes the **Manim** (Python) library to generate a high-quality animated video that visually explains the geometric definition of the **Definite Integral**.

The animation focuses on illustrating the following core concepts:
1.  The concept of **Riemann Sums** and how rectangles approximate the area under the curve.
2.  Definition of difinite and indifinite integral
3.  Applications in real-life

## 🚀 Getting Started

### ⚙️ Prerequisites

To run or modify the Manim code, you need the following installed:

* **Python:** Version 3.8 or higher.
* **Manim:** The Manim Community Edition library.
* **FFmpeg:** For rendering the video output. (optional)

### 💻 Installation

1.  **Clone the Repository:**
    ```bash
    git clone <YOUR_GITHUB_URL>
    cd <your_repo_name>
    ```

2.  **Install Manim:**
    It is recommended to use a virtual environment (`venv` or `conda`).
    ```bash
    pip install manim
    ```

### ▶️ Running the Animation

Use the `manim` command line tool to render the video.

1.  Navigate to the project root directory in your terminal.
2.  Run the Python file containing the integral scene definition:
    ```bash
    # Replace <your_file_name.py> with the actual file name (e.g., integral_definition.py)
    # Use -ql (low quality) for fast rendering, or -qh (high quality) for final output
    manim -pql <your_file_name.py> IntegralScene
    ```

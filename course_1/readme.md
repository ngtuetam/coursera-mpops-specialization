# Course 1: Introduction to Machine Learning in Production
## Week 1: Overview of the ML Lifecycle and Deployment
### **Lab**: Deploying a Deep Learning model (local setup)
- To get started, visit the following [link](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/tree/main/course1/week1-ungraded-lab) and follow the instructions there.
- Clone the repo:
    ```bash
    git clone https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public.git
    ```
#### **Method 1**: Python Virtual Environment with Conda
1. Create a virtual Environment
    ```bash
    conda create --name mlep-w1-lab python=3.8
    ```
    Active Conda virtual Environment
    ```bash
    conda activate mlep-w1-lab
    ```
2. Installing dependencies using PIP
    ```bash
    pip install -r requirements.txt
    ```
3. Launching Jupyter Lab
    ```bash
    jupyter lab
    ```
#### **Method 2**: Docker
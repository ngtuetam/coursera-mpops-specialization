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
    After execution, you will see some information printed on the terminal. Usually you will need to authenticate to use Jupyter lab. For this, copy the token that appears on your terminal, head over to http://localhost:8888/ and paste it there.
4. Running the notebook \
    Look for the `server.ipynb` file and open it to begin the lab.
#### **Method 2**: Docker
1. Pulling the image from Docker hub
    ```bash
    docker pull deeplearningai/mlepc1w1-ugl:jupyternb
    ```
2. Running a container out of the image:
    ```bash
    docker run -it --rm -p 8888:8888 -p 8000:8000 --mount type=bind,source="$(pwd)",target=/home/jovyan/work deeplearningai/mlepc1w1-ugl:jupyternb
    ```
- -it: Runs the container in an interactive mode and attaches a pseudo-terminal to it so you can check what is being printed in the standard streams of the container. This is very important since you will have to copy and paste the access token for Jupyter lab.

-  --rm: Deletes the container after stopping it.

-  -p: Allows you to map a port in your computer to a port in the container. In this case we need a port for the Jupyter server and another for the server you will run within the ungraded lab.

-  --mount: Allows you to mount a directory in your local filesystem within the container. This is very important because if no mounts are present, changes to files will not persist after the container is deleted. In this case we are mounting the current directory week1-ungraded-lab onto the /home/jovyan/work directory inside the container. \
When the container starts running you will see some information being printed in the terminal. Usually you will need to authenticate to use Jupyter lab, for this copy the token that appears on your terminal, head over to http://localhost:8888/ and paste it there.
# 🐍 Python Cloud Dev - Hello World

A simple starter project to prepare for cloud-based Python development. This project prints a greeting message using a Python script running inside a Docker container.

## 📦 Project Structure

```
python-cloud-dev/
├── Dockerfile
├── main.py
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-cloud-dev.git
cd python-cloud-dev
```

### 2. Run Locally (No Docker)

```bash
python main.py
```

### 3. Run with Docker

#### a. Build the Docker image

```bash
docker build -t hello-python .
```

#### b. Run the container

```bash
docker run hello-python
```

## 🧠 What You’ll Learn

- Basics of Python scripting
- Dockerfile syntax and image creation
- How to run Python apps inside containers
- Git version control basics

## 📂 Files Explained

| File         | Description                                  |
| ------------ | -------------------------------------------- |
| `main.py`    | A basic Python script that prints a greeting |
| `Dockerfile` | Instructions to containerize the app         |
| `README.md`  | Project documentation (this file)            |

## 🧪 Example Output

```bash
Hello, cloud world!
Welcome to the cloud, Lucas!
```

## 🛠️ Requirements

- Python 3.10+
- Docker
- Git
- VSCode or any code editor

## ✅ Next Steps

- Add input arguments to your Python script
- Connect the app to an external API
- Use FastAPI to turn the script into a web service
- Add a CI/CD pipeline (GitHub Actions)

## 📚 References

- [Python Official Docs](https://docs.python.org/3/)
- [Docker Docs](https://docs.docker.com/)
- [GitHub Docs](https://docs.github.com/)

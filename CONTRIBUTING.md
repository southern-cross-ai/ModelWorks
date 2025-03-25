# 🔧✨ Contributing to ModelWorks AI Builds

Welcome to the ModelWorks AI Builds project! We’re developing flexible and adaptable AI frameworks tailored for business and government use. Our focus is on building modular and reusable components that can be quickly adapted to meet specific needs. Your contributions help us build innovative, reliable solutions—thank you for being part of this project!

Whether you’re fixing bugs, adding new features, or improving documentation, every contribution counts. We value your time and effort and are here to support you throughout the process. Feel free to reach out if you need assistance—we’re building this together!

## 📝 Getting Started

ModelWorks AI Builds is designed to be simple, modular, and easy to deploy. We use Docker for consistent environments and leverage GPU acceleration where possible. Our stack typically includes Gradio, LangChain, and Chroma for developing adaptable AI applications.

By running everything inside Docker, we ensure compatibility and maintain a consistent setup across different environments. We encourage you to follow our Docker-based development and testing process to keep everything organized.

## 🛠️ Prerequisites

### Docker Installation

Make sure you have Docker installed and running on your system.

- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Docker Compose Guide](https://docs.docker.com/compose/)

#### Docker GPU Test:

To ensure your GPU is accessible, run:

```bash
docker run --gpus all nvidia/cuda:11.8.0-base nvidia-smi
```

## 🚀 Workflow Overview

### Fork the Repository

1. Go to the ModelWorks GitHub page and click the "Fork" button.
2. Clone your fork to your local machine:

```bash
git clone https://github.com/yourusername/ModelWorks.git
cd ModelWorks
```

3. Add the upstream remote:

```bash
git remote add upstream https://github.com/Southern-Cross-AI/ModelWorks.git
```

4. Verify your remotes:

```bash
git remote -v
```

### Build the Docker Container

Build the development environment using Docker:

```bash
docker build -t modelworks:latest .
```

### Start the Docker Container

Run the container with GPU support (if available):

```bash
docker run --gpus all -it --rm -v $(pwd):/workspace modelworks:latest /bin/bash
```

Inside the container, navigate to the workspace:

```bash
cd /workspace
```

### Make Your Code Changes

- Update any components or add new features as needed.
- Document any new dependencies added to the Dockerfile.

### Run Tests

Test your changes locally:

```bash
pytest tests/
```

For GPU-specific tests, run:

```bash
pytest --cuda tests/
```

Exit the container after testing:

```bash
exit
```

## 💡 Submitting Your Contribution

### Commit Your Changes

Stage and commit your changes:

```bash
git add .
git commit -m "Fix: Improved data processing speed"
```

### Push Your Branch

```bash
git push origin feature/my-new-feature
```

### Open a Pull Request (PR)

1. Go to your fork on GitHub and click "Compare & pull request".
2. Clearly explain your changes and why they’re needed.
3. Link any related issues or discussions.

## ✅ Pull Request Review and Testing

- Your PR will be reviewed by the maintainers and tested on GPU clusters if applicable.
- Feedback will be provided if changes are needed.
- Once approved, your PR will be merged into the main branch.

## 🤝 Community and Support

If you have questions or need help, join our Discord community or contact us via email at [support@southerncross.ai](mailto:support@southerncross.ai).

## 💡 Additional Tips

- Follow the Docker workflow to ensure consistent environments.
- Document any new dependencies or significant changes.
- Test thoroughly before submitting your PR.

Thank you for your contribution! Your efforts are invaluable to ModelWorks AI Builds! 🎉

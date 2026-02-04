# 📄 PDF Parser Project (PPP)

![Project Banner](https://placehold.co/1200x300/1e293b/38bdf8?text=PDF+Parser+Project+(PPP)&font=montserrat)
<!-- Replace the above URL with the actual banner once generated -->

**A modern, robust web application for extracting text and insights from PDF documents using multiple advanced parsing strategies.**

---

## 🌟 Overview

**PPP** is designed to provide developers and users with a flexible interface to parse PDF documents. By leveraging a **Hexagonal Architecture**, the system decouples the core parsing logic from the external interfaces, allowing for easy addition of new parsers and distinct front-end experiences.

### 🎯 Key Features

-   **🧩 Multi-Strategy Parsing:** Choose the best tool for the job.
    -   `Docling`: Advanced document structure analysis.
    -   `PyMuPDF`: Fast, high-fidelity text extraction.
    -   `PDFMiner`: Detailed layout and location data.
    -   `PyPDF2`: Lightweight metadata and basic text.
-   **⚡ Real-Time Feedback:** Instant progress updates and error reporting.
-   **🎨 Modern UI:** A responsive, dark-themed interface built with React and Tailwind CSS.
-   **🐳 Docker Ready:** Fully containerized for easy deployment.

---

## 🏗 Architecture

The project adheres to **Domain-Centric / Hexagonal Architecture** principles:

| Layer | Description |
| :--- | :--- |
| **Frontend** | React 18, TypeScript, Tailwind CSS, Vite. |
| **Backend** | Python 3.12+, FastAPI, `uv` for dependency management. |
| **Domain** | Pure business logic, isolated from frameworks. |
| **Infrastructure** | Adapters for specific libraries (Docling, PDFMiner, etc.). |

---

## 🚀 Quick Start

The fastest way to get running is via Docker.

### Prerequisites

-   Docker & Docker Compose

### Run the App

```bash
docker-compose up --build
```

Access the application:
-   **Frontend:** [http://localhost:5173](http://localhost:5173)
-   **Backend API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 👩‍💻 Developer Guide

For detailed setup instructions for specific components, please refer to their respective READMEs:

-   [**Backend Documentation**](./backend/README.md) - Setup, testing, and API details.
-   [**Frontend Documentation**](./frontend/README.md) - Components, state management, and styling.

### Project Structure

```mermaid
graph TD
    Root --> Backend
    Root --> Frontend
    Backend --> Src
    Src --> Domain
    Src --> Parsers
    Frontend --> Components
    Frontend --> Context
```

---

## 📜 License

This project is licensed under the MIT License.

# PDF Parser Project (PPP)

A modern web application for parsing PDF documents using multiple strategies. This project provides a user-friendly interface to upload PDFs, select different parsing algorithms, and view the extracted text results.

## 🏗 Architecture

The project follows a Domain-Centric / Hexagonal Architecture to ensure separation of concerns and maintainability.

### Frontend
- **Framework:** React 18 with TypeScript
- **Build Tool:** Vite
- **Styling:** Tailwind CSS
- **State Management:** React Context API
- **HTTP Client:** Native `fetch` with custom wrapper

### Backend
- **Framework:** FastAPI (Python 3.12+)
- **Dependency Management:** `uv`
- **Architecture Layers:**
  - **Domain:** Core business logic and interfaces (Ports).
  - **Application:** Use cases and orchestration.
  - **Infrastructure:** External adapters (Parsers, File System, API).

## 🚀 Features

- **Multi-Strategy Parsing:** Support for various PDF parsing libraries:
  - `PyPDF2`: Basic text extraction.
  - `PyMuPDF`: High-fidelity extraction.
  - `PDFMiner`: Layout analysis.
  - `Docling`: Advanced document processing.
- **Real-time Feedback:** Progress indicators and error handling.
- **Clean UI:** Responsive design with a sidebar for settings and a main content area for results.

## 🛠 Getting Started

### Prerequisites

- **Python:** 3.12 or higher
- **Node.js:** 20 or higher
- **uv:** An extremely fast Python package installer and resolver.

### Docker Setup

The easiest way to run the application is using Docker.

1. Build and run the application:
   ```bash
   docker-compose up --build
   ```

2. Access the services:
   - **Frontend:** `http://localhost:5173`
   - **Backend API:** `http://localhost:8000` (Docs at `/docs`)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Run the development server:
   ```bash
   uv run fastapi dev src/main.py
   ```
   The API will be available at `http://localhost:8000`.

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:5173`.

## 📂 Project Structure

For a detailed view of the directory structure, please refer to `project-structure.html`.

## 🔄 Data Flow

For a visualization of how data moves through the application, please refer to `data-flow-diagram.html`.
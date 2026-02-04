# ⚛️ PPP Frontend

The frontend for the PDF Parser Project, built with **React**, **TypeScript**, and **Tailwind CSS**. It provides a clean, modern interface for users to upload files, configure parsing settings, and view results.

## 🛠 Tech Stack

-   **Framework:** React 18
-   **Language:** TypeScript
-   **Build Tool:** Vite
-   **Styling:** Tailwind CSS
-   **State Management:** React Context API
-   **HTTP Client:** Native `fetch`

## 🚀 Getting Started

### Prerequisites

-   Node.js 20+
-   npm

### Installation

1.  Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

### Running the Dev Server

Start the Vite development server:

```bash
npm run dev
```

The app will be running at [http://localhost:5173](http://localhost:5173).

## 🧩 Key Components

-   **`FileUpload.tsx`**: Drag-and-drop zone for PDF files.
-   **`ParserSelector.tsx`**: Dropdown to select the parsing strategy (Docling, PDFMiner, etc.).
-   **`ResultGrid.tsx`**: Displays the parsed text results in a responsive grid.
-   **`AppContext.tsx`**: Global state management for file selection and parsing status.

## 📂 Structure

```text
src/
├── api/          # API client wrappers
├── components/   # Reusable UI components
├── context/      # React Context definitions
├── types/        # TypeScript interfaces
├── App.tsx       # Main layout
└── main.tsx      # Entry point
```
# Proposed Directory Structure

This structure separates the application into two distinct services: the API Backend and the Web Client.

```text
root/
├── .gitignore
├── README.md                  # Unified documentation for the whole project
├── docker-compose.yml         # (Optional) For running both services together
├── revise_plans/              # Planning documents
├── data/                      # Sample data (e.g., Quizlet Print.pdf)
│
├── backend/                   # PYTHON BACKEND
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── src/
│       ├── main.py            # FastAPI entry point (app initialization)
│       ├── config.py          # Environment variables and settings
│       ├── api/               # API Routes
│       │   ├── __init__.py
│       │   └── routes.py      # Endpoints (e.g., /parse)
│       └── parsers/           # EXISTING PARSER LOGIC (Moved from root src/)
│           ├── __init__.py
│           ├── base_parser.py
│           ├── docling_parser.py
│           ├── pdfminer_parser.py
│           ├── ...
│           └── utils.py
│
└── frontend/                  # TYPESCRIPT FRONTEND
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    ├── index.html
    ├── public/
    └── src/
        ├── main.tsx           # Entry point
        ├── App.tsx            # Main layout
        ├── api/               # API clients (axios/fetch wrappers)
        │   └── client.ts
        ├── components/        # Reusable UI components
        │   ├── FileUpload.tsx
        │   ├── ParserSelect.tsx
        │   └── ResultViewer.tsx
        └── types/             # TypeScript interfaces
            └── index.ts       # e.g., ParserResponse, ParseOptions
```

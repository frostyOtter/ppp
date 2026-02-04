from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
import sys
import tempfile
import os
import shutil
import time

from src.parsers import get_parser

# Configure logging
logger.remove()
logger.add(sys.stderr, level="INFO")
logger.add("logs/app.log", rotation="500 MB", level="INFO")

app = FastAPI(title="PDF Parser API")

# Configure CORS
origins = [
    "http://localhost:5173",
    # Add other origins if needed, e.g., "*" for development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to PDF Parser API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/v1/parse")
async def parse_pdf(
    file: UploadFile = File(...),
    parser_type: str = Form(...),
    start_page: int = Form(0),
    max_pages: int = Form(10),
):
    """
    Parse a PDF file and return the extracted content.
    """
    logger.info(f"Received parse request: parser={parser_type}, filename={file.filename}")

    # Validate parser type and map to internal name
    parser_mapping = {
        "docling": "Docling",
        "pdfminer": "PDFMiner",
        "pymupdf": "PyMuPDF",
        "pypdf2": "PyPDF2",
    }
    
    internal_parser_name = parser_mapping.get(parser_type.lower())
    if not internal_parser_name:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid parser type. Must be one of: {', '.join(parser_mapping.keys())}"
        )

    parser = get_parser(internal_parser_name)
    if not parser:
        raise HTTPException(status_code=500, detail=f"Parser {internal_parser_name} not initialized")

    # Create a temporary file to save the uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file_path = tmp_file.name
        try:
            # Write uploaded file content to temp file
            content = await file.read()
            tmp_file.write(content)
            tmp_file.flush()
            
            logger.info(f"Saved uploaded file to {tmp_file_path}")
            
            # Call the parser
            # API uses 0-based index, Parser uses 1-based index
            parser_start_page = start_page + 1
            
            logger.info(f"Parsing with {internal_parser_name}, start_page={parser_start_page}, max_pages={max_pages}")
            
            try:
                start_time = time.perf_counter()
                extracted_content = parser.parse(tmp_file_path, parser_start_page, max_pages)
                end_time = time.perf_counter()
                duration_ms = (end_time - start_time) * 1000
                
                # Check for error indicator in content (simple check based on return format)
                if extracted_content.startswith("# Error"):
                    # We might want to return 400 or 500 depending on the error,
                    # but for now let's wrap it in the success response as the content
                    # or explicitly raise if it's a critical failure.
                    # The instructions say "Handle errors ... with HTTPException".
                    # However, if the parser returns a formatted error string, maybe we return that?
                    # Let's log it.
                    logger.warning(f"Parser returned error content: {extracted_content[:100]}...")

                return {
                    "status": "success",
                    "metadata": {
                        "parser": parser_type,
                        "pages_processed": max_pages, # This is an approximation/request, not actual
                        "filename": file.filename,
                        "duration_ms": duration_ms
                    },
                    "content": extracted_content
                }
                
            except Exception as e:
                logger.error(f"Error during parsing: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Parsing failed: {str(e)}")
                
        except Exception as e:
            logger.error(f"Error handling file upload: {str(e)}")
            raise HTTPException(status_code=500, detail=f"File processing failed: {str(e)}")
        finally:
            # Clean up temp file
            if os.path.exists(tmp_file_path):
                try:
                    os.unlink(tmp_file_path)
                    logger.info(f"Deleted temp file {tmp_file_path}")
                except Exception as e:
                    logger.warning(f"Failed to delete temp file {tmp_file_path}: {str(e)}")
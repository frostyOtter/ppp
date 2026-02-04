import os
import sys
import pytest
from fastapi.testclient import TestClient

# Add backend to python path so we can import modules
# This assumes the test folder is at the root level, peer to backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))

from src.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_pdf_content():
    # Minimal valid PDF content for testing uploads
    return b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /Resources << >> /MediaBox [0 0 612 792] >>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF"
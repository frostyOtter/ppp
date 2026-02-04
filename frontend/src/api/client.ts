import type { ParseResponse } from '../types';

const BASE_URL = 'http://localhost:8000';

export async function uploadPdf(file: File, parser: string): Promise<ParseResponse> {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('parser_type', parser);

  const response = await fetch(`${BASE_URL}/api/v1/parse`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || `Failed to process PDF: ${response.statusText}`);
  }

  return response.json();
}

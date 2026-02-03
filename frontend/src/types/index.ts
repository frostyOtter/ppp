export type ParserType = 'docling' | 'pdfminer' | 'pymupdf' | 'pypdf2';

export interface ParseMetadata {
  parser: string;
  pages_processed: number;
  filename: string;
}

export interface ParseResponse {
  status: string;
  metadata: ParseMetadata;
  content: string;
}

export interface AppState {
  file: File | null;
  parser: ParserType;
  isProcessing: boolean;
  result: ParseResponse | null;
  error: string | null;
}

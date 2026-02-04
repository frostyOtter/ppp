export type ParserType = 'docling' | 'pdfminer' | 'pymupdf' | 'pypdf2';

export interface ParseMetadata {
  parser: string;
  pages_processed: number;
  filename: string;
  duration_ms: number;
}

export interface ParseResponse {
  status: string;
  metadata: ParseMetadata;
  content: string;
}

export type ProcessingStatus = 'idle' | 'pending' | 'success' | 'error';

export interface ParserResult {
  status: ProcessingStatus;
  data?: ParseResponse;
  error?: string;
  durationMs?: number;
}

export interface AppState {
  file: File | null;
  selectedParsers: ParserType[];
  results: Record<string, ParserResult>;
  isGlobalProcessing: boolean;
  globalError: string | null;
}
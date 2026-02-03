import React from 'react';
import { useApp } from '../context/AppContext';
import type { ParserType } from '../types';

export const ParserSettings: React.FC = () => {
  const { parser, setParser } = useApp();

  const parsers: { value: ParserType; label: string }[] = [
    { value: 'docling', label: 'Docling (Recommended)' },
    { value: 'pdfminer', label: 'PDFMiner' },
    { value: 'pymupdf', label: 'PyMuPDF' },
    { value: 'pypdf2', label: 'PyPDF2' },
  ];

  return (
    <div className="w-full max-w-md mx-auto p-4">
      <div className="bg-white rounded-lg shadow-sm p-4 border border-gray-100">
        <label htmlFor="parser-select" className="block text-sm font-medium text-gray-700 mb-2">
          Parser Engine
        </label>
        <select
          id="parser-select"
          value={parser}
          onChange={(e) => setParser(e.target.value as ParserType)}
          className="block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm p-2 border"
        >
          {parsers.map((p) => (
            <option key={p.value} value={p.value}>
              {p.label}
            </option>
          ))}
        </select>
        <p className="mt-2 text-xs text-gray-500">
          Select the parsing engine to extract text from your PDF.
        </p>
      </div>
    </div>
  );
};

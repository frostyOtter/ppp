import { useApp } from '../context/AppContext';
import type { ParserType } from '../types';

const PARSERS: { id: ParserType; label: string; description: string }[] = [
  { id: 'docling', label: 'Docling', description: 'Advanced layout analysis (Slower, Accurate)' },
  { id: 'pdfminer', label: 'PDFMiner', description: 'Text extraction (Fast, Basic)' },
  { id: 'pymupdf', label: 'PyMuPDF', description: 'High performance rendering' },
  { id: 'pypdf2', label: 'PyPDF2', description: 'Pure Python library' },
];

export const ParserSelector = () => {
  const { selectedParsers, toggleParser, isGlobalProcessing } = useApp();

  return (
    <div className="mb-8">
      <h3 className="text-lg font-medium text-gray-900 mb-4">Select Parsers to Run</h3>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {PARSERS.map((p) => {
          const isSelected = selectedParsers.includes(p.id);
          return (
            <div
              key={p.id}
              onClick={() => !isGlobalProcessing && toggleParser(p.id)}
              className={`
                relative flex items-start p-4 cursor-pointer rounded-lg border transition-all
                ${isSelected 
                  ? 'border-blue-500 ring-2 ring-blue-200 bg-blue-50' 
                  : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'}
                ${isGlobalProcessing ? 'opacity-50 cursor-not-allowed' : ''}
              `}
            >
              <div className="min-w-0 flex-1 text-sm">
                <label className="font-medium text-gray-900 cursor-pointer">
                  {p.label}
                </label>
                <p className="text-gray-500 mt-1">{p.description}</p>
              </div>
              <div className="ml-3 flex items-center h-5">
                <input
                  type="checkbox"
                  checked={isSelected}
                  onChange={() => {}} // Handled by div click
                  disabled={isGlobalProcessing}
                  className="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

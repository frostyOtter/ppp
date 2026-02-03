import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

interface ResultViewerProps {
  content: string;
}

const ResultViewer: React.FC<ResultViewerProps> = ({ content }) => {
  if (!content) {
    return (
      <div className="text-gray-500 italic text-center p-4 border border-dashed border-gray-300 rounded-lg">
        No content to display. Process a file to see results here.
      </div>
    );
  }

  return (
    <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200 overflow-auto max-h-[calc(100vh-200px)]">
      <div className="prose prose-slate max-w-none">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
      </div>
    </div>
  );
};

export default ResultViewer;

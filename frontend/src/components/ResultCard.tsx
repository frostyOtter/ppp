import type { ParserResult, ParserType } from '../types';

interface ResultCardProps {
  parserId: ParserType;
  result: ParserResult;
}

export const ResultCard = ({ parserId, result }: ResultCardProps) => {
  const { status, data, error, durationMs } = result;
  
  const parserLabel = parserId.charAt(0).toUpperCase() + parserId.slice(1);

  const handleDownload = (format: 'md' | 'json') => {
    if (!data) return;
    
    const originalName = data.metadata?.filename || 'document';
    const baseName = originalName.replace(/\.[^/.]+$/, "");
    const fileName = `${baseName}_${parserId}.${format}`;
    
    let content = '';
    let mimeType = '';

    if (format === 'md') {
      content = data.content;
      mimeType = 'text/markdown';
    } else {
      content = JSON.stringify(data, null, 2);
      mimeType = 'application/json';
    }

    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="bg-white rounded-lg shadow-md border border-gray-200 overflow-hidden flex flex-col h-96">
      <div className="bg-gray-50 px-4 py-3 border-b border-gray-200 flex justify-between items-center">
        <h3 className="font-medium text-gray-900">{parserLabel}</h3>
        <div className="flex items-center space-x-2">
            {status === 'success' && data && (
                <>
                    <button 
                        onClick={() => handleDownload('md')}
                        className="text-xs bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 px-2 py-1 rounded shadow-sm transition-colors"
                        title="Download Markdown"
                    >
                        MD
                    </button>
                    <button 
                        onClick={() => handleDownload('json')}
                        className="text-xs bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 px-2 py-1 rounded shadow-sm transition-colors"
                        title="Download JSON"
                    >
                        JSON
                    </button>
                </>
            )}
            {status === 'success' && durationMs && (
            <span className="text-xs text-gray-500 bg-gray-200 px-2 py-1 rounded-full">
                {(durationMs / 1000).toFixed(2)}s
            </span>
            )}
        </div>
      </div>
      
      <div className="p-4 flex-1 overflow-auto bg-gray-50/50">
        {status === 'pending' && (
           <div className="h-full flex flex-col items-center justify-center text-gray-500">
             <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500 mb-2"></div>
             <p>Processing...</p>
           </div>
        )}
        
        {status === 'error' && (
          <div className="h-full flex flex-col items-center justify-center text-red-500 p-4 text-center">
            <svg className="w-8 h-8 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <p className="text-sm">{error || 'An error occurred'}</p>
          </div>
        )}
        
        {status === 'success' && data && (
          <pre className="text-xs font-mono whitespace-pre-wrap text-gray-800 h-full overflow-y-auto">
            {data.content}
          </pre>
        )}

        {status === 'idle' && (
            <div className="h-full flex flex-col items-center justify-center text-gray-400">
                <p>Waiting to start...</p>
            </div>
        )}
      </div>
    </div>
  );
};

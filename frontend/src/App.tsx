import { FileUpload, ParserSettings, ResultViewer, LoadingSpinner, ErrorMessage } from './components';
import { useApp } from './context/AppContext';
import { uploadPdf } from './api/client';

function App() {
  const { 
    file, 
    parser, 
    isProcessing, 
    result, 
    error, 
    setError, 
    setIsProcessing, 
    setResult 
  } = useApp();

  const handleProcess = async () => {
    if (!file) return;

    setIsProcessing(true);
    setError(null);
    setResult(null);

    try {
      const data = await uploadPdf(file, parser);
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unknown error occurred');
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col md:flex-row">
      {/* Sidebar */}
      <aside className="w-full md:w-64 bg-white border-r border-gray-200 p-6 flex-shrink-0">
        <h1 className="text-xl font-bold text-gray-800 mb-6">PDF Parser</h1>
        <div className="space-y-6">
          <div>
            <h2 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-4">
              Configuration
            </h2>
            <ParserSettings />
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-8">
        <div className="max-w-4xl mx-auto">
          <div className="mb-8">
            <h2 className="text-2xl font-bold text-gray-900 mb-2">Upload Document</h2>
            <p className="text-gray-600">
              Select a PDF file to process using the configured parser.
            </p>
          </div>
          
          <div className="space-y-6">
            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
              <FileUpload />
              <div className="mt-6 flex justify-end">
                <button
                  onClick={handleProcess}
                  disabled={!file || isProcessing}
                  className={`
                    px-6 py-2 rounded-lg font-semibold text-white transition-colors
                    ${!file || isProcessing
                      ? 'bg-gray-400 cursor-not-allowed'
                      : 'bg-blue-600 hover:bg-blue-700 active:bg-blue-800'}
                  `}
                >
                  {isProcessing ? 'Processing...' : 'Process PDF'}
                </button>
              </div>
            </div>

            {error && (
              <ErrorMessage 
                message={error} 
                onDismiss={() => setError(null)} 
              />
            )}

            {isProcessing ? (
              <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 min-h-[200px] flex items-center justify-center">
                <LoadingSpinner />
              </div>
            ) : (
              result && (
                <div>
                  <h3 className="text-lg font-bold text-gray-900 mb-4">Parsed Result</h3>
                  <ResultViewer content={result.content} />
                </div>
              )
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
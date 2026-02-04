import { FileUpload, ErrorMessage, FileReview, ParserSelector, ResultGrid } from './components';
import { useApp } from './context/AppContext';
import * as api from './api/client';

function App() {
  const { 
    file, 
    globalError, 
    selectedParsers, 
    isGlobalProcessing, 
    setIsGlobalProcessing, 
    setGlobalError, 
    updateResult 
  } = useApp();

  const handleProcess = async () => {
    if (!file || selectedParsers.length === 0) return;
    
    setIsGlobalProcessing(true);
    setGlobalError(null);
    
    // Initialize results for selected parsers to pending
    selectedParsers.forEach(p => {
        updateResult(p, { status: 'pending' });
    });

    // Create a promise for each parser
    const promises = selectedParsers.map(async (parserId) => {
        const startTime = Date.now();
        try {
            const data = await api.uploadPdf(file, parserId);
            updateResult(parserId, { 
                status: 'success', 
                data, 
                durationMs: data.metadata.duration_ms
            });
        } catch (err: any) {
            const durationMs = Date.now() - startTime;
             updateResult(parserId, { 
                status: 'error', 
                error: err.message || 'Unknown error',
                durationMs
            });
        }
    });

    // Wait for all to finish
    await Promise.all(promises);
    setIsGlobalProcessing(false);
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-10">
          <h1 className="text-4xl font-extrabold text-gray-900 tracking-tight">PDF Parser Arena</h1>
          <p className="mt-3 text-lg text-gray-500">Compare results from different PDF parsing engines side-by-side</p>
        </div>

        <ErrorMessage message={globalError} />

        <div className="transition-all duration-500 ease-in-out">
          {!file ? (
             <div className="max-w-xl mx-auto">
               <FileUpload />
             </div>
          ) : (
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-start">
                <div className="lg:col-span-1 lg:sticky lg:top-8 lg:h-[calc(100vh-4rem)] overflow-hidden flex flex-col">
                    <FileReview />
                </div>
                
                <div className="lg:col-span-2 flex flex-col gap-6 w-full min-w-0">
                    <ParserSelector />
                    
                    <div className="flex justify-center">
                        <button
                            onClick={handleProcess}
                            disabled={selectedParsers.length === 0 || isGlobalProcessing}
                            className={`
                                px-8 py-3 rounded-lg font-semibold text-lg transition-all transform focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500
                                ${selectedParsers.length > 0 && !isGlobalProcessing
                                    ? 'bg-blue-600 text-white shadow-lg hover:bg-blue-700 hover:-translate-y-0.5' 
                                    : 'bg-gray-200 text-gray-400 cursor-not-allowed shadow-none'}
                            `}
                        >
                            {isGlobalProcessing ? (
                                <span className="flex items-center">
                                    <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                    </svg>
                                    Processing...
                                </span>
                            ) : 'Start Processing'}
                        </button>
                    </div>

                    <ResultGrid />
                </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;

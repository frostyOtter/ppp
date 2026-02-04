import { useApp } from '../context/AppContext';

export const FileReview = () => {
  const { file, removeFile } = useApp();

  if (!file) return null;

  const formatSize = (bytes: number) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6 mb-6 flex items-center justify-between border border-gray-100">
      <div className="flex items-center space-x-4">
        <div className="h-12 w-12 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600">
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
        </div>
        <div>
          <h3 className="text-lg font-medium text-gray-900">{file.name}</h3>
          <p className="text-sm text-gray-500">{formatSize(file.size)}</p>
        </div>
      </div>
      <button
        onClick={removeFile}
        className="px-4 py-2 text-sm font-medium text-red-600 hover:text-red-700 hover:bg-red-50 rounded-md transition-colors focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
      >
        Change File
      </button>
    </div>
  );
};

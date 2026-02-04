import { useApp } from '../context/AppContext';
import { ResultCard } from './ResultCard';

export const ResultGrid = () => {
  const { selectedParsers, results } = useApp();
  
  if (selectedParsers.length === 0) return null;

  return (
    <div>
      <h2 className="text-xl font-bold text-gray-900 mb-4">Results Comparison</h2>
      <div className="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
        {selectedParsers.map((parserId) => {
            const result = results[parserId] || { status: 'idle' };
            return (
                <ResultCard key={parserId} parserId={parserId} result={result} />
            );
        })}
      </div>
    </div>
  );
};

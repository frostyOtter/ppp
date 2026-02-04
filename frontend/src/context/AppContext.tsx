/**
 * AppContext.tsx
 * 
 * Provides global state management for the application using React Context.
 * Manages the current file, parser selection (multi-select), processing state, and results map.
 */
import { createContext, useContext, useState, type ReactNode } from 'react';
import type { AppState, ParserType, ParserResult } from '../types';

interface AppContextProps extends AppState {
  setFile: (file: File | null) => void;
  toggleParser: (parser: ParserType) => void;
  setIsGlobalProcessing: (isProcessing: boolean) => void;
  updateResult: (parser: ParserType, result: ParserResult) => void;
  resetResults: () => void;
  setGlobalError: (error: string | null) => void;
  resetState: () => void;
  removeFile: () => void;
}

const AppContext = createContext<AppContextProps | undefined>(undefined);

export const AppProvider = ({ children }: { children: ReactNode }) => {
  const [file, setFileState] = useState<File | null>(null);
  const [selectedParsers, setSelectedParsers] = useState<ParserType[]>([]);
  const [results, setResults] = useState<Record<string, ParserResult>>({});
  const [isGlobalProcessing, setIsGlobalProcessing] = useState(false);
  const [globalError, setGlobalError] = useState<string | null>(null);

  const setFile = (newFile: File | null) => {
    setFileState(newFile);
    // When file changes, reset results and error
    setResults({});
    setGlobalError(null);
  };

  const toggleParser = (parser: ParserType) => {
    setSelectedParsers(prev =>
      prev.includes(parser)
        ? prev.filter(p => p !== parser)
        : [...prev, parser]
    );
  };

  const updateResult = (parser: ParserType, result: ParserResult) => {
    setResults(prev => ({
      ...prev,
      [parser]: result
    }));
  };

  const resetResults = () => {
    setResults({});
    setIsGlobalProcessing(false);
    setGlobalError(null);
  };

  const removeFile = () => {
    setFileState(null);
    setResults({});
    setIsGlobalProcessing(false);
    setGlobalError(null);
    // Note: We deliberately keep selectedParsers so user doesn't have to re-select
  };

  const resetState = () => {
    setFileState(null);
    setSelectedParsers([]);
    setResults({});
    setIsGlobalProcessing(false);
    setGlobalError(null);
  };

  const value = {
    file,
    selectedParsers,
    results,
    isGlobalProcessing,
    globalError,
    setFile,
    toggleParser,
    setIsGlobalProcessing,
    updateResult,
    resetResults,
    setGlobalError,
    resetState,
    removeFile
  };

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
};

export const useApp = () => {
  const context = useContext(AppContext);
  if (context === undefined) {
    throw new Error('useApp must be used within an AppProvider');
  }
  return context;
};
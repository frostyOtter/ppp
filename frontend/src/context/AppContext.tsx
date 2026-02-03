/**
 * AppContext.tsx
 * 
 * Provides global state management for the application using React Context.
 * Manages the current file, parser selection, processing state, results, and errors.
 * 
 * Usage:
 * Wrap your application with <AppProvider>.
 * Use the useApp() hook to access state and actions in components.
 */
import { createContext, useContext, useState, type ReactNode } from 'react';
import type { AppState, ParserType, ParseResponse } from '../types';

interface AppContextProps extends AppState {
  setFile: (file: File | null) => void;
  setParser: (parser: ParserType) => void;
  setIsProcessing: (isProcessing: boolean) => void;
  setResult: (result: ParseResponse | null) => void;
  setError: (error: string | null) => void;
  resetState: () => void;
}

const AppContext = createContext<AppContextProps | undefined>(undefined);

export const AppProvider = ({ children }: { children: ReactNode }) => {
  const [file, setFile] = useState<File | null>(null);
  const [parser, setParser] = useState<ParserType>('docling');
  const [isProcessing, setIsProcessing] = useState(false);
  const [result, setResult] = useState<ParseResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const resetState = () => {
    setFile(null);
    setParser('docling');
    setIsProcessing(false);
    setResult(null);
    setError(null);
  };

  const value = {
    file,
    parser,
    isProcessing,
    result,
    error,
    setFile,
    setParser,
    setIsProcessing,
    setResult,
    setError,
    resetState,
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

import React, { useState, useEffect, useRef } from 'react';
import { Play, Pause, RotateCcw, Coffee, Brain } from 'lucide-react';

const WORK_TIME = 25 * 60;
const BREAK_TIME = 5 * 60;

const Pomodoro = () => {
  const [timeLeft, setTimeLeft] = useState(WORK_TIME);
  const [isActive, setIsActive] = useState(false);
  const [mode, setMode] = useState('focus'); // 'focus' or 'break'
  
  const timerRef = useRef(null);

  useEffect(() => {
    if (isActive && timeLeft > 0) {
      timerRef.current = setInterval(() => {
        setTimeLeft((prev) => prev - 1);
      }, 1000);
    } else if (timeLeft === 0) {
      clearInterval(timerRef.current);
      // Auto-switch mode
      if (mode === 'focus') {
        setMode('break');
        setTimeLeft(BREAK_TIME);
      } else {
        setMode('focus');
        setTimeLeft(WORK_TIME);
      }
      setIsActive(false); // Stop when switching
    }

    return () => clearInterval(timerRef.current);
  }, [isActive, timeLeft, mode]);

  const toggleTimer = () => setIsActive(!isActive);

  const resetTimer = () => {
    setIsActive(false);
    setTimeLeft(mode === 'focus' ? WORK_TIME : BREAK_TIME);
  };

  const switchMode = (newMode) => {
    if (mode === newMode) return;
    setIsActive(false);
    setMode(newMode);
    setTimeLeft(newMode === 'focus' ? WORK_TIME : BREAK_TIME);
  };

  const formatTime = (seconds) => {
    const m = Math.floor(seconds / 60).toString().padStart(2, '0');
    const s = (seconds % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  const progress = mode === 'focus' 
    ? ((WORK_TIME - timeLeft) / WORK_TIME) * 100 
    : ((BREAK_TIME - timeLeft) / BREAK_TIME) * 100;

  return (
    <div className="flex flex-col items-center bg-slate-800 rounded-[3rem] p-8 shadow-2xl border-4 border-slate-700/50 transition-colors duration-500 relative overflow-hidden w-full">
      
      {/* Background decoration */}
      <div className={`absolute top-0 left-0 w-full h-3 ${mode === 'focus' ? 'bg-tomato-500' : 'bg-break-500'} transition-colors duration-500`} />

      {/* Header */}
      <div className="flex justify-center space-x-4 mb-8 w-full pt-2">
        <button
          onClick={() => switchMode('focus')}
          className={`flex items-center px-5 py-2.5 rounded-2xl font-bold transition-all duration-300 ${
            mode === 'focus' 
              ? 'bg-tomato-500 text-white shadow-lg shadow-tomato-500/30 scale-105' 
              : 'bg-slate-700 text-slate-400 hover:bg-slate-600'
          }`}
        >
          <Brain size={20} className="mr-2" />
          Focus
        </button>
        <button
          onClick={() => switchMode('break')}
          className={`flex items-center px-5 py-2.5 rounded-2xl font-bold transition-all duration-300 ${
            mode === 'break' 
              ? 'bg-break-500 text-white shadow-lg shadow-break-500/30 scale-105' 
              : 'bg-slate-700 text-slate-400 hover:bg-slate-600'
          }`}
        >
          <Coffee size={20} className="mr-2" />
          Break
        </button>
      </div>

      {/* Timer Display */}
      <div className="relative flex justify-center items-center mb-10 group">
        <div className={`absolute w-64 h-64 rounded-full border-[8px] ${mode === 'focus' ? 'border-tomato-500/20' : 'border-break-500/20'} animate-pulse`} />
        
        {/* SVG Circle Progress */}
        <svg className="w-72 h-72 transform -rotate-90 drop-shadow-sm">
          <circle
            cx="144"
            cy="144"
            r="134"
            stroke="currentColor"
            strokeWidth="8"
            fill="transparent"
            className="text-slate-700"
          />
          <circle
            cx="144"
            cy="144"
            r="134"
            stroke="currentColor"
            strokeWidth="12"
            fill="transparent"
            strokeDasharray={2 * Math.PI * 134}
            strokeDashoffset={2 * Math.PI * 134 * (1 - progress / 100)}
            className={`transition-all duration-1000 ease-in-out ${mode === 'focus' ? 'text-tomato-500' : 'text-break-500'}`}
            strokeLinecap="round"
          />
        </svg>

        <div className="absolute flex flex-col items-center">
          <span className="text-7xl font-extrabold tracking-tighter text-white drop-shadow-md transition-all duration-300 group-hover:scale-105 select-none">
            {formatTime(timeLeft)}
          </span>
          <span className={`text-sm mt-2 font-bold uppercase tracking-widest ${mode === 'focus' ? 'text-tomato-400' : 'text-break-400'} select-none`}>
            {mode === 'focus' ? 'Time to focus!' : 'Take a break!'}
          </span>
        </div>
      </div>

      {/* Controls */}
      <div className="flex items-center space-x-6 mb-2">
        <button
          onClick={toggleTimer}
          className={`w-16 h-16 flex justify-center items-center rounded-full text-white transition-all duration-300 hover:scale-110 shadow-xl ${
            mode === 'focus' ? 'bg-tomato-500 hover:bg-tomato-400 shadow-tomato-500/40' : 'bg-break-500 hover:bg-break-400 shadow-break-500/40'
          }`}
        >
          {isActive ? <Pause size={32} fill="currentColor" /> : <Play size={32} fill="currentColor" className="ml-1" />}
        </button>
        <button
          onClick={resetTimer}
          className="w-12 h-12 flex justify-center items-center rounded-full bg-slate-700 text-slate-300 hover:bg-slate-600 hover:text-white transition-all duration-300 hover:rotate-180"
          title="Reset Timer"
        >
          <RotateCcw size={24} />
        </button>
      </div>

    </div>
  );
};

export default Pomodoro;

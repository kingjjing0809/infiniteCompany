import React from 'react'
import Pomodoro from './components/Pomodoro'

function App() {
  return (
    <div className="w-full max-w-md mx-auto p-4 flex items-center justify-center min-h-screen">
      <div className="w-full">
        <Pomodoro />
      </div>
    </div>
  )
}

export default App

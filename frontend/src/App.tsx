import { useState } from 'react';
import { predictFood } from './api/api';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [prediction, setPrediction] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
      setSelectedFile(event.target.files[0]);
    }
  };

  const handlePredict = async () => {
    if (!selectedFile) return;

    setLoading(true);
    setError('');
    setPrediction('');

    try {
      const result = await predictFood(selectedFile);
      if (result && typeof result.label === 'string') {
        setPrediction(result.label);
      } else {
        setError('Invalid response format.');
      }
    } catch (err) {
      setError('Failed to get prediction.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Food Image Prediction</h1>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button onClick={handlePredict} disabled={loading}>
        {loading ? 'Predicting...' : 'Predict'}
      </button>
      {prediction && <p>Prediction: {prediction}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;

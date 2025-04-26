export interface PredictionResponse {
  label: string;
}

export async function predictFood(file: File): Promise<PredictionResponse> {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch('http://127.0.0.1:8000/predict', {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Failed to get prediction');
  }

  const data = await response.json();
  return data;
}
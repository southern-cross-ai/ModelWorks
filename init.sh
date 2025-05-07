#!/bin/bash

MODEL="deepseek-r1:1.5b"

echo "🔧 Starting Ollama service..."
docker-compose up -d

echo "⏳ Waiting for Ollama service to become ready..."
until curl -s http://localhost:11434 > /dev/null; do
  sleep 1
  echo "  ...waiting for Ollama to respond on port 11434"
done

echo "✅ Ollama is ready."

if docker-compose exec ollama ollama list | grep -q "$MODEL"; then
  echo "✅ Model $MODEL already exists. Skipping pull."
else
  echo "⬇️ Pulling model $MODEL..."
  docker-compose exec ollama ollama pull $MODEL
fi

echo "🎉 Setup complete. Model is ready for use!"

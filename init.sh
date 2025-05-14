#!/bin/bash

MODEL="deepseek-r1:1.5b"
EMBED_MODEL="nomic-embed-text"

echo "🔧 Starting Ollama service..."
docker-compose up --build -d

echo "⏳ Waiting for Ollama service to become ready..."
until curl -s http://localhost:11434 > /dev/null; do
  sleep 1docker exec modelworks-ollama-1 ollama list
  echo "  ...waiting for Ollama to respond on port 11434"
done

echo "✅ Ollama is ready."

if docker-compose exec ollama ollama list | grep -q "$MODEL"; then
  echo "✅ Model $MODEL already exists. Skipping pull."
else
  echo "⬇️ Pulling model $MODEL..."
  docker-compose exec ollama ollama pull $MODEL
fi

echo "🔍 Checking if embedding model $EMBED_MODEL exists..."
if docker-compose exec ollama ollama list | grep -q "$EMBED_MODEL"; then
  echo "✅ Embedding model $EMBED_MODEL already exists."
else
  echo "⬇️ Pulling embedding model $EMBED_MODEL..."
  docker-compose exec ollama ollama pull $EMBED_MODEL
fi

echo "🎉 Setup complete. Model is ready for use!"

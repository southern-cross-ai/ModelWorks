#!/bin/bash

MODEL="deepseek-r1:1.5b"
EMBED_MODEL="nomic-embed-text"

echo "🔍 Checking if Docker is running..."
if ! docker info > /dev/null 2>&1; then
  echo "🚫 Docker is not running. Attempting to start Docker..."

  if [[ "$OSTYPE" == "darwin"* ]]; then
    open --background -a Docker
  elif grep -qi microsoft /proc/version 2>/dev/null || [[ "$OSTYPE" == "msys" ]]; then
    powershell.exe -Command "Start-Process 'C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe'" > /dev/null 2>&1
  else
    echo "❌ Unsupported OS for auto-starting Docker. Please start Docker manually."
    exit 1
  fi

  echo "⏳ Waiting for Docker to start..."
  maxWait=60
  elapsed=0
  while ! docker info > /dev/null 2>&1; do
    if [ $elapsed -ge $maxWait ]; then
      echo "❌ Docker did not start within $maxWait seconds. Please check Docker Desktop manually."
      exit 1
    fi
    sleep 5
    elapsed=$((elapsed + 2))
    echo "  ...waiting for Docker engine ($elapsed sec)"
  done
  echo "✅ Docker is running."
else
  echo "✅ Docker is already running."
fi


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
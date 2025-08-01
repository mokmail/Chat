systemctl kill ollama
export OLLAMA_HOST=0.0.0.0:11434 
ollama serve > ollama.json 2>&1 &
sleep 5

docker compose down 
docker compose up > ollama.json 2>&1 &

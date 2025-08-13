systemctl kill ollama
export OLLAMA_HOST=192.168.1.60:11434
ollama serve > ollama.json 2>&1 &
sleep 5

docker compose down 
docker compose up > ollama.json 2>&1 &

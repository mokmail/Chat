systemctl kill ollama
export OLLAMA_HOST=0.0.0.0:11434 
ollama serve > ollama.json 2>&1 &
sleep 5

sudo docker compose down 
sudo docker compose up > ollama.json 2>&1 &

✅ Step-by-step Instructions
Give execute permission to the script (only needed once):
`chmod +x init.sh`
Run the script to start the container and download the model:
`./init.sh`
🔁 Future Use (After Initial Setup)
Only run:
`./init.sh`

📦 Where the Model Is Stored
The model is saved in a Docker volume named ollama-data, which is mounted to the container's /root/.ollama directory.

As long as the volume is not deleted, the model will be preserved across container restarts and rebuilds.
❌ 1. Avoid `docker-compose down -v`
This deletes both the container and the volume
❌ 2. Avoid `docker volume rm ollama-data`
This deletes the volume manually
❌ 3. Avoid using `--volumes` with `docker rm` or `docker container prune`
This will remove all unused containers and their associated anonymous volumes
✅ Safe Commands You CAN Use
`docker-compose down` Stops and removes containers but keeps volumes



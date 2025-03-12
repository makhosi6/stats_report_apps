# Stats

1. Confirm/Inspect
- `docker-compose --env-file ./stats_web_ui/.env config`

2. Deploy
- `docker-compose --env-file ./stats_web_ui/.env up -d --force-recreate --build --remove-orphans`


`docker network create -d bridge stats_bridge`
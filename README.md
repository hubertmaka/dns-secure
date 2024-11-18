# dns-secure

The goal of this project is to show DNS communication vulnerabilities and secure them.

## How to run:

1. Clone the repository:
   ```bash
   git clone https://github.com/hubertmaka/dns-secure.git
   ```
2. Go into cloned repo directory:
   ```bash
   cd ./dns-secure
   ```
3. Check containers:
   ```bash
   docker ps
   ```
4. Run docker-compose to run lab:
   ```bash
   docker compose up -d --build
   ```
5. To run any container bash:
   ```bash
   docker exec -it [container_name] bash
   ```

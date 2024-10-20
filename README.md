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
3. Build image (make sure you have Docker deamon running):
   ```bash
   docker build -t bind9_image:0.1 .
   ```
4. Check if image was built:
   ```bash
   docker images
   ```
5. Run docker-compose to run bind server:
   ```bash
   docker compose up -d
   ```
6. Chceck server availability:
   ```bash
   host pvedemo1.homelab.lan 127.0.0.1
   host 192.168.102.31 127.0.0.1
   ```
7. To stop BIND server:
   ```bash
   docker container stop bind9
   ```

FROM debian:latest

RUN apt update
RUN apt install bind9 -y

EXPOSE 53/tcp
EXPOSE 53/udp

USER bind:bind

CMD ["/usr/sbin/named", "-f"]




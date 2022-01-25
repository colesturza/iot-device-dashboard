FROM eclipse-mosquitto:2.0.14

RUN ["apk", "update", "&&", "apk", "add", "bash"]

COPY entrypoint.sh /
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]
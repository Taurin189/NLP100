FROM redis
ADD artist.txt .
RUN apt update && apt install -y procps
ADD init_script.sh .
CMD ["sh", "init_script.sh"]
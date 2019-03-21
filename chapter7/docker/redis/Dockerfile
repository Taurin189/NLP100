FROM redis
RUN apt update && apt install -y procps
ADD artist.txt .
ADD init_script.sh .
CMD ["sh", "init_script.sh"]
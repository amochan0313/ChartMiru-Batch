FROM ubuntu:18.04

# env設定
ENV LANG="C.UTF-8"
ENV FLASK_APP="cli"

RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install python-dotenv

# コンテナ内で必要なスクリプトを実行
COPY docker-entrypoint.sh /usr/local/bin
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["tail", "-f", "/dev/null"]


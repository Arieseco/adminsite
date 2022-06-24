FROM python:3.11.0b3-buster

# パッケージのインストール
RUN apt-get update \
&& apt-get install -y tzdata \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1
ENV TZ=Asia/Tokyo
ENV USER fwpc0811

# 一般権限のユーザー追加
RUN useradd -m ${USER} --uid 1000
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:password | chpasswd"

# ユーザーの切り替え
USER ${USER}

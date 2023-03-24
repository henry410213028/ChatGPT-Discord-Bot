FROM python:3.9-alpine

WORKDIR /DiscordBot

COPY ./requirements.txt /DiscordBot/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./ /DiscordBot

CMD ["python3", "main.py"]
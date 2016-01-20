import discord

def responses(client, message):
    data_file = open("data.txt")
    for string in data_file.read().split("\n"):
        tuple_string = string.split(":")
        if len(tuple_string) == 2:
            client.send_message(message.channel, tuple_string[0] + " - " + tuple_string[1])

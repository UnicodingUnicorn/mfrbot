import discord
import sched, time

email = "mfr.discordbot@gmail.com"
password = "silverleaf"

client = discord.Client()
client.login(email, password)

def read_data():
    global data
    data_file = open("data.txt")
    data = {}
    for string in data_file.read().split("\n"):
        tuple_string = string.split(":")
        if len(tuple_string) == 2:
            data[tuple_string[0]] = tuple_string[1]
@client.event
def on_message(message):
    if message.author.id != client.user.id:
	if message.content == "!responses":
		client.send_message(message.channel, "Listing all my responses:")
		for key in data:
			client.send_message(message.channel, key + " - " + data[key])
	else:
	        for key in data:
        	    if message.content.startswith(key):
                	string = data[key]
	                send_string = ""
        	        for word in string.split():
                	    if word == "@user":
                        	send_string += message.author.mention() + " "
	                    else:
        	                send_string += word + " "
                	client.send_message(message.channel, send_string)
	                break
#@client.event
#def on_member_join(member):
#    send_string = "Welcome " + member.mention() + ", welcome to " + member.server.name + "!"
#    for channel in member.server.channels:
#        client.send_message(channel, send_string)
@client.event
def on_message_delete(message):
        send_string = "Psst! " + message.author.name + "  said \"" + message.content + "\" at " + str(message.timestamp) + " but regretted it."
        client.send_message(message.channel, send_string)
@client.event
def on_member_remove(member):
	client.send_message(member, client.create_invite(member.server).url)
@client.event
def on_ready():
    print "Online"

def update_minute(sc):
    read_data()
    print "Updated"
    sc.enter(60, 1, update_minute, (sc,))

read_data()

client.run()

s = sched.scheduler(time.time, time.sleep)
s.enter(60, 1, update_minute, (s,))
s.run()
print "ran"

import paho.mqtt.client as mqtt
import sys
import re
import time


sId = sys.argv[1]
name = sys.argv[2]
topic = sys.argv[3]
host_name = sys.argv[4]
port = int(sys.argv[5])
total = 0
id = []
client = mqtt.Client(name)
client.connect(host_name,port = port)
client.subscribe(topic, qos=0)

def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))
    read = str(re.findall("\s\d*\d\s",message.payload.decode("utf-8"))[0].strip())
    print(read)
    global increment
    increment = int(read)
client.on_message=on_message

for c in sId:
    id.append(c)
print (str(id))
for i in id:
    total += int(i)
increment = 0
client.loop_start()
while(increment == 0 ):
    time.sleep(0.1)
client.loop_stop()

print(increment)
total += increment

result = bin(total)[2:]


print('engmt280\Team7', name + ' ' + result)
#client.publish('engmt280\AssessmentI6', name + ' ' + result)



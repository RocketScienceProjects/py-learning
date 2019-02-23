from kafka import BrokerConnection
from kafka.protocol.admin import *
import socket
# import kafka

bc = BrokerConnection('10.173.210.68', 9092, socket.AF_INET)
bc.connect_blocking()

list_groups_request = ListGroupsRequest_v1()

future = bc.send(list_groups_request)
while not future.is_done:
    for resp, f in bc.recv():
        f.success(resp)

for group in future.value.groups:
    print(group)
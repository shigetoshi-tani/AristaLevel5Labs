import pyeapi
connect = pyeapi.connect_to("leaf1-DC1")
connect.api("ipinterfaces").create('Ethernet4')
result = connect.api("ipinterfaces").set_address('Ethernet4','4.4.4.4/24')

if result == True:
    print("Completed!")
if result == False:
    print("Error!")

from jsonrpclib import Server
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

user = "arista"
password = "arista32y8"

cmds = ["enable","configure","router ospf 100", "shutdown"]
#cmds = ["show ip ospf summary"]

switches = ["leaf1-DC1", "leaf2-DC1", "leaf3-DC1","leaf4-DC1",
            "leaf1-DC2", "leaf2-DC2", "leaf3-DC2","leaf4-DC2",
            "spine1-DC1", "spine2-DC1", "spine3-DC1",
            "spine1-DC2", "spine2-DC2", "spine3-DC2",
            "borderleaf1-DC1", "borderleaf2-DC1",
            "borderleaf1-DC2", "borderleaf2-DC2" ]

for switch in switches:
    sw = Server("https://%s:%s@%s/command-api" % (user,password,switch) )
    r = sw.runCmds(1,cmds)
 #   print(r[0]["vrfs"]["default"]["instList"]["100"]["inst"]["routerId"])
    print(switch)



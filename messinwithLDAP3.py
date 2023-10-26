# seeing about getting Domain controller name #
from ldap3 import Server, Connection, ALL


server = Server('ssi-mi.local', get_info=ALL)
conn = Connection(server)
conn.bind()
serv = server.info

print(conn)
print(serv)
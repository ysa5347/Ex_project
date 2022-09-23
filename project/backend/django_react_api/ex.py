import os
from dotenv import load_dotenv
from sshtunnel import SSHTunnelForwarder
import pymysql
import socket

with SSHTunnelForwarder(
        'bastion',
        remote_bind_address=('ex-finder-db.cqpnhc7dgpt9.ap-northeast-2.rds.amazonaws.com', 3306),
    ) as ssh_tunnel:
    print(f'remote bind host : {ssh_tunnel.local_bind_port}')
    with pymysql.connect(
        host='localhost',
        user='admin',
        password='roqkfqkekr__a',
        db='Ex_finder',
        port=ssh_tunnel.local_bind_port
    )   as conn:
        print('connected!')
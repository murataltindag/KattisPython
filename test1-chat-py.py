#! python3

"""
Automated testing
Assignment: Chat
Test 1 for Python code

Tests included:
Does the server start? If not, perhaps the name is wrong?
Does the client start? If not, perhaps the name is wrong?
Are messages transferred immediately?
Does the client end when stdin ends?
Does the client write the correct output?
"""

import os, sys, time, subprocess, psutil
from within_file import WithinFile
withinFile= WithinFile()

shell_command= 'rm client1-recvd.txt'
os.system( shell_command )
shell_command= 'rm client2-recvd.txt'
os.system( shell_command )

server_program_name = 'ChatServer.py'
client_program_name = 'ChatClient.py'

#check whether the program files are named correctly
try:
	file_stat= os.stat( server_program_name )
except FileNotFoundError:
	print( server_program_name + ' does not exist; the name of your server program must match exactly' )
	sys.exit()
if file_stat.st_size == 0:
	print( 'Your server program, ' + server_program_name + ', is an empty file' )
	sys.exit()

try:
	file_stat= os.stat( client_program_name )
except FileNotFoundError:
	print( client_program_name + ' does not exist; the name of your client program must match exactly' )
	sys.exit()
if file_stat.st_size == 0:
	print( 'Your client program, ' + client_program_name + ', is an empty file' )
	sys.exit()

# find a vacant port number
for port in range(1025, 65535):
        if not (port in [i.laddr.port for i in psutil.net_connections()]):
                break
print('using port number', port)
args= ['py','-u',server_program_name,str(port)]
server_errors= open( 'server-errors.txt', 'w' )
server= subprocess.Popen( args, stderr= server_errors )

time.sleep( 2 ) # CHANGE: changed from 1 to 2

# create blank input for the pipe to client1
#args= ['py','-u','input-writer.py','0', '4', 'client1-name-only.txt'] # CHANGE: changed pace from 2 to 4
args= ['py','-u','input-writer.py','0', '5', 'client1-name-only.txt'] # 1-9-23 changed pace 4 to 5
client1_input_writer= subprocess.Popen( args, stdout=subprocess.PIPE)

# start the client program as client1
args= ['py','-u', client_program_name, str(port)]
client1_output_text= open( 'client1-recvd.txt', 'w' )
client1= subprocess.Popen( args, stdin= client1_input_writer.stdout, stdout=client1_output_text)

# create the input for the pipe to client2
args= ['py','-u','input-writer.py','1', '1', 'client2-msgs-test.txt'] # CHANGE: changed initial delay from 0 to 1
client2_input_writer= subprocess.Popen( args, stdout=subprocess.PIPE)

# start the client program as client2
args= ['py','-u', client_program_name, str(port)]
client2_output_text= open( 'client2-recvd.txt', 'w' )
client2= subprocess.Popen( args, stdin= client2_input_writer.stdout, stdout=client2_output_text)

# check whether messages were transferred immediately from client2 to client1
#time.sleep( 4 ) # CHANGE: changed from 3 to 4
time.sleep( 3.5 ) # 1-9-23 changed from 4 to 3.5
found= withinFile.searchText( 'client1-recvd-multiple-test.txt', 'client1-recvd.txt' )
if not found:
	print( 'messages must be transferred immediately; your program must be revised' )
	client1.kill()
	client2.kill()
	server.kill()
	try:
		server_errors.close()
	except Exception:
		pass
	sys.exit()

# wait until the input pipe for client2 closes; then, check whether the process terminated
try:
#	client2.wait( 3 ) # CHANGE: changed from 0 to 3
	client2.wait( 2 ) # 1-9-23 changed from 3 to 2
	if client2.returncode != 0:
		print( client_program_name + ' (client2) returned: ' + str(client2.returncode) + '; your program must be revised' )
		client1.kill()
		server.kill()
		try:
			server_errors.close()
		except Exception:
			pass
		sys.exit()
except subprocess.TimeoutExpired:
	print( client_program_name + ' (client2) has not exited within the expected timeframe; your program must be revised' )
	client1.kill()
	client2.kill()
	server.kill()
	try:
		server_errors.close()
	except Exception:
		pass
	sys.exit()

# wait until the input pipe for client1 closes; then, check whether the process terminated
try:
	client1.wait( 5 ) # CHANGE: changed from 2 to 5
	if client1.returncode != 0:
		print( client_program_name + ' (client1) returned: ' + str(client1.returncode) + '; your program must be revised' )
		server.kill()
		try:
			server_errors.close()
		except Exception:
			pass
		sys.exit()
except subprocess.TimeoutExpired:
	print( client_program_name + ' (client1) has not exited within the expected timeframe; your program must be revised' )
	client1.kill()
	server.kill()
	try:
		server_errors.close()
	except Exception:
		pass
	sys.exit()

server.kill()
try:
	server_errors.close()
except Exception:
	pass

print( 'test1 terminated properly' )

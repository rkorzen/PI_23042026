# pip install paramiko
# pip install python-dotenv
import paramiko
from dotenv import dotenv_values

config = dotenv_values(".env")


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname=config.get("SSH_HOST"),
    username=config.get("SSH_USER"),
    password=config.get("SSH_PASSWORD"),
    port=config.get("SSH_PORT")
)

stdin, stdout, stderr = client.exec_command("ls -al")

print(stdout.read().decode())
print(stderr.read().decode())

client.close()

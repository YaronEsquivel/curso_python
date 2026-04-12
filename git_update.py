import subprocess

subprocess.run("git add .", shell=True)
message = input(" agregar mensaje para el commit > ")
subprocess.run(["git", "commit", "-m", message])
subprocess.run(["git", "push"])

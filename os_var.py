import os

passwd = os.getenv("DBPASS")

if passwd is None:
    passwd = input("give me your password for db")
else:
    print(f"your var in env {passwd}")
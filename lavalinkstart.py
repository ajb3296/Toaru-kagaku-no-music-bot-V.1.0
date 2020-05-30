import os
import multiprocessing
from urllib import request

def child_process(link):
    print(f"Child process PID : {multiprocessing.current_process().pid}")
    request.urlretrieve(link, "Lavalink.jar")
    additional_options = os.environ.get(
            "-Xmx300m"
    )
    os.system("java -jar Lavalink.jar %s" %additional_options)

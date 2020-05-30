import os
import multiprocessing
from urllib import request

def child_process(link):
    print(f"Child process PID : {multiprocessing.current_process().pid}")
    request.urlretrieve(link, "Lavalink.jar")
    os.system("java -jar Lavalink.jar -XX:+UseContainerSupport -Xmx200m -Xss512k -XX:CICompilerCount=2 -Dfile.encoding=UTF-8")

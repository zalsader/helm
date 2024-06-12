import ctypes
import os
import tempfile
import threading


helm = ctypes.cdll.LoadLibrary('./bin/helm.so')
helmCmd = helm.helmCmd
helmCmd.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

with tempfile.NamedTemporaryFile() as helm_out:
    # helmCmd(helm_out.name.encode(encoding="utf-8"), b"helm repo update")
    helm_thread = threading.Thread(target=helmCmd, args=[helm_out.name.encode(encoding="utf-8"), b"helm repo update"])
    helm_thread.start()
    while True:
        output = helm_out.readline().decode(encoding="utf-8")
        if output == "" and not helm_thread.is_alive():
            break
        if output:
            print(output)

#Python Tutorial: Calling External Commands Using the Subprocess Module
'''
O módulo subprocess em Python é usado para executar comandos externos ao seu programa Python.
'''

import subprocess

p1 = subprocess.run('dir', shell=True, capture_output=True, text=True)

#print(p1)

print(p1.args)

print(p1.returncode)

print(p1.stdout)

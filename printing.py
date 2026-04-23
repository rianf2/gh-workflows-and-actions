import sys
import subprocess

print(f'Script name: {sys.argv[0]}')
print(f'Arguments: {sys.argv[1:]}')

subprocess.run(sys.argv[1:])

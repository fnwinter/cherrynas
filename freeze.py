import os
import subprocess

if __name__ == '__main__':
  requirements = None
  process_ = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
  requirements = process_.stdout.splitlines()
  requirements = list(filter(lambda x: not 'cherrynas' in x, requirements))
  
  with open('requirements.txt', 'w') as f:
    f.write("\r\n".join(requirements))

  with open('requirements.py', 'w') as f:
    f.write("req = [\r\n")
    for r in requirements:
      if 'cherrynas' in r: continue
      f.write("  '" + r + "',\r\n")
    f.write("]\r\n")
  print("done")
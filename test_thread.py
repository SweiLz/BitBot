import subprocess
import sys
pid = subprocess.Popen([sys.executable,
                        "BITBOT_display1.py"])
pid2 = subprocess.Popen([sys.executable,
                        "BITBOT_display2.py"])

# You can change this string to modify the allowed characters to use
allowedCharacters = [char for char in "abcdefghijklmnopqrstuvwxz0123456789_-/*?.!#"]
# You can change this variable to modify the amount of characters to use. If 0, then it chooses a random from 8-16
amountOfChars = 0
# You can change this to copy to clipboard. THIS MAY NOT WORK, THERE ISN'T ONE DEFINITIVE WAY TO DO THIS IN PYTHON. VERY OS DEPENDENT
copyToClipboard = True

import random
outputpassword = ""
if amountOfChars == 0:
    amountOfChars = random.randint(8, 16)
for i in range(amountOfChars):
    random.shuffle(allowedCharacters)
    outputpassword += allowedCharacters[1]
print(outputpassword)
if copyToClipboard: # Don't mind this ugly code of me trying to make sure you will always have a way to copy it no matter your os
    try:
        import pyperclip
        pyperclip.copy(outputpassword)
    except:
        try:
            import os
            command = 'echo ' + outputpassword.strip() + '| clip'
            os.system(command)
        except:
            try:
                import subprocess
                process = subprocess.Popen(
                    'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
                process.communicate(outputpassword.encode('utf-8'))
            except:
                try:
                    import pandas as pd
                    df=pd.DataFrame([outputpassword])
                    df.to_clipboard(index=False,header=False)
                except:
                    try:
                        from subprocess import Popen, PIPE
                        p = Popen(['xsel','-pi'], stdin=PIPE)
                        p.communicate(input=outputpassword)
                    except:
                        print("Unable to copy to clipboard")
input("Press enter to close.\n")

from gtts import gTTS 
import os 
mytext = 'tree' 
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)  
myobj.save("/media/syed/ubuntu/ashish/audio/tree.mp3") 
os.system("mpg321 /media/syed/ubuntu/ashish/audio/tree.mp3") 
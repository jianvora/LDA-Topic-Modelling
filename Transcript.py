
 
import speech_recognition as sr 
  
V=sr.AudioFile('V38.wav')
  

  
r = sr.Recognizer() 
  
with V as source: 
  
    audio = r.record(source)   
  
try: 
    print(r.recognize_sphinx(audio)) 
  
except sr.UnknownValueError: 
    print("Sphinx could not understand audio") 
  
except sr.RequestError as e: 
    print("Could not request results from Sphinx service; {0}".format(e))
               


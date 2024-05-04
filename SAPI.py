# # Python SAPI Voice for Windows
# import win32com.client

# speaker = win32com.client.Dispatch("SAPI.SpVoice")

# print("Enter the word you want to speak (-1 to stop)")
# s = input()
# while s != "-1":
#     speaker.Speak(s)
#     print("Enter the word you to speak (-1 to stop)")
#     s = input()

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello, it works!")
# class Bird:

#    def __init__(self):
#      print('Bird is ready')

#    def whoisThis(self):
#      print('Bird')

#    def swim(self):
#      print('Swim faster')

# # child class
# class Penguin(Bird):

#    def __init__(self):
#      # call super() function
#      super().__init__()
#      print('Penguin is ready')

#    def whoisThis(self):
#      print('Penguin')

#    def run(self):
#      print('Run faster')

# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()
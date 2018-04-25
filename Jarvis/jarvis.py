from gtts import gTTS
import mpg123
import test
import speech_recognition as sr
import os
import webbrowser
import smtplib

sounds_folder = os.curdir
counter = 1

def setUp():
	if not os.path.isdir("sound_clips"):
		os.makedirs("sound_clips")
	sounds_folder = "sound_clips"
	os.chdir(sounds_folder)	

"""
creates audio file from text, prints string to console, saves the mp3 file
and then plays it, implements counter to keep track of following audio files
"""
def talkToMe(audio):					
	global counter
	print(audio)								# printing the audio string 
	tts = gTTS(text=audio, lang='en')			# creating a gTTS object
	sound_file = 'audio' + str(counter) + '.mp3'
	tts.save(sound_file)						# saving the gTTS object as mp3 file
	os.system('mpg123 ' + sound_file)			# playing the audio file using mpg123
	counter += 1

# listen for commands
def myCommand():
	recognisor = sr.Recognizer()
	with sr.Microphone() as source:
		print("I am ready for your next command")
		# recognisor.pause_threshold = 1
		recognisor.adjust_for_ambient_noise(source, duration=1)
		audio = recognisor.listen(source)
	try:
		command = recognisor.recognize_google(audio)
		print("You said: " + command)
	# loop back to continue to listen for commands if cant find speech
	except sr.UnknownValueError:
		print("I don't understand!")
		return("ac4t")
	except sr.RequestError:
		print("Makes no sense to me")
		return("ac5t")
	return command

# series of if statesments to execute commands
def assistant(command):

	if 'open Reddit' in command:
		chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application"
		url = "https://www.reddit.com"
		webbrowser.get('windows-default').open(url)
		talkToMe("reddit opened!")

	if 'what\'s up' in command:
		response = "nothing much"
		talkToMe(response)

	if 'ac4t' in command:
		response = "I don't understand"
		talkToMe(response)

	if 'ac5t' in command:
		response = "Makes no sense to me"
		talkToMe(response)

	if 'email' in command:
		talkToMe('who is the recipient?')
		recipient = myCommand()
		if 'Shoaib' in recipient:
			talkToMe("What should I say?")
			content = myCommand()
			# init gmail SMTP
			mail = smtplib.SMTP('smtp.gmail.com', 587)
			# identify to server
			mail.ehlo()
			# encrypt sessions
			mail.starttls()
			username = ""
			password = ""
			mail.login(username, password)
			# send message
			recipient_email = ""
			mail.sendmail(recipient, recipient_email, content)
			# close connection
			mail.close()
			talkToMe("email sent")

def main():
	setUp()
	talkToMe("hello")
	while True:
		command = myCommand()
		assistant(command)

if __name__ == "__main__":
	main()

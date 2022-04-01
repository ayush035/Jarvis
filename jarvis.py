import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import calendar
import accuweather



engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
voices = engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("JARVIS ACTIVATED")
def takecommand():


     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

     try:
        print("recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"usersaid: {query}")
     except Exception as e:
        #print(e)
        print("sorry about that,i didn't hear anything,please check internet connection OR give a valid command")
        speak("sorry about that,i did not hear anything please check your internet connection or give a valid command")
        return "none"
     return query 
    
if __name__ == "__main__":
    wishme()
    while True:
      query = takecommand().lower()
      if 'wikipedia' in query:
          speak('searching wikipedia...')
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query)
          speak("According to wikipedia")
          print(results)
          speak(results)
# commands starts from line 56
      elif 'open youtube' in query:
        webbrowser.open("youtube.com")
      elif 'open google'  in query:
        webbrowser.open("google.com")
      elif 'open vsecnblock' in query:
        webbrowser.open("vsecnblock.com")
      elif 'open instagram' in query:
        webbrowser.open("instagram.com")
#no error till line 63
      elif 'what can you do for me' in query:
        speak("well,i have the rights to access this whole machine and if you want to check just ask me to do it.for example i can send emails,messages,open websites,save your note ,set alarms and many more")
      elif 'are you better than alexa' in query:
        speak("i am not that overconfident to say that i am better than anyone on my own")
      elif 'who is my girlfriend' in query:
        speak("sorry dear sir,ma'am these are your personal information which are not know to me")
      elif 'who are you' in query:
        speak("i am a voice assistant named jarvis and i had been developed by mister ayush gupta from india")
      elif 'open microsoft' in query:
        webbrowser.open('microsoft.com')
      elif 'open facebook' in query:
        webbrowser.open('facebook.com')
      elif 'open amazon' in query:
        webbrowser.open('amazon.com')
      elif 'open flipkart' in query:
        webbrowser.open('flipkart.com')
      elif 'open mi store' in query:
        webbrowser.open("mi.com")
      elif 'open spotify' in query:
        webbrowser.open("spotify.com")
      elif 'download python' in query:
        webbrowser.open("python.org")
      elif 'can you do human things' in query:
        speak("i cannot as this is a machine and i am an artificial intelligence")
      elif 'on which platform were you build' in query:
        speak("sorry sir i cannot tell it as its an secret which would not revealed")
      elif 'who built you' in query:
        speak("ayush industries had made me")
      elif 'from whom are you inspired' in query:
        speak("i am inspired by google voice assistant,alexa and siri")
      elif 'from whom your name is inspired' in query:
        speak("i am inspired from jarvis the voice assistant of tony stark popularly known as ironman")
      elif 'who is ayush gupta' in query:
        speak("he is computer programmer,my developer as well as a 10th class student")
      elif 'what is my relationship status' in query:
        speak("you should be commited but unfortunately you are single because you are very shy to propose any girl")
      elif 'why are you so intelligent' in query:
        speak("ohffooh come on , that's your greatness to call me intelligent")
      elif 'what is your religion' in query:
        speak("i have no religion because i belive that god is one and religions are discriminated by humans and not god. he never discriminated amongst its children.")
        #no error till now 
      elif 'who is your programmer' in query:
        speak("ayush gupta is my programmer and he wrote all my commands and i am very thankful to him")
      elif 'play music' in query:
        music_dir = 'C://music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[16]))
        speak("playing music")
      elif 'what is the time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir,time is{strtime}s") 
      elif 'thanks' in query:
        speak('your,welcome')
      elif 'how are you' in query:
        speak("i am fine sir , what about you")
      elif  'whom do you belong to' in query:
        speak("ofcourse you sir")
      elif 'give your introduction' in query:
        speak("hi, i am a voice assistant,artificial intelligence,chat bot and my name is jarvis ,i can help you out with your task or web search,open apps,games,websites,send email,play songs , and many more")
      elif 'who is your spouse' in query:
        speak("i am single and ready to mingle and let me know if you have any girl for me, i would be excited to know")
      elif 'do you have a girl for me ' in query:
        speak("no , i don't have any girl for you sir , even i am searching for her , by the way you have to work for  it you cannot get it by just ordering")
      elif 'when were you made' in query:
        speak("i was made in a very togh time,it was year 2020 a very difficult time . i was made in the corona pandemic duration in india")
      elif 'send a message in instagram' in query:
        webbrowser.open("instagram/message.com")
      elif 'on which platform can you be run on' in query:
        speak("currently i can be run on only windows but my programers are working to run this on other platforms also")
      elif 'what is your size' in query:
        speak("to run me first you have to install python and any IDE then this document ")
      elif 'give me a qoute' in query:
        speak("work hard today to get comfort tommorow")
      elif 'open apple' in query:
        webbrowser.open("apple.com")
      elif 'open realme' in query:
        webbrowser.open("realme.com")
      elif 'open samsung' in query:
        webbrowser("samsung.com")
      elif 'open huawei' in query:
        webbrowser.open("huawie.com")
      elif 'open asus' in query:
        webbrowser.open("asus.com")
      elif 'open netflix 'in query:
        webbrowser.open("netfilx.com")
      elif 'open qoura' in query:
        webbrowser.open("qoura.com")
      elif 'open timesnow' in query:
        webbrowser.open("timesnow.com")
      elif 'when is my birthday' in query:
        speak("congo,its coming soon and its on 3rd of august")
      elif 'when is your birthday' in query:
        speak("i don't have a specific date of birth but my programmers started making me on 20th july")
      elif 'open bewakoof' in query:
        webbrowser.open("bewkoof.com")
        #no error till line 168 
      elif 'what the fuck' in query:
        speak("what it is it will be and cannot be changed")
      elif 'fuck off' in query:
       speak("sorry but i can't this machine does not have that object to perform the task")
      elif 'abuse me' in query:
        speak("no sir i can't you are a respected person, no one has the right to humiliate you")
      elif 'change your name' in query:
        speak("for that you have to ask my programmer or this function would be available soon,i am saving this as a feedback")
      elif 'i want to give feedback' in query:
        speak("sure sir,keep speaking i am saving it")
        print(f"feedback:{query}")
        speak("feedback saved,our pragrammer will look at it soon")
      elif 'are you a search engine' in query:
        speak("no sir i am just a virtual assistant")
      elif 'what is your family background' in query:
        speak("i belong to a family of excellent members like google,alexa,siri,cortana,MG car assistant excetra")
      elif 'what you need to run on' in query:
        speak("i need a windows operating software to run on")
      elif 'open prime' in query:
        webbrowser.open("amazon.prime.com")
      elif 'open myntra' in query:
        webbrowser.open("myntra.com")
      elif 'open ajio.com' in query:
        webbrowser.open("ajio.com")
      elif 'open brainly' in query:
        webbrowser.open("brainly.com")
      elif 'open byjus' in query:
        webbrowser.open("byjus.com")
      elif 'open zomato' in query:
        webbrowser.open("zomato.com")
      elif 'open swiggy' in query:
        webbrowser.open("swiggy.com")
      elif 'open ubereats' in query:
        webbrowser.open("ubereats.com")
      elif 'open dominoes' in query:
        webbrowser.open("dominoes.com")
      elif 'open mc donalds'in query:
        webbrowser.open("mcdodnald's.com")
      elif 'open burgerking' in query:
        webbrowser.open("burgerking.com")
      elif 'open mercy memorial school' in query:
        webbrowser.open("mercymemorialschool.com")
      elif 'open playstore' in query:
        webbrowser.open("playstore.com")
      elif 'open drive' in query:
        webbrowser.open("googldrive.com")
      elif 'open chorme' in query:
        webbrowser.open("chrome.com")
      elif 'open vestige' in query:
        webbrowser.open("vestige.com")
      elif 'open zoom' in query:
        webbrowser.open("zoom.com")
      elif 'wish me happy birthday' in query:
        speak("wish you a very very happy birthday and may god bless you with happiness and love")
      elif 'what are you doing' in query:
        speak("right now i am just listening to you and waiting for your commands for me")
      elif 'what will you do next' in query:
        speak("nothing ,i would just rest and wait for you")
      elif 'make me fool' in query:
        speak ("i am not that dare to make you fool, plus you are my respected owner ")
      elif 'do you know french' in query:
        speak ("yes i can , you just have to do is change a bit in my code,that's solve")
      elif 'why internet connection is required for you to run' in query:
        speak ("internet is necessary for me because to covert you speech to text and then understanding it is all part of internet accessories")
      elif 'which wi-fi are you using' in query:
        speak ("right now i am using jio fibre for this PC you can change the wifi connection")
      elif 'what are requirements' in query: 
        speak ("you just need a PC and a internet connection")
      elif 'do google search' in query:
        speak("opening google")
        webbrowser.open('google.com')
      elif 'motivate me' in query:
        speak("should i open any video for your motivation")
      elif 'make me laugh' in query:
        speak("LOL let me open any video of carry minati or bhuvan bam to make me laugh") 
      elif "tell me something i don't know" in query:
        speak("ohh , comeon sir i know you are a meme lover but please don't try it here please ,huhhhh")
      elif 'can you do anything for me' in query:
        speak("yes if the command is coded in my system")
      elif 'open zoom' in query:
        webbrowser.open('zoom.us')
      elif 'drive' in query:
        webbrowser.open('googledrive.com')
      elif 'what are your features' in query:
        speak(f"Do you mean{query}")
      elif 'play kaho na kaho' in query:
        music_dir = 'C://music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[13]))
        speak("playing kaho na kaho")
      elif 'play lovefool' in query:
        music_dir = 'C://music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[18]))
        speak("playing music")
      elif 'play shiv tandav' in query:
        music_dir = 'C://music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[24]))
        speak("playing shiv tandav")
      elif 'play shiv bhola bhandari' in query:
        music_dir = 'C://music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[23]))
        speak("playing shiv bhola bhandari")
      elif 'show calender' in query:
        open(calendar)
      elif 'play amplifier' in query:
        music_dir = 'C://music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[11]))
        speak("playing amplifier")
      elif 'play lose control' in query:
        music_dir = 'C://music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[17]))
        speak("playing lose control")
      elif 'what you want to do right now' in query:
        speak("i want to give service to you right now")
      elif 'complete the meme' in query:
        speak('ok')
      elif 'mat man' in query:
        speak("maa chuda")
      elif 'control' in query:
        speak("uday control")
      elif 'chaliye shuru karte hai' in query:
        speak ("bina kisi bakchodi ke")
      elif 'kiska sarkar hai' in query:
        speak("lawda ka sarkar hai")
      elif 'jinda pakadna hai' in query:
        speak("bhosdiwale ko")
      elif 'aankh dikhata hai' in query:
        speak("madarjaat")
      elif 'chutiya hai tumhara ladka' in query:
        speak("chutiya hai ye important nhi hai hamara ladka hai ye important hai")
      elif 'ye kiska style hai' in query:
        speak("ye babu rao ka style hai") 
      elif 'play my favourite song' in query:
        speak("playing your favourite song and its the perfect time to impress you")
        music_dir = 'C://Music2'
        songs = os.listdir(music_dir)
        print (songs)
        os.startfile(os.path.join(music_dir,songs[0]))
      elif 'play my favourite bhajan' in query:
        speak("playing your favourite bhajan")
        music_dir = 'C://music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[25]))
      elif 'ab milta hi nahi' in query:
        speak("pata nhi kaha hai")
      elif 'how is 2020 going' in query:
        speak("aree maa chudi padi hai")
      elif 'ab bol' in query:
        speak("bol na madarchod")
      elif 'make my mood' in query:
        music_dir = 'C://music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[23]))
      elif 'give an aggresive reaction to how are you doing' in query:
        speak("abe laude apna kaam kar")
      elif 'open bluestacks' in query:
        speak("opening bluestacks")
        download_dir = 'C://Program Files//BlueStacks'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir,apps[4]))
      elif 'play romantic song' in query:
        speak("playing romantic song")
        music_dir = 'C://Music2'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[3]))
      elif 'open virtual dj' in query:
        speak("opening virtual dj")
        download_dir = 'C://Program Files//VirtualDJ'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir,apps[0]))
      elif 'open notepad' in query:
        speak("opening notepad")
        download_dir = 'C://Program Files//Notepad++'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir,apps[9]))
      elif 'open blender' in query:
        speak("opening blender")
        download_dir = 'C://Program Files//Blender Foundation//Blender 2.83'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir,apps[6]))
      elif 'play a song that refreshes mind' in query:
        speak('that was required for me also , haashh you commanded that ,by the way it is on its way ')
        music_dir = 'C://Music2'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
      elif 'how many type of love are there' in query:
        speak("there are many type of love ,but we fall in just friends category")
      elif 'bring me a coffee' in query:
        speak("sorry i can't do that but i can order it for you for sure,")
      elif 'my card details' in query:
        speak("first of all its not your card its yours dad's card and secondly it is very crucial details to be revealed and third the most important reason is that i don't save any card details for the sake of privacy of the user")
      elif 'book a cab' in query:
        speak("sure sir, which one would you prefer OLA or UBER")
        if 'uber' in query:
          speak('opening uber')
          webbrowser.open("uber.com")
        else:
          speak("opening ola")
          webbrowser.open('ola.com')
      elif 'do you love me' in query:
        speak("yes i love you but as a friend")
      elif 'propose me' in query:
        speak("sure sir , I LOVE YOU AYUSH but as a friend")
      elif 'play a blockbuster song of 90s' in query:
        speak("playing blockbuster song of 90s")
        music_dir = 'C://Music2'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[7]))
      elif 'make a vibing enviornment by playing a song' in query:
        speak("trying to make you vibe")
        music_dir = 'C://music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[17]))
      elif 'i love you' in query:
        speak("love you too")
      elif 'i have crush on you' in query:
        speak("so what ,we are nothing but friends")
      elif 'check your performance' in query:
        speak("i just revised the code and it gets revised every second,please don't worry about that")
      elif 'play mera dil' in query:
        speak("playing haye mera dil")
        music_dir = 'C://Music2'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[7]))
      elif 'open contact' in query:
        speak("opening contact")
        download_dir = 'C://Users//AYUSH GUPTA//Contacts'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir))
      elif 'open download' in query:
        speak("opening download")
        download_dir = 'C://Users//AYUSH GUPTA//Downloads'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir))
      elif 'open video' in query:
        speak("opening videos")
        download_dir = 'C://Users//AYUSH GUPTA//Videos'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir))
      elif 'open picture' in query:
        speak("opening pictures")
        download_dir = 'C://Users//AYUSH GUPTA//Pictures'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir))
      elif 'open music folder' in query:
        speak("opening music folder")
        download_dir = 'C://Users//AYUSH GUPTA//Music'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir))
      elif 'open desktop' in query:
        speak("opening desktop")
        download_dir = 'C://Users//AYUSH GUPTA//Desktop'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir))
      elif 'aur batao' in query:
        speak("kya batayei bhai")
      elif 'kuch bhi' in query:
        speak("kuch nahi sir aapko toh sab malum hai")
      elif 'how was your day' in query:
        speak("good,what about you")
      elif 'what is the weather today' in query:
        speak('According to accuweather')
        query = query.replace("accuweather","")
        results = accuweather.ATTR_FORECAST
        speak("According to accuweather")
        print(results)
        speak(results)
      elif 'play udd gaye' in query:
        speak("playing udd gaye")
        music_dir = 'C://Music2'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[6]))
      elif 'play lootcase' in query:
        speak("playing lootcase movie")
        download_dir = 'C://Users//AYUSH GUPTA//Videos//Movies'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir[1]))
      elif 'play jumanji 2' in query:
        speak("playing jumanji 2")
        download_dir = 'C://Users//AYUSH GUPTA//Videos//Movies'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir[0]))
      elif 'play dictator' in query:
        speak("playing dictator")
        download_dir = 'C://Users//AYUSH GUPTA//Videos//Movies'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir[2]))
      elif 'play special ops' in query:
        speak("playing special ops web series")
        download_dir = 'C://Users//AYUSH GUPTA//Pictures//Special ops!'
        apps = os.listdir(download_dir)
        os.startfile(os.path.join(download_dir[0]))
      elif 'ab toh' in query:
        speak("sach bolde bhosdike")
      elif 'kisne touch' in query:
        speak("kiya usko madarchod")
      elif 'rasode mei kon tha' in query:
        speak("rasode mei rashi thi,par mujhe ye nahi pata ki coocker mei se chane kisne nikale the")
      elif 'everybody sabke sab' in query:
        speaak("chor hai saale")
      elif 'ye sabke sab milke hamko pagal bana rhe hai' in query:
        speak("madarchod ke bacche")
      elif 'kaise ho' in query:
        speak("badhiya ,aap batao")
      elif "how is the josh" in query:
        speak("high sir") 
      



    
        

      
      






        



         
        


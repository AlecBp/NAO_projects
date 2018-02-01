import time
import speech_recognition as sr
import wikipedia
r = sr.Recognizer("en-US")
replaceList = ["u'", "[", "]", "'"]
pageContent = ""
#pageTitle = ""

def audioStuff():
    timeHolder = time.time()
    #print "Started recog process"
    with sr.WavFile("teste4.wav") as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file

    try:
        list = r.recognize(audio,True)                  # generate a list of possible transcriptions
        #print("Possible transcriptions:")
        result = []
        for prediction in list:
            #print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
            result.append(prediction["text"])
    except LookupError:                                 # speech is unintelligible
        print("Could not understand audio")

    result = str(result)
    for word in replaceList:
        result = result.replace(word, "")
    result = result.split(",")
    #timerAudioStuff = time.time()-timeHolder
    #print str(timerAudioStuff)+" timerAudioStuff"
    return result[0]

def getPage():
    pageContentArray = []
    page = wikipedia.page(audioStuff())
    pageTitle = page.title
    pageContentArray.append(pageTitle)
    pageContent = page.content
    pageContentArray.append(pageContent)
    pageContentSplited = pageContent.split("== Forms ==")
    pageContentFirstParagraph = pageContentSplited[0]
    pageContentArray.append(pageContentFirstParagraph)
    return pageContentArray

def benchMark(samples):
    timerBenchMark=0
    for x in range (samples):
        timeHolder = time.time()
        audioStuff()
        timerBenchMark = timerBenchMark + (time.time() - timeHolder)
        #print str(timerBenchMark)+" timerBenchMark, test number" + str(x) + "of " + str(samples)
    return timerBenchMark/x+1

print "_____________________" + "\n" + "MEAN: " + str(benchMark(50))
#dataOutput = getPage()
#print dataOutput[2]
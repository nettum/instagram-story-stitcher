import json
from os import path, getcwd, remove
from dateutil import parser
from datetime import datetime
from glob import glob
from time import time
import subprocess

def getVideoStoriesFromJsonFiles():
    combinedJsonData = []

    for jsonFile in glob('json/*.json'):
        file = open(jsonFile)
        data = file.read()
        jsonData = json.loads(data)
        for story in jsonData['stories']:
            if story['path'].endswith('.mp4') and path.exists(story['path']):
                combinedJsonData.append(story)
        file.close()
        
    stories = sorted(combinedJsonData, key=lambda item:item['taken_at'])
    return stories

def generateFfmpegInputFiles(stories):
    lastStoryTS = 0

    for story in stories:
        dateObj = parser.parse(story['taken_at'])
        storyTS = datetime.timestamp(dateObj)
        if (storyTS - lastStoryTS > 60):
            if (lastStoryTS != 0):
                tmpFile.close()
            key = dateObj.strftime('%Y%m%d_%H%M')

        tmpFile = open('out/' + key + '.tmp', 'a')
        tmpFile.write('file ' + getcwd() + '/' + story['path'] + '\n')
        lastStoryTS = storyTS

def convertVideoFilesToStories():
    numStories = 0
    for file in glob('out/*.tmp'):
        storyFilename = file.replace('tmp', 'mp4')
        print('Generating story %s...' % (storyFilename))
        subprocess.call(['ffmpeg', '-hide_banner', '-loglevel', 'warning', '-f', 'concat', '-safe', '0', '-i', file, '-c', 'copy', storyFilename ])
        remove(file)
        numStories += 1
    return numStories

def main():
    startTime = time()
    print('\n\nGenerating stories\n\n')

    stories = getVideoStoriesFromJsonFiles()
    generateFfmpegInputFiles(stories)
    numStories = convertVideoFilesToStories()

    endTime = time()
    timeTaken = endTime - startTime
    print('\n\nDONE!\nConverted %s videofiles into %s stories in %.2f seconds\n\n' % (len(stories), numStories, timeTaken))

main()

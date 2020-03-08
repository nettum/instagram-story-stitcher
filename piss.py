import json
from os import path, getcwd, remove
from dateutil import parser
from datetime import datetime
import glob
import subprocess

def main():
    file = open('json/media.json')
    data = file.read()
    jsonData = json.loads(data)
    file.close()
    stories = sorted(jsonData['stories'], key=lambda item:item['taken_at'])
    lastStoryTS = 0

    for story in stories:
        if story['path'].endswith('.mp4') and path.exists(story['path']):
            dateObj = parser.parse(story['taken_at'])
            storyTS = datetime.timestamp(dateObj)
            if (storyTS - lastStoryTS > 60):
                key = dateObj.strftime('%Y%m%d_%H%M')
            tmpFile = open('out/' + key + '.tmp', 'a')
            tmpFile.write('file ' + getcwd() + '/' + story['path'] + '\n')
            lastStoryTS = storyTS
    tmpFile.close()

    for file in glob.glob('out/*.tmp'):
        storyFilename = file.replace('tmp', 'mp4')
        print('Generating story ' + storyFilename + '...')
        subprocess.call(['ffmpeg', '-hide_banner', '-loglevel', 'warning', '-f', 'concat', '-safe', '0', '-i', file, '-c', 'copy', storyFilename ])
        remove(file)

main()

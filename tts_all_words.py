import subprocess
from concurrent.futures.thread import ThreadPoolExecutor
import os

MAX_WORKERS=4

def generate_tts(infile, outfile):
    subprocess.call(['flite', infile, '-o', outfile])
    return

# for each word/string, create
def generate_tts_for_string(fname, string, outdir):
    outpath = '%s/%s'%(outdir, fname)
    try:
        subprocess.call(['mkdir', outpath])
        with open('%s/%s.txt'%(outpath,fname), 'w') as f:
            f.write(string)
        generate_tts("%s/%s.txt"%(outpath,fname), '%s/%s.wav'%(outpath,fname))
    except Exception as e:
        print(e)
        pass

def done_tts(future):
    return

if __name__=="__main__":
    with open('corncob_lowercase.txt','r') as f:
        words = [line.strip() for line in f.readlines()]
    print(len(words))

    #indir = '/home/kruppe/Projects/english_words_tts/data'
    outdir = '/home/kruppe/Projects/english_words_tts/data'
    for i, w in enumerate(words[:10000]):
        with ThreadPoolExecutor(MAX_WORKERS) as executor:
            executor.submit(generate_tts_for_string, i, w, outdir)
    
    


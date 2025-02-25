#from transformers import T5Tokenizer, T5ForConditionalGeneration
#from datasets import load_dataset
#from rouge_score import rouge_scorer
#from bert_score import score
#import torch
import os
import xml.etree.ElementTree as ET


# processing 1 xml file
def load_transcript(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    transcript = []
    for word in root.findall(".//w"):
        if word.text:
            transcript.append(word.text)
    return " ".join(transcript)

def all_transcripts(path):
    transcripts = {}
    for file in os.listdir(path):
        if file.endswith(".words.xml"):
            file_path = os.path.join(path, file)
            m_id = file.split(".")[0]
            transcripts[m_id] = load_transcript(file_path)
    return transcripts

path = "/Users/elizamg/Desktop/224nProject/ICSIplus/Words"

transcripts = all_transcripts(path)

for meeting, text in transcripts.items():
    print(f"Meeting {meeting}:\n{text[:500]}...\n")
    break
#from transformers import T5Tokenizer, T5ForConditionalGeneration
#from datasets import load_dataset
#from rouge_score import rouge_scorer
#from bert_score import score
#import torch
import os
import xml.etree.ElementTree as ET
import json


# processing 1 xml file
def load_transcript(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    transcript = []
    for word in root.findall(".//w"):
        if word.text:
            transcript.append(word.text)
    return " ".join(transcript)

# processing all json files

def all_transcripts(path):
    transcripts = {}
    for file in os.listdir(path):
        if file.endswith(".words.xml"):
            file_path = os.path.join(path, file)
            m_id = file.split(".")[0]
            transcripts[m_id] = load_transcript(file_path)
    return transcripts

path = "/Users/elizamg/Desktop/224nprojectgit/224nProject/ICSIplus/Words"

transcripts = all_transcripts(path)

# saving data
def save_json(transcripts):
    output_folder = "/Users/elizamg/Desktop/224nprojectgit/224nProject/transcripts"
    os.makedirs(output_folder, exist_ok = True)

    for meeting_id, transcript in transcripts.items():
        file_path = os.path.join(output_folder, f"{meeting_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump({"meeting_id": meeting_id, "transcript": transcript}, f, indent=4)

    print(f"Saved {len(transcripts)} transcripts as JSON.")
save_json(transcripts)

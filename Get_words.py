import json
import re
from typing import Set

def clean_data_chapters(words: Set[str]) -> Set[str]:
    """
    Clean the set of words by removing punctuation, numbers, and normalizing case.

    Args:
        words (Set[str]): A set of words from the transcription.

    Returns:
        Set[str]: A cleaned set of words with punctuation and numbers removed.
    """
    cleaned_words = {
        re.sub(r'\d+', '', re.sub(r'[^\w\s]', '', word)).strip().lower()
        for word in words
    }
    return {word for word in cleaned_words if word}  # Filter out empty strings

def get_words_from_transcription(json_filename: str) -> Set[str]:
    """
    Extract words from the transcription JSON file.

    Args:
        json_filename (str): The name of the JSON file with transcription data.

    Returns:
        Set[str]: A set of words extracted from the transcription.
    """
    try:
        with open(json_filename, 'r') as file:
            transcription_data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {json_filename} does not exist.")
    except json.JSONDecodeError:
        raise ValueError(f"The file {json_filename} is not a valid JSON file.")
    
    text = transcription_data.get('text', '')
    words = set(text.split())
    return words

def save_words_to_json(words: Set[str], output_filename: str) -> None:
    """
    Save the set of words to a JSON file.

    Args:
        words (Set[str]): A set of cleaned words.
        output_filename (str): The name of the output JSON file.
    """
    try:
        with open(output_filename, 'w') as file:
            json.dump(list(words), file, indent=4)
        print(f"Cleaned words saved to {output_filename}")
    except IOError as e:
        print(f"An error occurred while writing to {output_filename}: {e}")

if __name__ == "__main__":
    input_json_filename = 'transcription_result.json'
    output_json_filename = 'cleaned_words.json'
    
    try:
        words = get_words_from_transcription(input_json_filename)
        cleaned_words = clean_data_chapters(words)
        save_words_to_json(cleaned_words, output_json_filename)
    except Exception as e:
        print(f"An error occurred: {e}")

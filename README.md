# 📚 WordTube-Anki

This project allows users to **practice vocabulary from specific videos** by focusing on targeted words within the video content. By providing a transcript of the video, the tool extracts individual words and enables users to practice them through **Anki**, a popular flashcard application. The tool is designed to simplify learning new vocabulary by breaking down the words and seamlessly integrating with Anki for effective retention.

## 🎯 What is this project?

- Extracts **specific words from a video transcript**, allowing focused vocabulary practice.
- You can practice a **specific set of vocabulary** derived directly from the video's content, ensuring contextual learning.

## 🔧 What do we need here?

- **📝 A text file** containing the transcription of the video.
  - The transcription will be processed.
  - Each word will be separated and prepared for vocabulary practice.
- **🔗 Connection to Anki** to create corresponding flashcards for each word, enabling smooth integration and review.

## 📂 Folder Structure:

- **`Transcription.py`**: Handles video transcription and converts the audio to text.
- **`Get_words.py`**: Extracts and processes individual words from the transcription.
- **`Connect_Anki.py`**: Connects with Anki to upload and create vocabulary flashcards based on the extracted words.

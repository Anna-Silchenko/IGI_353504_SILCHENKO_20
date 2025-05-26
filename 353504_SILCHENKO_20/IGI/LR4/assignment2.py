#!/usr/bin/env python3
"""
Program: Text Analysis and Processing from File
Lab Number: Lab #4
Version: 1.1
Developer: Сильченко Анна
Date: 2025-05-07

Purpose:
    This module reads text from a source file, analyzes the text using regular expressions,
    and extracts various information:
      - Total number of sentences and counts by type (declarative, interrogative, exclamatory).
      - Average sentence length (sum of word lengths) and average word length.
      - Count of emoticons matching a specified pattern.
      - List of dates in the format with year 2007.
      - Extraction of special words from the text where the third character from the end is a consonant
        and the penultimate character is a vowel.
    The analysis results are displayed on the screen, saved to a result file, and then the result
    file is archived using zipfile.
"""

import re
import zipfile
import os
import statistics

def read_text_file(filename: str) -> str:
    """
    Read the entire contents of a text file.

    Parameters:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file.

    Raises:
        IOError: If the file cannot be opened.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

class TextAnalyzer:
    """
    A class for analyzing text.

    Methods:
        analyze_sentences: Count total sentences and categorize them by type.
        average_sentence_length: Compute the average sentence length in terms of letters of words.
        average_word_length: Compute the average word length.
        count_emoticons: Count emoticons in the text based on a specified regex pattern.
        extract_dates: Extract dates matching the pattern with year 2007.
        extract_special_words: Extract words where the third from last letter is a consonant and the penultimate letter is a vowel.
    """
    def __init__(self, text: str):
        self.text = text
        # Split text into sentences (using lookbehind to include punctuation)
        self.sentences = re.split(r'(?<=[.!?])\s+', text)
        self.words = re.findall(r'\b\w+\b', text)

    def analyze_sentences(self) -> dict:
        """
        Count the total number of sentences and categorize them by type.

        Returns:
            dict: Contains total, declarative, interrogative, and exclamatory sentence counts.
        """
        counts = {"total": 0, "declarative": 0, "interrogative": 0, "exclamatory": 0}
        for sentence in self.sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            counts["total"] += 1
            if sentence.endswith('.'):
                counts["declarative"] += 1
            elif sentence.endswith('?'):
                counts["interrogative"] += 1
            elif sentence.endswith('!'):
                counts["exclamatory"] += 1
        return counts

    def average_sentence_length(self) -> float:
        """
        Compute the average length of sentences in terms of total letters of words (ignoring spaces and punctuation).

        Returns:
            float: The average sentence length.
        """
        lengths = []
        for sentence in self.sentences:
            words = re.findall(r'\b\w+\b', sentence)
            word_lengths = [len(word) for word in words]
            if word_lengths:
                lengths.append(sum(word_lengths))
        if lengths:
            return sum(lengths) / len(lengths)
        return 0.0

    def average_word_length(self) -> float:
        """
        Compute the average word length in the text.

        Returns:
            float: The average length of words.
        """
        if self.words:
            total = sum(len(word) for word in self.words)
            return total / len(self.words)
        return 0.0

    def count_emoticons(self) -> int:
        """
        Count emoticons in the text.
        An emoticon is defined as follows:
          - It must start with ':' or ';'
          - Followed by zero or more '-' characters
          - Ending with one or more identical brackets (one of '(', ')', '[' or ']')
          - The emoticon should be bounded by whitespace or punctuation.

        Returns:
            int: The number of valid emoticons found.
        """
        # Improved regular expression:
        pattern = re.compile(r'([:;])(-*)([\(\)\[\]])\3+')

        emoticons = pattern.findall(self.text)
        return len(emoticons)

    def extract_dates(self) -> list:
        """
        Extract dates matching the pattern with the year 2007.

        Returns:
            list: A list of date strings.
        """
        pattern = re.compile(r'\b\d{1,2}[./-]\d{1,2}[./-]2007\b')
        return pattern.findall(self.text)

    def extract_special_words(self) -> list:
        """
        Extract words from the text where the third from last letter is a consonant
        and the penultimate letter is a vowel.

        Returns:
            list: A list of words satisfying the condition.
        """
        vowels = "aeiouAEIOU"
        special_words = []
        for word in re.findall(r'\b\w+\b', self.text):
            if len(word) >= 3:
                if (word[-3].lower() not in vowels) and (word[-2].lower() in vowels):
                    special_words.append(word)
        return special_words

def analyze_specific_line(line: str) -> dict:
    """
    Analyze a given line by performing word-based analysis:
      - Extract words where the third from last letter is a consonant and the penultimate letter is a vowel.
      - Count the total number of words.
      - Determine the longest word and its 1-based position.
      - Extract words in odd positions.

    Parameters:
        line (str): The line to analyze.

    Returns:
        dict: Dictionary with keys 'special_words', 'total_words', 'longest_word', and 'odd_words'.
    """
    vowels = "aeiouAEIOU"
    words = re.findall(r'\b\w+\b', line)
    special_words = []
    for word in words:
        if len(word) >= 3:
            if (word[-3].lower() not in vowels) and (word[-2].lower() in vowels):
                special_words.append(word)
    
    total_words = len(words)
    if words:
        longest = max(words, key=len)
        position = words.index(longest) + 1  # 1-based indexing
    else:
        longest, position = "", 0
    odd_words = [word for idx, word in enumerate(words, start=1) if idx % 2 == 1]
    
    return {
        "special_words": special_words,
        "total_words": total_words,
        "longest_word": (longest, position),
        "odd_words": odd_words
    }

def save_text_to_file(filename: str, content: str):
    """
    Save the given content to the specified file.

    Parameters:
        filename (str): Name of the file.
        content (str): Content to be saved.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def archive_file(zip_filename: str, file_to_archive: str):
    """
    Archive the specified file using zipfile and print archive details.

    Parameters:
        zip_filename (str): Name of the zip archive.
        file_to_archive (str): The file to archive.
    """
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_to_archive, arcname=os.path.basename(file_to_archive))
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        info = zipf.infolist()
        for fileinfo in info:
            print(f"Archived: {fileinfo.filename}, Size: {fileinfo.file_size} bytes")

def analyze_text_file(source_filename: str, result_filename: str):
    """
    Read text from 'source_filename', perform text analysis, and save the results.
    If the file contains multiple lines, the user is asked to choose one for detailed analysis.
    The report is printed, saved to 'result_filename', and then archived.

    Parameters:
        source_filename (str): Input text file name.
        result_filename (str): Filename to save the analysis report.
    """
    try:
        full_text = read_text_file(source_filename)
    except IOError as e:
        print(f"Error reading file {source_filename}: {e}")
        return

    analyzer = TextAnalyzer(full_text)
    sentence_stats = analyzer.analyze_sentences()
    avg_sentence_len = analyzer.average_sentence_length()
    avg_word_len = analyzer.average_word_length()
    emoticon_count = analyzer.count_emoticons()
    dates = analyzer.extract_dates()
    special_words_global = analyzer.extract_special_words()

    report_lines = []
    report_lines.append("=== Global Text Analysis ===")
    report_lines.append(f"Total number of sentences: {sentence_stats['total']}")
    report_lines.append(f"  Declarative sentences: {sentence_stats['declarative']}")
    report_lines.append(f"  Interrogative sentences: {sentence_stats['interrogative']}")
    report_lines.append(f"  Exclamatory sentences: {sentence_stats['exclamatory']}")
    report_lines.append(f"Average sentence length (in letters): {avg_sentence_len:.2f}")
    report_lines.append(f"Average word length: {avg_word_len:.2f}")
    report_lines.append(f"Emoticon count: {emoticon_count}")
    report_lines.append(f"Dates found (year 2007): {dates}")
    report_lines.append(f"Special words (global extraction): {special_words_global}")
    report_lines.append("")

    lines = full_text.splitlines()
    if not lines:
        print("The source text is empty.")
        return

    if len(lines) > 1:
        print(f"The source file contains {len(lines)} lines.")
        while True:
            try:
                line_num = int(input(f"Enter the line number (1 - {len(lines)}) to analyze further: "))
                if 1 <= line_num <= len(lines):
                    chosen_line = lines[line_num - 1]
                    break
                else:
                    print("Invalid line number. Try again.")
            except ValueError:
                print("Please enter a valid integer.")
    else:
        chosen_line = lines[0]
        print("The source file contains only one line.")

    line_analysis = analyze_specific_line(chosen_line)
    report_lines.append("=== Detailed Analysis for the Chosen Line ===")
    report_lines.append(f"Chosen line: {chosen_line}")
    report_lines.append(f"Total number of words: {line_analysis['total_words']}")
    longest_word, pos = line_analysis["longest_word"]
    report_lines.append(f"Longest word: '{longest_word}' at position {pos}")
    report_lines.append(f"Words in odd positions: {line_analysis['odd_words']}")
    report_lines.append(f"Special words (line extraction): {line_analysis['special_words']}")

    report_content = "\n".join(report_lines)
    print("\n" + report_content)

    save_text_to_file(result_filename, report_content)
    print(f"\nReport saved to {result_filename}")
    zip_filename = result_filename.rsplit('.', 1)[0] + ".zip"
    archive_file(zip_filename, result_filename)

if __name__ == "__main__":
    source_file = input("Enter the source text file name: ").strip()
    result_file = "text_analysis_report.txt"
    analyze_text_file(source_file, result_file)

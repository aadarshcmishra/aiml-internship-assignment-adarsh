def word_frequency(paragraph):
    """Calculates word frequency in a paragraph."""
    words = paragraph.lower().replace('.', '').split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict
  print(f"3. Frequency 'Hello world hello': {word_frequency('Hello world hello')}")
   

import difflib
def is_plagiarism(text1, text2):
    # Calculate the similarity score between the two texts.
    similarity_score = difflib.SequenceMatcher(None, text1, text2).ratio()
    # Return True if the similarity score is greater than or equal to the threshold.
    return similarity_score >= THRESHOLD
# Set the plagiarism threshold.
THRESHOLD = 0.5
# Get the two texts to be compared.
text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")
# Check if the two texts are plagiarized.
if is_plagiarism(text1, text2):
    print("The two texts are plagiarized.")
else:
    print("The two texts are not plagiarized.")
# Lesson 6: Assignments | Python Strings
# Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!
# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!
# ________________________________________
# 1. Product Review Analysis
# Objective: The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter
# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.
reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is good excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was poor average. Nothing extraordinary about it." ]
keywords = ["good", "excellent", "bad", "poor", "average"]

def highlight_keywords(reviews, keywords):
  
  highlighted_reviews = []
  for review in reviews:
    highlighted_review = review  # Create a copy to avoid modifying the original review
    for keyword in keywords:
      # Use case-insensitive matching for flexibility
      if keyword.lower() in review.lower():
        # Preserve original casing during replacement
        highlighted_review = highlighted_review.replace(keyword, keyword.upper())
    highlighted_reviews.append(highlighted_review)
  return highlighted_reviews

# Example usage

highlighted_reviews = highlight_keywords(reviews, keywords)

for review in highlighted_reviews:
  print(review)


# # Task 2: Sentiment Tally
# # Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.
def sentiment_tally(review, positive_words, negative_words):
  positive_count = 0
  negative_count = 0
  # Split the review into lowercase words
  words = review.lower().split()

  # Count occurrences of positive and negative words
  for word in words:
    if word in positive_words:
      positive_count += 1
    elif word in negative_words:
      negative_count += 1

  # Return the sentiment counts
  return {"positive": positive_count, "negative": negative_count}

# Example usage
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

review = "This great product is very good good , but the poor bad customer service was awful."

sentiment_counts = sentiment_tally(review, positive_words, negative_words)
print(sentiment_counts)  # Output: {'positive': 1, 'negative': 1}


# Task 3: Review Summary
# •	Implement a function that takes the first 30 characters of a review and appends "…" to create a summary. (Bonus) Ensure that the summary does not cut off in the middle of a word.

def create_summary(review):
    #Creates a summary of the first 30 characters of a review.
    if len(review) <= 30:
        return review
    else:
        summary = review[:30]
        last_space_index = summary.rfind(' ')
        if last_space_index != -1:
            summary = summary[:last_space_index]
        return summary + "…"

# Example usage
reviews = [
    "This product.",
    "Theperformanceofthisproductisexcellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "This was a poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."]



print("\nTask 3: Review Summary")
for review in reviews:
    print(create_summary(review))

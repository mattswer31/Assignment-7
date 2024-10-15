keywords = ["good", "excellent", "bad", "poor", "average"]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def highlighter(reviews):
    new_reviews = []
    for review in reviews:
        words = []
        words += review.split(' ')
        for word in words:
            for i in range(len(keywords)):
                if keywords[i] in word.lower():
                    words[words.index(word)] = word.upper()
        new_string = " ".join(words)
        new_reviews.append(new_string)
    for review in new_reviews:
        print(review)

def tally(review):
    positive_count = 0
    negative_count = 0
    split_review = []
    split_review += review.split()
    for word in split_review:
        for i in range(len(positive_words)):
            if positive_words[i] in word.lower():
                positive_count += 1
        for i in range(len(negative_words)):
            if negative_words[i] in word.lower():
                negative_count += 1
    print(f"There are {positive_count} positive words and {negative_count} negative words in this review.")
        

def summary(review):
    summary = []
    char_count = 0
    last_word = ""
    summary += review.split()
    for word in summary:
        char_count += len(word)
        if char_count > 30:
            last_index = summary.index(word)-1
            last_word = summary[last_index]
            break
    while True:
        if summary[-1] != last_word:
            summary.pop(-1)
        else:
            break
    review_summary = " ".join(summary) + "..."
    print(review_summary)
    
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
highlighter(reviews)
for review in reviews:
    tally(review)
for review in reviews:
    summary(review)

import re

# Sample text
text = "My email is test@example.com and my phone is +1-123-456-7890. Call me!"

# 1. Match: Checks if the pattern matches from the start of the string
match_result = re.match(r"My email is (\S+)", text)
if match_result:
    print("[1]. Match:", match_result.group())

# 2. Search: Finds the first occurrence
search_result = re.search(r"\+1-\d{3}-\d{3}-\d{4}", text)
if search_result:
    print("[2]. Search:", search_result.group())

# 3. Findall: Finds all occurrences
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("[3]. Findall (Emails):", emails)

# 4. Finditer: Returns an iterator with match objects
for match in re.finditer(r"\d{3}", text):
    print(f"[4]. Finditer Match at {match.start()}-{match.end()}: {match.group()}")

# 5. Substitution: Replaces patterns
replaced_text = re.sub(r"\+1-\d{3}-\d{3}-\d{4}", "[REDACTED PHONE]", text)
print("[5]. Substituted:", replaced_text)

# 6. Splitting: Splits text based on regex
split_result = re.split(r"\s+", text)  # Split by whitespace
print("[6]. Split Result:", split_result)

# 7. Precompiling regex
email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
compiled_result = email_pattern.findall(text)
print("[7]. Compiled Regex Findall:", compiled_result)

# 8. Grouping and Capturing
phone_pattern = re.search(r"(\+\d+)-(\d{3})-(\d{3})-(\d{4})", text)
if phone_pattern:
    print("[8]. Captured Groups:", phone_pattern.groups())

# 9. Lookaheads and Lookbehinds
lookahead_match = re.findall(r"\b\w+(?= is)", text)  # Words before "is"
lookbehind_match = re.findall(r"(?<=email is )\S+", text)  # Words after "email is"
print("[9]. Lookahead Matches:", lookahead_match)
print("[10]. Lookbehind Matches:", lookbehind_match)

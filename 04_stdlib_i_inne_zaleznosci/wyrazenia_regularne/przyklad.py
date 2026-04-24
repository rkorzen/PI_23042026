import re


text = "123 123456789 123456 456789123 1234563"
PHONE_PATTERN = r"\d{9}"

pattern = re.compile(PHONE_PATTERN)

print(pattern.findall(text))

print(re.findall(PHONE_PATTERN, text))
print(re.match(PHONE_PATTERN, "123456789"))




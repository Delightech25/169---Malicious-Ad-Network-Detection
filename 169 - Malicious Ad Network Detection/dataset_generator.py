import pandas as pd
import random

malicious_urls = [
    "http://free-money.xyz",
    "http://secure-paypal-alert.com",
    "http://update-bank-info.net",
    "http://malware-downloads.ru",
    "http://click-and-win-prize.com",
    "http://login-facebook-security.net"
]

safe_urls = [
    "https://google.com",
    "https://amazon.in",
    "https://github.com",
    "https://stackoverflow.com",
    "https://wikipedia.org",
    "https://microsoft.com"
]

data = []

# Generate more samples randomly
for _ in range(200):
    url = random.choice(malicious_urls)
    data.append([url, 1])

for _ in range(200):
    url = random.choice(safe_urls)
    data.append([url, 0])

df = pd.DataFrame(data, columns=["url", "label"])
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("dataset.csv", index=False)

print("dataset.csv generated successfully!")
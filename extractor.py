import re
from urllib.parse import urlparse
from models.classifier import classify_text
import string
import nltk
from nltk.corpus import stopwords
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
STOPWORDS = set(stopwords.words("english"))

def extract_links(description):
    return re.findall(r'https?://[^\s]+', description)


def extract_promo_codes(description):
    patterns = [
        r"(?:code|coupon|promo)\s*[:\-]?\s*([A-Z0-9]{4,20})",  # e.g. code: SAVE20
        r"use\s+([A-Z0-9]{4,20})\s+(?:to|get)\s+(?:discount|offer)",  # e.g. use TECH10 to get discount
        r"apply\s+code\s+([A-Z0-9]{4,20})",  # e.g. apply code WELCOME25
    ]

    description = description.upper()  # Promo codes are usually all caps

    codes=[]
    for pattern in patterns:
        matches = re.findall(pattern, description)
        codes.extend(matches)

    codes = [code for code in codes if code.lower() not in STOPWORDS]

    return list(set(codes))

# def is_promo_link(link):
#     promo_keywords = ["amzn.to", "walmart.com", "aff", "ref", "discount", "deal", "promo", "coupon", "track", "click", "rstyle", "partner", "shop"]
#     bad_keywords = ["instagram", "twitter", "facebook", "tiktok", "youtube", "subscribe", "follow", "patreon", "paypal"]
#
#     return any(k in link.lower() for k in promo_keywords) and not any(b in link.lower() for b in bad_keywords)

def is_promo_link(link):
    link = link.lower()
    parsed = urlparse(link)

    promo_keywords = [
        "amzn.to", "rstyle.me", "bit.ly", "aff", "ref", "deal", "promo", "click", "shop", "go", "track", "offer", "outbound"
    ]

    known_social_domains = [
        "instagram.com", "facebook.com", "twitter.com", "tiktok.com", "youtube.com", "linkedin.com", "patreon.com", "paypal.com"
    ]

    # Include if it has a promo keyword in domain or path
    has_promo_hint = any(k in link for k in promo_keywords)

    # Exclude if domain is a known social platform
    is_social = any(soc in parsed.netloc for soc in known_social_domains)

    # Allow custom domains like mysite.com/deal or shop.mychannel.io
    is_custom_redirect = not is_social and len(parsed.netloc.split(".")) >= 2 and parsed.path.count("/") >= 1

    return (has_promo_hint or is_custom_redirect) and not is_social

def extract_and_classify(description):
    links = list(set(extract_links(description)))
    codes = extract_promo_codes(description)
    filtered_links = [l for l in links if is_promo_link(l)]
    # Classify links
    classified_links = [{"link": l, "type": classify_text(l)} for l in filtered_links]

    return {
        "links": classified_links,
        "promo_codes": list(set(codes))
    }

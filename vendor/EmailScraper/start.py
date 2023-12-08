# -*- coding: utf-8 -*-
from tldextract import extract
from collections import Counter
import subprocess
import json

def main():
    
    print("=== WELCOME TO EMAILSCRAPER FROM GMBOT ===")
    print("About EmailScraper from GMBot: https://github.com/thomasgottvalles/GMBot")
    
    # Opens the file generated by GMBot's Selenium.
    with open("../../output/all.json",'r+') as json_file:
        json_data = json.load(json_file)
        for element in json_data:
            
            # Checks data in the file.
            print("Checking if website exists at: " + element["title"])
            if element["website"] is not None:
                website = extract(element["website"])
                domain = website.registered_domain
                if not "emails_extracted" in element and not "contact_email" in element:

                    # Extracts emails on the website.
                    print("Website found! Starting the bot and scraping emails at: " + domain)
                    command = "scrapy crawl emailscraper -a domain=" + domain + " -o " + domain + ".json"
                    subprocess.run(command, shell=True)

                    # Counts emails and selects the most relevant contact email.
                    json_file_website = open(domain + ".json")
                    json_data_website = json.load(json_file_website)
                    link_internal = []
                    text_internal = []
                    link_external = []
                    text_external = []
                    for i in json_data_website:
                        link_internal += i["emails"]["link_internal"]
                        text_internal += i["emails"]["text_internal"]
                        link_external += i["emails"]["link_external"]
                        text_external += i["emails"]["text_external"]

                    print("Emails extrated from " + domain + ".json")
                    print("Domain: internal - Type: link : " + str(Counter(link_internal).most_common()))
                    print("Domain: internal - Type: text : " + str(Counter(text_internal).most_common()))
                    print("Domain: external - Type: link : " + str(Counter(link_external).most_common()))
                    print("Domain: external - Type: text : " + str(Counter(text_external).most_common()))

                    emails_extracted = [
                        {"domain_internal_type_link": None if not link_internal else dict(Counter(link_internal).most_common())},
                        {"domain_internal_type_text": None if not text_internal else dict(Counter(text_internal).most_common())},
                        {"domain_external_type_link": None if not link_external else dict(Counter(link_external).most_common())},
                        {"domain_external_type_text": None if not text_external else dict(Counter(text_external).most_common())}
                    ]

                    print("Contact email selected:")
                    if Counter(link_internal).most_common():
                        contact_email = Counter(link_internal).most_common()[0][0]
                    elif Counter(text_internal).most_common():
                        contact_email = Counter(text_internal).most_common()[0][0]
                    elif Counter(link_external).most_common():
                        contact_email = Counter(link_external).most_common()[0][0]
                    elif Counter(text_external).most_common():
                        contact_email = Counter(text_external).most_common()[0][0]
                    else:
                        contact_email = None
                    print(contact_email)

                    # Updates the file.
                    element['emails_extracted'] = emails_extracted
                    element['contact_email'] = contact_email
                    json_file.seek(0)
                    json.dump(json_data,json_file, indent = 4)
                    
                else:
                    print("\"emails_extracted\" and \"contact_email\" already exist at: " + domain)
            else:
                print("No website found at: " + element["title"])
                
            
if __name__ == "__main__":
    main()
# <p align="center">GMBot</p>

🌟 Get 120 Leads in 2.5 Minutes!

This Python program is a bot designed to explore establishments on Google Maps, extract data from each establishment and store it for later use in a JSON and CSV file. Added value of the fork: the establishments websites are then explored with Scrapy in order to extract and store email addresses.

In versions before the commits September 4, 2023 of the original repository (Google Maps Scraper) that I forked, it is not possible to extract email addresses. This is why I developed an extension (Scrapy) to extract email addresses on establishment websites. For this to work, it is important to define `website` in the `select` key or all fields (Default) in the specific fields of the configuration file. Read more in "How to select specific Fields?" for more details.

For those who don't know Scrapy, it's a Python framework that allows you to extract data from the web : 

## 🌟 Overview

Welcome to the GMBot, a powerful scraper designed to scrape up to 1200 Google Map Leads in just 25 minutes. Its Top Features are:

1. Scrapes **1200** Google Map Leads in just **25** minutes giving you lots of prospects to make potential sales.
2. Scrapes **30** Data Points including website, phone, category, owner, geo-coordinates, and **26** more data points. Even the ones that are not publicly shown in Google Maps, so you have all the data you need.
3. You can sort, select and filter the leads to get you the leads relevant to your Business.
4. You can scrape multiple queries in one go.
5. Scrapes Data in Real Time, so you have the latest data.
6. Saves Data as both JSON and CSV for easy usage.

The Table below shows the most important data points that will be generated in both CSV and JSON formats:

|title                |rating|number_of_reviews|address                                                                                                                    |website                                                                                 |phone      |img_link                                                                                       |link                                                                                                                                                                                                                 |main_category      |place_id                   |categories                                                                                                        |
|---------------------|------|-----------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|---------------------------|------------------------------------------------------------------------------------------------------------------|
|Tamasha              |4.1   |12483            |In Anand House, A 28, KG Marg, Connaught Place, New Delhi, Delhi 110001                                                    |https://website-tamasha-restaurant.business.site/?utm_source=gmb&utm_medium=referral    |9999477661 |https://lh5.googleusercontent.com/p/AF1QipOFfAmtHyXBBWAAPqL8ifQSgDW98xOGa7_WYpmA=w426-h240-k-no|https://www.google.com/maps/place/Tamasha/data=!4m7!3m6!1s0x390cfd369e6964e7:0x304898e2f2d5e7a1!8m2!3d28.6298016!4d77.2218419!16s%2Fg%2F11cmr16zjb!19sChIJ52Rpnjb9DDkRoefV8uKYSDA?authuser=0&hl=en&rclk=1            |Restaurant         |ChIJ52Rpnjb9DDkRoefV8uKYSDA|Restaurant, Bar, Continental restaurant, Italian restaurant, North Indian Restaurant                              |
|Indian Accent        |4.7   |8152             |The Lodhi, Lodhi Rd, CGO Complex, Pragati Vihar, New Delhi, Delhi 110003                                                   |https://indianaccent.com/newdelhi                                                       |1166175151 |https://lh5.googleusercontent.com/p/AF1QipMRaSvBkBK3ipKoWei-gn3IEW-2NBRwVLS-CuR-=w627-h240-k-no|https://www.google.com/maps/place/Indian+Accent/data=!4m7!3m6!1s0x390cfd309eebed77:0xfd133b52e7612c26!8m2!3d28.5918336!4d77.2382224!16s%2Fg%2F11c561vl9w!19sChIJd-3rnjD9DDkRJixh51I7E_0?authuser=0&hl=en&rclk=1      |Restaurant         |ChIJd-3rnjD9DDkRJixh51I7E_0|Restaurant, Asian restaurant, Bar, European restaurant, Fine dining restaurant, Indian restaurant                 |
|Olive Bar & Kitchen  |4.6   |6528             |Mile 6, One Style, 8, Kalka Das Marg, Seth Sarai, Mehrauli, New Delhi, Delhi 110030                                        |http://www.olivebarandkitchen.com/                                                      |9910457373 |https://lh5.googleusercontent.com/p/AF1QipNv1aHvISiSOPyM0tECLKe5-ND_N5s-p6ZTeKMv=w408-h306-k-no|https://www.google.com/maps/place/Olive+Bar+%26+Kitchen/data=!4m7!3m6!1s0x390ce2f15b20d0fd:0xaaa8607911b1bdf!8m2!3d28.5257701!4d77.1841311!16s%2Fg%2F1q64qjzb6!19sChIJ_dAgW_HiDDkR3xsbkQeGqgo?authuser=0&hl=en&rclk=1|European restaurant|ChIJ_dAgW_HiDDkR3xsbkQeGqgo|European restaurant, Bar, Cafe, Fine dining restaurant, Italian restaurant, Mediterranean restaurant, Restaurant  |
|Kiyan                |4.7   |639              |NH-8, Samalkha, New Delhi, Delhi 110037                                                                                    |http://www.roseatehotels.com/newdelhi/theroseate/dine/kiyan/                            |1130158676 |https://lh5.googleusercontent.com/p/AF1QipM_HsL2Xojc7nHdzW14rV2Cv3joGalRODYx2fZF=w408-h278-k-no|https://www.google.com/maps/place/Kiyan/data=!4m7!3m6!1s0x390d1c07eff4422b:0x8abf827be567fe7e!8m2!3d28.531523!4d77.103096!16s%2Fg%2F1pwfbhfv9!19sChIJK0L07wccDTkRfv5n5XuCv4o?authuser=0&hl=en&rclk=1                 |Fine dining restaurant|ChIJK0L07wccDTkRfv5n5XuCv4o|Fine dining restaurant, Breakfast restaurant, Continental restaurant, European restaurant, Mughlai Restaurant, North Indian Restaurant, Thai restaurant|
|Thyme Restaurant - The Umrao|4.5   |555              |National Highway 8, Rajokri Rd, D Block, Samalkha, Pushpanjali Farms, New Delhi, Delhi 110037                              |https://theumrao.com/dining                                                             |1147707050 |https://lh5.googleusercontent.com/p/AF1QipPhEscYrXx_m8po3qEbaeA54iOslEhRA2CXgP_Y=w408-h247-k-no|https://www.google.com/maps/place/Thyme+Restaurant+-+The+Umrao/data=!4m7!3m6!1s0x390d1bfec9e42687:0x14d497d545bba4b!8m2!3d28.525558!4d77.098439!16s%2Fg%2F11b5wq57rd!19sChIJhybkyf4bDTkRS7pbVH1JTQE?authuser=0&hl=en&rclk=1|Fine dining restaurant|ChIJhybkyf4bDTkRS7pbVH1JTQE|Fine dining restaurant, Breakfast restaurant, Chinese restaurant, Continental restaurant                          |

## 🛠️ Installation and execution
To work, this fork requires Python 3 and Scrapy 2.

To install Python 3, go to the [official Python documentation](https://docs.python.org/fr/3/using/index.html).  To install Pip, also go to the [official Pip documentation](https://pip.pypa.io/en/stable/installation/). Since Python 3.4, it is included by default with the Python installer. Next in your console: 
```
pip install Scrapy
```

Next, let's get started by generating Google Maps Leads by following these simple steps.

Clone the Magic :
```
git clone https://github.com/thomasgottvalles/GMBot
cd GMbot
```

Install Dependencies :
```
python -m pip install -r requirements.txt
```

Let the Rain of Google Map Leads Begin :
```
python main.py
```

Once the scraping process is complete, you can find your leads in the `output` directory. 

![Google Maps Data Scraper CSV Result](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/gmap_result.png)

## 🤔 FAQs

### The scraper is only retrieving 5 results. How can I scrape all Google Maps search results?
A: Open the file `src/config.py` and comment out the line that sets the `max_results` parameter. 

By doing so, you can scrape all the search results from Google Maps. For example, to scrape all restaurants in Delhi, modify the code as follows:
```
queries = [
    {
        "keyword": "restaurants in delhi",
        # "max_results" : 5,
    },
]
```
Note: You will be able to scrape up to 120 leads per search due to Google's scrolling limitation. 

### I want to scrape search results for a specific search query. How can I achieve that?
A: Open the file `src/config.py` and update the `keyword` with your desired search query. 

For example, if you want to scrape data about stupas in Kathmandu 🇳🇵, modify the code as follows:
```
queries = [
    {
        "keyword": "stupas in kathmandu",
    },
]
```

### How can I filter google map search results?

A: You have the option to apply filters to your Google Maps search results using the following parameters:

1. min_rating
2. min_reviews
3. max_reviews
4. has_phone
5. has_website

To specify filters, open `src/config.py` and specify your filters. 

The Following example will scrape only those listings with a minimum of 5 reviews, a maximum of 100 reviews, and a phone number.

```
queries = [
    {
        "keyword": "restaurants in delhi",
        "min_reviews": 5 ,
        "max_reviews": 100,
        "has_phone": True,
    },
]
```

### How to sort by reviews, rating, or title?

To sort your results by reviews, rating, or title, follow these steps:

Open the file `src/config.py` and set the `sort` key. 

For example, to sort by reviews in descending order, modify the code as follows:

```
queries = [
    {
        "keyword": "stupas in kathmandu",
        "sort": {
            "by": "reviews",
            "order": "desc",
        },
    },
]
```

You can sort by any field, such as `reviews`, `main_category`, `title`, `rating`, or any other field. Here are some common sort examples:

1. Sort by `reviews` count in descending order:
```
        "sort": {
            "by": "reviews",
            "order": "desc",
        },
```

2. Sort by `main_category` in ascending order:
```
        "sort": {
            "by": "main_category",
            "order": "asc",
        },
```

3. Sort by `title` in ascending order:
```
        "sort": {
            "by": "title",
            "order": "asc",
        },
```

4. Sort by `rating` in descending order:
```
        "sort": {
            "by": "rating",
            "order": "desc",
        },
```

### How to select specific Fields?
If you want to select specific fields to be output in your CSV and JSON files, you can do so by following these steps:

1.  Open `src/config.py`.
2.  Modify the `select` key to include the fields you want to select.

For example, if you want to select "title", "link", "main_category", "rating", "reviews", "website", "phone", and "address", you should adjust the code as follows:

```
queries = [
    {
        "keyword": "stupas in kathmandu",
        "select": ["title", "link", "main_category", "rating", "reviews",  "website", "phone" , "address"],
    },
]
```

You are free to select any field. Here are a couple of common field selections:

1. Standard field selection:
```
        "select": ["title", "link", "main_category", "rating", "reviews",  "website", "phone" , "address"],
```

2. Selection of all fields (Default):
```
        "select": "ALL",
```

### How to increase the speed of the Scraper?

To boost the scraping speed, the scraper launches multiple browsers simultaneously. Here's how you can increase the speed furthur:

- Adjust the `number_of_scrapers` variable in the configuration file. Recommended values are:
  - Standard laptop: 4 or 8
  - Powerful laptop: 12 or 16

Note: Avoid setting `number_of_scrapers` above 16, as Google Maps typically returns only 120 results. Using more than 16 scrapers may lead to a longer time spent on launching the scrapers than on scraping the places. Hence, it is best to stick to 4, 8, 12, or 16.

In case you encounter any issues, like the scraper crashing due to low-end PC specifications, follow these recommendations:

- Reduce the `number_of_scrapers` by 4 points.
- Ensure you have sufficient storage (at least 4 GB) available, as running multiple browser instances consumes storage space.
- Close other applications on your computer to free up memory.

Additionally, consider improving your internet speed to further enhance the scraping process.

### Can I scrape more than one query using this script?
A: Absolutely! Open `src/config.py` and add as many queries as you like. 

For example, if you want to scrape restaurants in both Delhi 😎 and Bangalore 👨‍💻, use the following code:
```
queries = [
    {
        "keyword": "restaurants in delhi",
    },
    {
        "keyword": "restaurants in bangalore",
    }
]
```

### How to scrape emails and social links like Twitter and Facebook of Shop Owners?

Google Maps does not display the emails and social links of shop owners. However, it does show the owner's Google profile, which we scrape and store in the `owner` field as shown below:

```
        "owner": {
            "id": "102395794819517641473",
            "link": "https://www.google.com/maps/contrib/102395794819517641473",
            "name": "38 Barracks Restaurant and Bar (Owner)"
        },
```

To obtain the shop owner's emails and social links, you have two options:

1. Visit the website of each shop and manually find the contact details.
2. define `website` in the `select` key or all fields (Default) in the specific fields of the configuration file. Read more in "How to select specific Fields?" for more details. 

If you are using the GMBot for prospecting and selling your products or services, it is recommended to manually visit the first 100 lead's websites. This will provide you with a better understanding of your prospects. Also, the task of finding contact details from 100 websites, can be done within 2 hours if you work with focus and speed.

### How much time does it take to scrape "n" searches?

On average, each Google Maps search gives 120 listings. It takes approximately 2.5 minutes to scrape these 120 listings.

To calculate the number of **hours** it takes to scrape "n" searches, you can **google search** this formula substituting `n` with number of searches you want to conduct:

`n * 2.5 minutes`

For example, if you want to scrape 10 google map queries or 1200 listings, it will take around 25m.

![](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/search-time.png)

### How can I utilize the data obtained from Google Maps?
A: Most people scrape Google Maps Listings to sell things!

For example, you can search for restaurants in Amritsar and pitch your web development services to them.

You can also find real estate listings in Delhi and promote your exceptional real estate software.

Google Maps is seriously a great platform to find B2B customers to sell things to!


## 🍰 Contribution
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Contact me for any contribution request.

## 📝 Licence
GMBot is Open Source software distributed under a single license: [MIT License](https://opensource.org/license/mit). As such, GMBot can freely be **used, analyzed, modified and redistributed** under the MIT License.

## 🧑 Author
Thomas Gottvalles at 
[Tesseract IT - L'agence 100% WEB ](https://tesseract-it.com)

## 🏄 Have fun
"Si vous voulez que quelque chose soit bien fait, faites-le vous-même"
"If you want something done right, do it yourself"
        Napoléon Bonaparte.
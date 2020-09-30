# Inshorts News API 

This API is capable of fetching news contents from various sources as gathered by Inshorts app and website.


### Show some :heart: and :star: the repo to support the project
---
## News Categories

This API supports category wise news. Here is a complete list of all categories.

| Sl. No.  | Category | Endpoints |
| --- | --- | --- |
| 1 | All | /all | 
| 2 | Automobile | /automobile |
| 3 | Business | /business | 
| 4 | Entertainment | /entertainment | 
| 5 | National | /national | 
| 6 | Politics | /politics | 
| 7 | Science | /science | 
| 8 | Sports | /sports | 
| 9 | Startups | /startup |
| 10 | Technology | /technology | 
| 11 | World | /world | 

---
## Installation

Refer to requirements.txt file for all the packages needed.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python packages.

```bash
pip install package_name
```

---

## Usage

Make a get request specifying the category of news you want
```
https://inshorts-news.vercel.app/{category_name}
```
Example - https://inshorts-news.vercel.app/science

---

## Response Format

The response JSON Object looks something like this - 

```JSON
{
  "category": "technology",
  "count-articles":24,
  "data": [
    {
      "author":"Nandini Sinha",
      "decription":"The UAE has become the first Gulf Arab country to establish diplomatic relations with Israel in a \"historic deal\" brokered by US President Donald Trump. Under the deal, Israel will suspend its annexation of the occupied West Bank to focus on improving relations with the Arab and Muslim world, a joint statement by the US, UAE and Israel read.",
      "images":"https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2020/08_aug/13_thu/img_1597332122442_79.jpg?",
      "inshorts-link":"https://inshorts.com/en/news/israel-to-suspend-annexation-of-west-bank-establish-diplomatic-ties-with-uae-1597334118265",
      "read-more":"https://www.rt.com/news/497940-israel-uae-deal-trump-palestine/amp/?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
      "time":"09:25 pm on 13 Aug",
      "title":"Israel to suspend annexation of West Bank, establish diplomatic ties with UAE"
    },
    ],
}
```
---
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


### Show some :heart: and :star: the repo in case you liked it :)

### © [kehsihba19](https://bit.ly/kehsihba19)

# Inshorts News API [Unofficial]
---
This API is capable of fetching news contents from various sources as gathered by Inshorts app.

---
### Show some :heart: and :star: the repo to support the project
---

## News Categories

This API supports category wise news. Here is a complete list of all categories.

1. all
2. national //Indian News only
3. business
4. sports
5. world
6. politics
7. technology
8. startup
9. entertainment
10. miscellaneous
11. science
12. automobile

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

#### Star the Repo in case you liked it :)

# © [kehsihba19](https://bit.ly/kehsihba19)

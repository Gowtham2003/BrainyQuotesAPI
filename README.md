# BrainyQuotesAPI

Unofficial Brainy Quotes API using Python , Flask , BeautifulSoup4

---

An Unofficial Brainy Quotes API Which Fetches Quotes from Brainy Quotes .

---

## Support My Project If You Like 

[![GitHub stars](https://img.shields.io/github/stars/gowtham2003/brainyquotesapi.svg?style=social&label=Star)](https://github.com/gowtham2003/brainyquotesapi)


![GitHub followers](https://img.shields.io/github/followers/gowtham2003.svg?style=social&label=Follow)


---

---
## Usage

Make a get request specifying the category of quote you want
```
https://brainyquotes.herokuapp.com/news?category={category_name}
```
Example - https://brainyquotes.herokuapp.com/news?category=nature

---
## Response Format 

Example Of Brainy Quote API Response Below 

--- 

```JSON

"data": [
    {
      "author": "By Frederick Douglass", 
      "authorlink": "https://www.brainyquote.com//authors/frederick-douglass-quotes", 
      "quote": "It is not light that we need, but fire; it is not the gentle shower, but thunder. We need the storm, the whirlwind, and the earthquake.", 
      "quotelink": "https://www.brainyquote.com//quotes/frederick_douglass_134570?src=t_nature", 
      "tags": [
        "Light", 
        "Fire", 
        "Storm", 
        "Thunder"
      ]
    }, 
    {
      "author": "By Henry David Thoreau", 
      "authorlink": "https://www.brainyquote.com//authors/henry-david-thoreau-quotes", 
      "quote": "Nature will bear the closest inspection. She invites us to lay our eye level with her smallest leaf, and take an insect view of its plain.", 
      "quotelink": "https://www.brainyquote.com//quotes/henry_david_thoreau_106919?src=t_nature", 
      "tags": [
        "Leaf", 
        "View", 
        "Will", 
        "Insect"
      ]
    }
    ],
     "success": true
}


```
---
## Setup

Install all dependencies listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python app.py
    ```
---
---

### You can fork the repo and deploy on VPS or deploy it on Heroku :)  
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Gowtham2003/BrainyQuotesAPI/tree/master)

---

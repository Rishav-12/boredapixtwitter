# boredapixtwitter

This is a Twitter bot integrated with https://boredapi.com.

## Installation

- Clone the repo
- Run

```bash
pip install requests
pip install tweepy
```

## Description

This bot pulls a random activity from The Bored API and posts to Twitter automatically.

Here's the account https://twitter.com/@new_to6/

## Usage

- Create a developer account on twitter

- Get all the tokens from the app dashboard
    - Find a detailed guide here : https://docs.tweepy.org/en/stable/examples.html

- Create a `secrets.json` file in the root of the repo and paste the following code

```json
{
    "consumer_key": "YOUR_CONSUMER_KEY",
    "consumer_secret": "YOUR_CONSUMER_SECRET",
    "access_token": "YOUR_ACCESS_TOKEN",
    "access_token_secret": "YOUR_ACCESS_TOKEN_SECRET"
}
```
Make sure to put them in correctly. Also ensure that your app has write access to your twitter account. You can always look up the official documentation for more help.

## License
[MIT](https://choosealicense.com/licenses/mit/)

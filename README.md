<div align="center">
    <img src="https://cdn3.iconfinder.com/data/icons/digital-marketing-27/64/Computer-notebook-laptop-website-click-banner-web-512.png" alt="logo" height="196">
</div>

# rrfortune

![pytest](https://github.com/zehengl/rrfortune/workflows/pytest/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A RenRen fortune collector

## Why

Believe it or not, my wife is still obsessed with the login streak on [RenRen](http://renren.com/).
She will be unhappy if I forget to login and collect RenRen fortune.
Most of the time, let alone when you travel, it's hard to remember.
So I have to improvise.

## Solution

- Consider logging in and clicking the button a UI test
- Have GitHub Actions run a daily build to trigger that test

## Prerequisites

Assuming you have access the following services

- A RenRen account
- A GitHub account
- A Rollbar account (lazy error tracking)

## Setup

### Rollbar

1. Create a new project
2. Markdown the project access token with `post_server_item` scope

### GitHub

1. Fork this repo
2. Set the environment variables on `Settings > Secrets > Repository secrets`
   - rollbar: Rollbar project access token
   - email: RenRen email
   - password: RenRen password

All set!

## Develop

Export credentials

    export email="..."
    export password="..."
    export rollbar="..."

Run test

    cd rrfortune
    python -m venv venv
    source venv/bin/activate
    pip install -U pip
    pip install -r requirements-dev.txt
    seleniumbase install chromedriver
    pytest --headless

<hr>

<sup>

## Credits

- [Icon][1] by [Eucalyp Studio][2]

</sup>

[1]: https://www.iconfinder.com/icons/2992651/banner_click_computer_laptop_notebook_web_website_icon
[2]: https://www.iconfinder.com/ratch0013

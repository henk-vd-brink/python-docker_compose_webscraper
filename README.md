## About the project

This repository contains a multi-container application to scrape cars from https://marktplaats.nl. It makes use of a proxy in conjunction with Tor to anonymously scrape data from the aforementioned website. Every time the bot blocker blocks the used IP, the scraper switches IP to evade the block.

The data is pushed into a local PostgreSQL database via an REST-ful API.

## Getting Started

### Prerequisites
- Docker

### Installation
```
git clone https://github.com/henk-vd-brink/docker-compose-webscraper.git
cd docker-compose-webscraper
```

### Run
```
docker-compose up --build
```

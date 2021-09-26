import os


class Config:
    NEWS_API_KEY ='f4de1ca5f663456ea8bae142093fb813'
    NEWS_API_BASE_URI ='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_ARTICLE_API_URL ='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey='

    




class DevConfig:

    DEBUG =True


    config_option ={
        'development':DevConfig




    }



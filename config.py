import os


class Config:
    NEWS_API_BASE_URI ='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_ARTICLE_API_URL ='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey='

    




class DevConfig(Config):

    DEBUG =True


    config_option ={
        'development':DevConfig
    }



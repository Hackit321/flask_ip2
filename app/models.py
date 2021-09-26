class Articles :

    '''
    Articles class to define articles object
    '''
    def __init__(self,source,author,title,description,url,urlToImage,publishedAt):

        self.source =source
        self.author = author
        self.title = title
        self.description =description
        self.url = url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


class Sources:

    '''
    soucrces class that defines each source object
    '''

    def __init__(self,id,name,description,url,category,language,country):

        self.name = name
        self.id = id 
        self.description = description
        self.url = url
        self.category = category
        self.country = country
    

        

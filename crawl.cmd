scrapy crawl index -a category=new -o new.csv 
scrapy crawl index -a category=applications -o applications.csv 
scrapy crawl index -a category=movies -o movies.csv 
scrapy crawl index -a category=tv -o tv.csv 
scrapy crawl index -a category=anime -o anime.csv 
scrapy crawl index -a category=xxx -o xxx.csv 
scrapy crawl index -a category=games -o games.csv 
scrapy crawl index -a category=music -o music.csv 
scrapy crawl index -a category=other -o other.csv 
rem 2>>err.txt

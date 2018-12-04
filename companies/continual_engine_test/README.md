# Scrap the top 3 website results

* Get the top 3 google search links for "Types of earthquake". 
* scrape the top website result.
* Highlight the query words in the result. 

## Requirements:

* BeautifulSoup
* google

## Steps:

* create the virtualenv

	```mkvirtualenv continual_engine```

* Install the requirements
	
	```pip install -r requirements.txt```

* Run this application:

	```python scrapy.py "Types of earthquake"```

* Output to a file.

	```python scrapy.py "Types of earthquake" >> output.text```

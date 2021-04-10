# dataminingchallenge

Before starting coding, I started of inspecting the requests from <a href="http://www.zalora.com.my/women/shoes/?from=header&occasion=Casual&brand=aldo">this</a> link. Where I came across <a href="https://www.zalora.com.my/_c/v1/lite/list_products?limit=40&catalogtype=Main&lang=en&country_iso=my&url=%2Fshoes%2Faldo%2F&offset=0&dir=desc&express_shipping=false&membership_program=true&name_search=false&enable_visual_sort=true&auto_correct=true&enable_similar_term=true&is_brunei=false&brand=87&category_id=164&occasion=Casual">this</a> URL from where the data was being fetched. 



From the URL, I ran some experiments with "limit" and "offset" parameters. I found out that I can go till limit 400 in a single request. In the data, I found out the I can fetch number of products found from the query which helped me in computed number of pages beforehand. In this case, it was 2 pages since the number of products were 418 with respect to limit 400.

Finally, I also inspected <a href="https://www.zalora.com.my/robots.txt">robots.txt file</a>. Where I looked for blocked pages and specially the crawl-delay which was not found therefore, I didn't applied any delay notion in my code.

I tested my code in docker using the following commands (this include getting the output to host machine rather than the container itself):<br/>
<strong>
docker build -t zalora_scraping . <br/> <br/>
docker run --rm -it -v %cd%:/code/ zalora_scraping
</strong><br/><br/>
To run this project simply execute the following command:<br/><br/>
<strong>docker-compose up</strong>

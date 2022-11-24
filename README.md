# FacebookWebCrawler
The FacebookWebCrawler would automatically find the urls with specific conditoins, and store the urls into txt file.

**The version only for Chinese language.**

## Overview
The process of the FacebookWebCrawler.py
1. Search the keyword in the search bar, then click the post and choose the latest post and year.
2. The program should automatically click the "show more".
3. Store urls with specific conditions.

## The environemnt

+ Python version  ```3.10.5```
+ ChromeDriver 

## Download the ChromeDriver
**The ChromDriver version should be the same or newer than your Google Chrome**

+ First, you need to Check your Google Chrome version
  1. On your computer, open Chrome. See steps for Android or iOS.
  2. At the top right, look at More.
  3. Click Help > About Chrome.

+ Second, download the chromedriver and put into the same folder.

[Download ChromeDriver](https://chromedriver.chromium.org/downloads)

## Instasll the required package

+ Run ``` pip install -r requirements.txt``` or ```pip3 install -r requirements.txt``` to install the required packages

## Execution
+ Run ```python FacebookWebCrawler.py``` or ```python3 FacebookWebCrawler.py``` to execute the program. 

Searching for a keyword 

![image](https://user-images.githubusercontent.com/79703512/203686504-cde28c9c-a3c3-460d-a44c-eec6f4376b53.png) wholesales

The year of the article

![image](https://user-images.githubusercontent.com/79703512/203686600-e04a95b4-c5ce-42b7-aad5-3fca18f3c79a.png) 2022

The specific conditions in the urls

![image](https://user-images.githubusercontent.com/79703512/203686665-80189644-fada-4da1-85b7-357fbb384b49.png) https

Success: Successful to Click the "show more"

New URL: Find the urls that meets the criteria

![image](https://user-images.githubusercontent.com/79703512/203688466-6e5d1ae9-bbfb-4d98-b740-5fb809bee2fe.png)

![image](https://user-images.githubusercontent.com/79703512/203688958-c5d10860-911a-4482-a6b6-9f1ccbd77b0f.png)

## Follow my Socialmedia

[LinkedIn](https://www.linkedin.com/in/mingyi-huang/)

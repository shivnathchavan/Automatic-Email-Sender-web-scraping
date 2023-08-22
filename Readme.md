### Flipkart Price Tracker

This Python script scrapes the price of a product from a Flipkart webpage and sends an email notification if the price falls below a certain threshold. It utilizes libraries like BeautifulSoup for web scraping and smtplib for sending emails.

#### Prerequisites

- Python 3.x
- Required libraries: `numpy`, `pandas`, `re`, `smtplib`, `beautifulsoup4`

#### Usage

1. Clone this repository or download the script directly.

2. Install the required libraries if you haven't already:

   ```bash
   pip install numpy pandas requests beautifulsoup4
   ```


3. Open the script flipkart_price_tracker.py in a text editor.

4. Update the following sections in the script with your information:

5. Update the url variable with the Flipkart product URL you want to track.

6. Update the title dictionary with your user agent information.

In the send_mail function:

1. Set up your SMTP server information (e.g., Gmail SMTP).

2. Replace 'your_email@gmail.com' with your Gmail email address.

3. Replace 'your_generated_app_password' with an App Password generated from your Google Account.

4. Adjust the price threshold in the checkprice function as desired.

Run the script:

```bash
python flipkart_price_tracker.py 
```



The script will check the price of the product. If the price falls below the set threshold, it will send an email notification.

#### Note

Be cautious when using automated scripts for web scraping, as some websites may have terms of service that prohibit scraping. Always respect website terms and policies.
Storing passwords directly in scripts is not secure. Use environment variables or other secure methods to manage sensitive information.

#### License
This project is licensed under the MIT License - see the LICENSE file for details.
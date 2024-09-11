<mark>This project extracts real estate listings from the site [realtor.com](realtor.com) using the Hidden API method.<mark>

## Description:

* **Website:** https://www.realtor.com/realestateandhomes-search/Colorado
* **Purpose:** Extracts real estate listings in Colorodo which come under "Newest Listings" filter
* **Fields extracted:** property_id, list_price, status, permalink, branding, list_date, description.beds, description.baths_consolidated, description.sqft, description.type, description.sub_type, description.sold_price, description.sold_date, location.street_view_url, location.address, flags.is_new_listing
* **Scraping tool:** Hidden API method
* **Libraries/Methods used:** curlconvertor.com, Postman
* **Exported data:** [response_data.json](https://github.com/rohanrvpatil/realtorcom_listings/blob/main/response_data.json), [response_data.xlsx](https://github.com/rohanrvpatil/realtorcom_listings/blob/main/response_data.xlsx)
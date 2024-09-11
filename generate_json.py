# Youtube link: https://www.youtube.com/watch?v=DqtlR0y0suo

import requests
import json
import pandas as pd
import random
import time


def generate_json(offset):

    cookies = {
        'split': 'n',
        '__vst': '833de609-434a-4c0c-b91e-ce48700be9e4',
        '__ssn': '6e923513-4533-49a5-a2ed-27f4464091cb',
        '__ssnstarttime': '1725787110',
        '__bot': 'false',
        'AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg': '1',
        'G_ENABLED_IDPS': 'google',
        'mdLogger': 'false',
        'kampyle_userid': 'b73d-8715-bd09-f24e-f648-cf2d-08c5-09a0',
        'AWSALBTG': 'BOHK887FMJEvEpjzAd2HitculXA92daCYZ0eJm4qg+vjhFsqoGP3QMTPxFa0aXnbh5B0p6nBaxJ1dOseZI8C7qHdSiXGH2MOTuo4fWoRoeQaE3gg3lQAbRVi8PzG7Ghv8dpp4gKTzdEHwMDfG1SDnuHYaK4XSMURIUvRLPKsHwO9',
        'AWSALBTGCORS': 'BOHK887FMJEvEpjzAd2HitculXA92daCYZ0eJm4qg+vjhFsqoGP3QMTPxFa0aXnbh5B0p6nBaxJ1dOseZI8C7qHdSiXGH2MOTuo4fWoRoeQaE3gg3lQAbRVi8PzG7Ghv8dpp4gKTzdEHwMDfG1SDnuHYaK4XSMURIUvRLPKsHwO9',
        'AWSALB': 'WpHa+MCovmmi6f8JDJ5jgG5MmDW9l6TpXwbYpIE+hzxC2ZBxrOj42KZ0VRnHvwh6bu6M77FjZervuPHi4WneRCy1ZaCZu2JgKREvxyOnhdG7p0zBO5czw8P5sykz',
        'AWSALBCORS': 'WpHa+MCovmmi6f8JDJ5jgG5MmDW9l6TpXwbYpIE+hzxC2ZBxrOj42KZ0VRnHvwh6bu6M77FjZervuPHi4WneRCy1ZaCZu2JgKREvxyOnhdG7p0zBO5czw8P5sykz',
        'split_tcv': '163',
        'ldp-open-houses': 'false',
        'ldp-neighborhood': 'false',
        'ldp-environmental-risk': 'false',
        'ldp-real-estimates': 'false',
        'ldp-monthly-payment': 'false',
        'ldp-connect-to-lender': 'false',
        'ldp-property-history': 'false',
        'ldp-property-details': 'false',
        'pxcts': '73273b32-6dfd-11ef-99af-cf89288e2887',
        '_pxvid': '7327300c-6dfd-11ef-99af-80eb84c17f35',
        'kampyleUserSession': '1726063635618',
        'kampyleUserSessionsCount': '15',
        'srchID': '9808a128aa63447ab48340d537a02196',
        'kampyleUserPercentile': '27.158783683976107',
        'criteria': 'sprefix%3D%252Fnewhomecommunities%26area_type%3Dstate%26pg%3D3%26state_code%3DCO%26state%3DColorado%26state_id%3DCO%26loc%3DColorado%26locSlug%3DColorado',
        'isAuth0EnabledOnGnav': 'C1',
        'AMCV_8853394255142B6A0A4C98A4%40AdobeOrg': '-1124106680%7CMCIDTS%7C19977%7CMCMID%7C56627326404917994127083688707770073365%7CMCAID%7CNONE%7CMCOPTOUT-1726073913s%7CNONE%7CvVersion%7C5.2.0',
        'kampyleSessionPageCounter': '7',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': 'split=n; __vst=833de609-434a-4c0c-b91e-ce48700be9e4; __ssn=6e923513-4533-49a5-a2ed-27f4464091cb; __ssnstarttime=1725787110; __bot=false; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; G_ENABLED_IDPS=google; mdLogger=false; kampyle_userid=b73d-8715-bd09-f24e-f648-cf2d-08c5-09a0; AWSALBTG=BOHK887FMJEvEpjzAd2HitculXA92daCYZ0eJm4qg+vjhFsqoGP3QMTPxFa0aXnbh5B0p6nBaxJ1dOseZI8C7qHdSiXGH2MOTuo4fWoRoeQaE3gg3lQAbRVi8PzG7Ghv8dpp4gKTzdEHwMDfG1SDnuHYaK4XSMURIUvRLPKsHwO9; AWSALBTGCORS=BOHK887FMJEvEpjzAd2HitculXA92daCYZ0eJm4qg+vjhFsqoGP3QMTPxFa0aXnbh5B0p6nBaxJ1dOseZI8C7qHdSiXGH2MOTuo4fWoRoeQaE3gg3lQAbRVi8PzG7Ghv8dpp4gKTzdEHwMDfG1SDnuHYaK4XSMURIUvRLPKsHwO9; AWSALB=WpHa+MCovmmi6f8JDJ5jgG5MmDW9l6TpXwbYpIE+hzxC2ZBxrOj42KZ0VRnHvwh6bu6M77FjZervuPHi4WneRCy1ZaCZu2JgKREvxyOnhdG7p0zBO5czw8P5sykz; AWSALBCORS=WpHa+MCovmmi6f8JDJ5jgG5MmDW9l6TpXwbYpIE+hzxC2ZBxrOj42KZ0VRnHvwh6bu6M77FjZervuPHi4WneRCy1ZaCZu2JgKREvxyOnhdG7p0zBO5czw8P5sykz; split_tcv=163; ldp-open-houses=false; ldp-neighborhood=false; ldp-environmental-risk=false; ldp-real-estimates=false; ldp-monthly-payment=false; ldp-connect-to-lender=false; ldp-property-history=false; ldp-property-details=false; pxcts=73273b32-6dfd-11ef-99af-cf89288e2887; _pxvid=7327300c-6dfd-11ef-99af-80eb84c17f35; kampyleUserSession=1726063635618; kampyleUserSessionsCount=15; srchID=9808a128aa63447ab48340d537a02196; kampyleUserPercentile=27.158783683976107; criteria=sprefix%3D%252Fnewhomecommunities%26area_type%3Dstate%26pg%3D3%26state_code%3DCO%26state%3DColorado%26state_id%3DCO%26loc%3DColorado%26locSlug%3DColorado; isAuth0EnabledOnGnav=C1; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C19977%7CMCMID%7C56627326404917994127083688707770073365%7CMCAID%7CNONE%7CMCOPTOUT-1726073913s%7CNONE%7CvVersion%7C5.2.0; kampyleSessionPageCounter=7',
        'origin': 'https://www.realtor.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'rdc-client-name': 'RDC_WEB_SRP_FS_PAGE',
        'rdc-client-version': '3.x.x',
        'referer': 'https://www.realtor.com/realestateandhomes-search/Colorado/sby-6/pg-4',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'ConsumerSearchQuery',
        'variables': {
            'query': {
                'primary': True,
                'status': [
                    'for_sale',
                    'ready_to_build',
                ],
                'search_location': {
                    'location': 'Colorado',
                },
            },
            'client_data': {
                'device_data': {
                    'device_type': 'desktop',
                },
            },
            'limit': 42,
            'offset': offset,
            'sort': [
                {
                    'field': 'list_date',
                    'direction': 'desc',
                },
                {
                    'field': 'photo_count',
                    'direction': 'desc',
                },
            ],
        },
        'query': 'query ConsumerSearchQuery($query: HomeSearchCriteria!, $limit: Int, $offset: Int, $search_promotion: SearchPromotionInput, $sort: [SearchAPISort], $sort_type: SearchSortType, $client_data: JSON, $bucket: SearchAPIBucket, $mortgage_params: MortgageParamsInput) {\n  home_search: home_search(\n    query: $query\n    sort: $sort\n    limit: $limit\n    offset: $offset\n    sort_type: $sort_type\n    client_data: $client_data\n    bucket: $bucket\n    search_promotion: $search_promotion\n    mortgage_params: $mortgage_params\n  ) {\n    count\n    total\n    search_promotion {\n      names\n      slots\n      promoted_properties {\n        id\n        from_other_page\n        __typename\n      }\n      __typename\n    }\n    mortgage_params {\n      interest_rate\n      __typename\n    }\n    properties: results {\n      property_id\n      list_price\n      search_promotions {\n        name\n        asset_id\n        __typename\n      }\n      primary_photo(https: true) {\n        href\n        __typename\n      }\n      rent_to_own {\n        right_to_purchase\n        rent\n        __typename\n      }\n      listing_id\n      matterport\n      virtual_tours {\n        href\n        type\n        __typename\n      }\n      status\n      products {\n        products\n        brand_name\n        __typename\n      }\n      source {\n        id\n        type\n        spec_id\n        plan_id\n        agents {\n          office_name\n          __typename\n        }\n        __typename\n      }\n      lead_attributes {\n        show_contact_an_agent\n        opcity_lead_attributes {\n          cashback_enabled\n          flip_the_market_enabled\n          __typename\n        }\n        lead_type\n        ready_connect_mortgage {\n          show_contact_a_lender\n          show_veterans_united\n          __typename\n        }\n        __typename\n      }\n      community {\n        description {\n          name\n          __typename\n        }\n        property_id\n        permalink\n        advertisers {\n          office {\n            hours\n            phones {\n              type\n              number\n              primary\n              trackable\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        promotions {\n          description\n          href\n          headline\n          __typename\n        }\n        __typename\n      }\n      permalink\n      price_reduced_amount\n      description {\n        name\n        beds\n        baths_consolidated\n        sqft\n        lot_sqft\n        baths_max\n        baths_min\n        beds_min\n        beds_max\n        sqft_min\n        sqft_max\n        type\n        sub_type\n        sold_price\n        sold_date\n        __typename\n      }\n      location {\n        street_view_url\n        address {\n          line\n          postal_code\n          state\n          state_code\n          city\n          coordinate {\n            lat\n            lon\n            __typename\n          }\n          __typename\n        }\n        county {\n          name\n          fips_code\n          __typename\n        }\n        __typename\n      }\n      open_houses {\n        start_date\n        end_date\n        __typename\n      }\n      branding {\n        type\n        name\n        photo\n        __typename\n      }\n      flags {\n        is_coming_soon\n        is_new_listing(days: 14)\n        is_price_reduced(days: 30)\n        is_foreclosure\n        is_new_construction\n        is_pending\n        is_contingent\n        __typename\n      }\n      list_date\n      photos(limit: 2, https: true) {\n        href\n        __typename\n      }\n      advertisers {\n        type\n        builder {\n          name\n          href\n          logo\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  commute_polygon: get_commute_polygon(query: $query) {\n    areas {\n      id\n      breakpoints {\n        width\n        height\n        zoom\n        __typename\n      }\n      radius\n      center {\n        lat\n        lng\n        __typename\n      }\n      __typename\n    }\n    boundary\n    __typename\n  }\n}',
    }

    response = requests.post('https://www.realtor.com/frontdoor/graphql', cookies=cookies, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"operationName":"ConsumerSearchQuery","variables":{"query":{"primary":true,"status":["for_sale","ready_to_build"],"search_location":{"location":"Colorado"}},"client_data":{"device_data":{"device_type":"desktop"}},"limit":42,"offset":126,"sort":[{"field":"list_date","direction":"desc"},{"field":"photo_count","direction":"desc"}]},"query":"query ConsumerSearchQuery($query: HomeSearchCriteria!, $limit: Int, $offset: Int, $search_promotion: SearchPromotionInput, $sort: [SearchAPISort], $sort_type: SearchSortType, $client_data: JSON, $bucket: SearchAPIBucket, $mortgage_params: MortgageParamsInput) {\\n  home_search: home_search(\\n    query: $query\\n    sort: $sort\\n    limit: $limit\\n    offset: $offset\\n    sort_type: $sort_type\\n    client_data: $client_data\\n    bucket: $bucket\\n    search_promotion: $search_promotion\\n    mortgage_params: $mortgage_params\\n  ) {\\n    count\\n    total\\n    search_promotion {\\n      names\\n      slots\\n      promoted_properties {\\n        id\\n        from_other_page\\n        __typename\\n      }\\n      __typename\\n    }\\n    mortgage_params {\\n      interest_rate\\n      __typename\\n    }\\n    properties: results {\\n      property_id\\n      list_price\\n      search_promotions {\\n        name\\n        asset_id\\n        __typename\\n      }\\n      primary_photo(https: true) {\\n        href\\n        __typename\\n      }\\n      rent_to_own {\\n        right_to_purchase\\n        rent\\n        __typename\\n      }\\n      listing_id\\n      matterport\\n      virtual_tours {\\n        href\\n        type\\n        __typename\\n      }\\n      status\\n      products {\\n        products\\n        brand_name\\n        __typename\\n      }\\n      source {\\n        id\\n        type\\n        spec_id\\n        plan_id\\n        agents {\\n          office_name\\n          __typename\\n        }\\n        __typename\\n      }\\n      lead_attributes {\\n        show_contact_an_agent\\n        opcity_lead_attributes {\\n          cashback_enabled\\n          flip_the_market_enabled\\n          __typename\\n        }\\n        lead_type\\n        ready_connect_mortgage {\\n          show_contact_a_lender\\n          show_veterans_united\\n          __typename\\n        }\\n        __typename\\n      }\\n      community {\\n        description {\\n          name\\n          __typename\\n        }\\n        property_id\\n        permalink\\n        advertisers {\\n          office {\\n            hours\\n            phones {\\n              type\\n              number\\n              primary\\n              trackable\\n              __typename\\n            }\\n            __typename\\n          }\\n          __typename\\n        }\\n        promotions {\\n          description\\n          href\\n          headline\\n          __typename\\n        }\\n        __typename\\n      }\\n      permalink\\n      price_reduced_amount\\n      description {\\n        name\\n        beds\\n        baths_consolidated\\n        sqft\\n        lot_sqft\\n        baths_max\\n        baths_min\\n        beds_min\\n        beds_max\\n        sqft_min\\n        sqft_max\\n        type\\n        sub_type\\n        sold_price\\n        sold_date\\n        __typename\\n      }\\n      location {\\n        street_view_url\\n        address {\\n          line\\n          postal_code\\n          state\\n          state_code\\n          city\\n          coordinate {\\n            lat\\n            lon\\n            __typename\\n          }\\n          __typename\\n        }\\n        county {\\n          name\\n          fips_code\\n          __typename\\n        }\\n        __typename\\n      }\\n      open_houses {\\n        start_date\\n        end_date\\n        __typename\\n      }\\n      branding {\\n        type\\n        name\\n        photo\\n        __typename\\n      }\\n      flags {\\n        is_coming_soon\\n        is_new_listing(days: 14)\\n        is_price_reduced(days: 30)\\n        is_foreclosure\\n        is_new_construction\\n        is_pending\\n        is_contingent\\n        __typename\\n      }\\n      list_date\\n      photos(limit: 2, https: true) {\\n        href\\n        __typename\\n      }\\n      advertisers {\\n        type\\n        builder {\\n          name\\n          href\\n          logo\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n  commute_polygon: get_commute_polygon(query: $query) {\\n    areas {\\n      id\\n      breakpoints {\\n        width\\n        height\\n        zoom\\n        __typename\\n      }\\n      radius\\n      center {\\n        lat\\n        lng\\n        __typename\\n      }\\n      __typename\\n    }\\n    boundary\\n    __typename\\n  }\\n}"}'
    #response = requests.post('https://www.realtor.com/frontdoor/graphql', cookies=cookies, headers=headers, data=data)
    
    for product in response.json()['data']['home_search']['properties']:
        filtered_product = {
            'property_id': product.get('property_id'),
            'list_price': product.get('list_price'),
            'status': product.get('status'),
            'permalink': product.get('permalink'),
            'description': {
                'beds': product.get('description', {}).get('beds'),
                'baths_consolidated': product.get('description', {}).get('baths_consolidated'),
                'sqft': product.get('description', {}).get('sqft'),
                'type': product.get('description', {}).get('type'),
                'sub_type': product.get('description', {}).get('sub_type'),
                'sold_price': product.get('description', {}).get('sold_price'),
                'sold_date': product.get('description', {}).get('sold_date')
            },
            'location': {
                'street_view_url': product.get('location', {}).get('street_view_url'),
                'address': product.get('location', {}).get('address', {}).get('line')
            },
            'branding': [b.get('name') for b in product.get('branding', [])],
            'flags': {
                'is_new_listing': product.get('flags', {}).get('is_new_listing')
            },
            'list_date': product.get('list_date')
        }
        yield filtered_product
    
    
#['data']['home_search']['properties']
#51220 homes
#256 requests to be sent

results=[]

for offset in range(0,210,42):
    for product in generate_json(offset):
        results.append(product)
    print(f"{offset+42}/210 properties extracted.")
    time.sleep(random.uniform(30,50))


with open("./response_data.json", "w") as f:
    json.dump(results, f)
    

with open('./response_data.json', 'r') as json_file:
    json_data = json.load(json_file)

df = pd.json_normalize(json_data)
df.to_excel('./response_data.xlsx', index=False)



"""
if response.status_code == 200:
    data = response.json()

    with open('response_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("Data saved to 'response_data.json'")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
"""


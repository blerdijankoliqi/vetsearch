from django.shortcuts import render
from django.http import HttpResponse
from wagtail.core.models import Page
from .models import LocalityPage
from django.core.exceptions import ObjectDoesNotExist

import json
import requests

def convert_json(self):
    
    response_API = requests.get('https://api-development.petleo.de/v1/localities/')
    data = response_API.text
    parse_json = json.loads(data)

    converted = []
    id = 1
    for item in parse_json:
        converted.append({
            "id": id,
            "id_from_api": item["id"],
            "city": item["city"],
            "postal_code": item["postal_code"],
            "country_code": item["country_code"],
            "lat": item["lat"],
            "lng": item["lng"],
            "google_places_id": item["google_places_id"]
        })
        id += 1
        for sub_locality in item["sub_localities"]:
            converted.append({
                "id": id,
                "id_from_api": item["id"],
                "city": sub_locality,
                "postal_code": item["postal_code"],
                "country_code": item["country_code"],
                "lat": item["lat"],
                "lng": item["lng"],
                "google_places_id": item["google_places_id"]
            })
            id += 1



    # Works
    for page in converted:
        
        ind = 0
        try:
            page = Page.objects.get(title=page['city'])
            ind=1

        except ObjectDoesNotExist:
            ind=2

        if ind==2:
            parent_page = Page.objects.get(title='Localities')
            print(parent_page.slug)
            locality_page = LocalityPage(
                title=page['city'],
                id_from_api=page['id_from_api'],
                city=page['city'],
                postal_code=page['postal_code'],
                country_code=page['country_code'],
                lat=page['lat'],
                lng=page['lng'],
                google_places_id=page['google_places_id'],
                search_description="Looking for reliable and affordable pet care in " + page['city'] + "? Check out our list of local veterinarians, providing everything from preventative medicine to surgical services. Find the right vet for your pet today.",
                seo_title=page['city'] + " Veterinarians Near You | Find Affordable Pet Care"
            )
            parent_page.add_child(instance=locality_page)
            locality_page.save()            
    
    return HttpResponse("adding")


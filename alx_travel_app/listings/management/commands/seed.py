import uuid
import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing

User = get_user_model()

LOCATIONS = [
    "Dar es Salaam, Tanzania",
    "Arusha, Tanzania",
    "Zanzibar, Tanzania",
    "Nairobi, Kenya",
    "Cape Town, South Africa",
]

NAMES = [
    "Ocean View Bungalow",
    "Mountain Retreat Cabin",
    "Urban Studio Apartment",
    "Luxury Beachfront Villa",
    "Safari Lodge Suite",
]

DESCRIPTIONS = [
    "A lovely place to stay with an amazing view of the ocean.",
    "Perfect for a quiet getaway surrounded by nature.",
    "Located in the heart of the city, close to all attractions.",
    "Premium amenities and stunning views. Ideal for vacation.",
    "Experience the wild from the comfort of luxury living.",
]


class Command(BaseCommand):
    help = 'Seed the database with sample listings data.'

    def handle(self, *args, **kwargs):
        host_users = User.objects.filter(is_staff=True)[:5]
        if not host_users:
            self.stdout.write(self.style.WARNING('No host users (is_staff=True) found. Please create at least one.'))
            return

        created_count = 0

        for i in range(10):
            listing = Listing.objects.create(
                property_id=uuid.uuid4(),
                host=random.choice(host_users),
                name=random.choice(NAMES),
                description=random.choice(DESCRIPTIONS),
                location=random.choice(LOCATIONS),
                pricepernight=random.uniform(30.00, 250.00),
            )
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} listings.'))

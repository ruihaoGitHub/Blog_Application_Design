import os
import django
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')
django.setup()

from django.contrib.auth.models import User
from blogs.models import BlogPost

def create_data():
    print("Starting data generation...")

    # 1. Get Superuser (Admin)
    # Assuming the first user is the superuser you created
    admin_user = User.objects.filter(is_superuser=True).first()
    if not admin_user:
        print("Error: No superuser found. Please create one first.")
        return
    print(f"Found Admin user: {admin_user.username}")

    # 2. Create a New User
    new_username = 'alice'
    new_user, created = User.objects.get_or_create(username=new_username)
    if created:
        new_user.set_password('password123')
        new_user.save()
        print(f"Created new user: {new_username} (password: password123)")
    else:
        print(f"User {new_username} already exists.")

    # 3. Define the 4 posts content
    posts_data = [
        {
            "title": "My Vibrant Campus Life",
            "text": "Life at Shenzhen University is full of energy! From early morning library sessions to late-night coding marathons, every day brings something new. The lychee trees are blooming, and the campus looks more beautiful than ever. I joined the AI club yesterday and met so many like-minded friends.",
            "owner": admin_user
        },
        {
            "title": "Reflections on Work-Life Balance",
            "text": "Transitioning from student to professional is challenging. In the tech industry, things move fast. It's important to find time for yourself. I've started jogging around the park every evening to clear my mind. Coding is a passion, but health is a priority.",
            "owner": admin_user
        },
        {
            "title": "Adventures in Study Abroad",
            "text": "Studying abroad has been an eye-opening experience. The cultural exchange, the different academic approaches, and the challenge of living independently have helped me grow so much. I miss the food back home, but I'm learning to cook local dishes!",
            "owner": new_user
        },
        {
            "title": "Frontiers of Technology: AI & Future",
            "text": "The latest developments in Generative AI are mind-blowing. Large Language Models are changing how we code, write, and create. It's not just about automation; it's about augmentation. We are standing at the precipice of a new technological revolution.",
            "owner": new_user
        }
    ]

    # 4. Update existing posts or Create new ones
    # We will delete all existing posts to ensure a clean slate for this specific request
    # giving you exactly the 4 posts you wanted.
    print("Clearing existing posts to ensure correct topics...")
    BlogPost.objects.all().delete()

    for post_data in posts_data:
        BlogPost.objects.create(
            title=post_data['title'],
            text=post_data['text'],
            owner=post_data['owner']
        )
        print(f"Created post: '{post_data['title']}' for user {post_data['owner'].username}")

    print("\nDone! Please refresh your browser.")

if __name__ == '__main__':
    create_data()

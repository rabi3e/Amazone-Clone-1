#for Django seting
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django 
django.setup()

# import Faker
from faker import Faker
import random
from product.models import Product , Brand , ProductImages , ProductReview
from django.contrib.auth.models import User
def seed_Brand(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg']
    for  x in range(n):
        Brand.objects.create(
            nom = fake.name(),
            image = f"brand/{images[random.randint(1,12)]}",
        )
    print(f'{n} Brand Seeded')


def seed_product(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    flags = ['N','V','P']
    tagss = ['test1','test2','test3','test4','test']
    for x in range(n):
        Product.objects.filter(id=x+1).update(
            flag = flags[random.randint(0,2)]
        )
        print(Product.nom)
        print(x)
    print(f'{n} Products Seeded')
    
def seed_product_images(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    for x in range(n): 
        ProductImages.objects.create(
            product = Product.objects.get(id=n) , 
            image = f"productimages/{images[random.randint(0,12)]}" ,    
        )
      
    print(f'{n} Products Images Seeded')
    
    
def seed_product_reviews(n):
    fake = Faker()
    rattt = [1,2,3,4,5]
    for x in range(n): 
        ProductReview.objects.create(
            user = User.objects.get(id=1),
            product = Product.objects.get(id=x+1) , 
            rate = rattt[random.randint(0,4)],
            review = fake.text(),  
        )
        print (x)
      
    print(f'{n} Products Images Seeded')
#seed_Brand(120)
seed_product(5010)
#seed_product_images(10000)
#seed_product_reviews(5009)


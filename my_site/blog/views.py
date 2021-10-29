from django.shortcuts import render
from datetime import date


posts = [
    {
        'slug': 'today-i-ate-a-cake',
        'image': 'rainbow-cake.jpg',
        'author': 'Vampira',
        'date': date(2021, 10, 28),
        'title': 'Today I ate a cake',
        'content': '''
            One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed 
            in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little 
            he could see his brown belly, slightly domed and divided by arches into stiff sections. 
            The bedding was hardly able to cover it and seemed ready to slide off any moment. His many legs, 
            pitifully thin compared with the size of the rest of him, waved about helplessly as he looked. 
            "What's happened to me?" he thought. It wasn't a dream. His room, a proper human room although a 
            little too small, lay peacefully between its four familiar walls. A collection of textile samples 
            lay spread out on the table - Samsa was a travelling salesman - and above it there hung a picture 
            that he had recently cut out of an illustrated magazine and housed in a nice, gilded frame. 
            It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff 
            that covered the whole of her lower arm towards the viewer. Gregor then turned to look out the 
            window at the dull weather.
            ''',
        'excerpt': 'One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin.'
    },
    {
        'slug': 'i-saw-a-kitten',
        'image': 'kitten.jpg',
        'author': 'Vampira',
        'date': date(2021, 7, 1),
        'title': 'I saw a kitten',
        'content': '''
            One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed 
            in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little 
            he could see his brown belly, slightly domed and divided by arches into stiff sections. 
            The bedding was hardly able to cover it and seemed ready to slide off any moment. His many legs, 
            pitifully thin compared with the size of the rest of him, waved about helplessly as he looked. 
            "What's happened to me?" he thought. It wasn't a dream. His room, a proper human room although a 
            little too small, lay peacefully between its four familiar walls. A collection of textile samples 
            lay spread out on the table - Samsa was a travelling salesman - and above it there hung a picture 
            that he had recently cut out of an illustrated magazine and housed in a nice, gilded frame. 
            It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff 
            that covered the whole of her lower arm towards the viewer. Gregor then turned to look out the 
            window at the dull weather.
            ''',
        'excerpt': 'One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin.'
    },
    {
        'slug': 'places-in-los-angeles',
        'image': 'los-angeles.jpg',
        'author': 'Vampira',
        'date': date(2020, 12, 8),
        'title': 'Places in Los Angeles',
        'content': '''
            One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed 
            in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little 
            he could see his brown belly, slightly domed and divided by arches into stiff sections. 
            The bedding was hardly able to cover it and seemed ready to slide off any moment. His many legs, 
            pitifully thin compared with the size of the rest of him, waved about helplessly as he looked. 
            "What's happened to me?" he thought. It wasn't a dream. His room, a proper human room although a 
            little too small, lay peacefully between its four familiar walls. A collection of textile samples 
            lay spread out on the table - Samsa was a travelling salesman - and above it there hung a picture 
            that he had recently cut out of an illustrated magazine and housed in a nice, gilded frame. 
            It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff 
            that covered the whole of her lower arm towards the viewer. Gregor then turned to look out the 
            window at the dull weather.
            ''',
        'excerpt': 'One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin.'
    },
    {
        'slug': 'my-special-ramen-recipe',
        'image': 'ramen.jpg',
        'author': 'Vampira',
        'date': date(2018, 1, 1),
        'title': 'My special ramen recipe',
        'content': '''
            One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed 
            in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little 
            he could see his brown belly, slightly domed and divided by arches into stiff sections. 
            The bedding was hardly able to cover it and seemed ready to slide off any moment. His many legs, 
            pitifully thin compared with the size of the rest of him, waved about helplessly as he looked. 
            "What's happened to me?" he thought. It wasn't a dream. His room, a proper human room although a 
            little too small, lay peacefully between its four familiar walls. A collection of textile samples 
            lay spread out on the table - Samsa was a travelling salesman - and above it there hung a picture 
            that he had recently cut out of an illustrated magazine and housed in a nice, gilded frame. 
            It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff 
            that covered the whole of her lower arm towards the viewer. Gregor then turned to look out the 
            window at the dull weather.
            ''',
        'excerpt': 'One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin.'
    }
]


def get_date(post):
    return post.get('date')


def index(request):
    sorted_posts = sorted(posts, key=get_date, reverse=True)
    latest_posts = sorted_posts[:3]
    return render(request, 'blog/index.html', {'latest_posts': latest_posts})


def all_posts(request):
    sorted_posts = sorted(posts, key=get_date, reverse=True)
    return render(request, 'blog/all-posts.html', {'all_posts': sorted_posts})
    

def single_post(request, slug):
    post = next(post for post in posts if post['slug'] == slug)
    return render(request, 'blog/single-post.html', {'post': post})

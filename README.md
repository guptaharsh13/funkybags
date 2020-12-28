In this E-Commerce project, I have made use of Celery, and I have optimized the way in which we usually send emails using Django. Once any user signs in to the website, and clicks on BUY NOW button -
I send an E-mail to the user's email id with the help of an Asynchronous task, using Celery. I have also handeled the case, when a user is not signed in, but he tries to buy an item form the website.
Also, there is more to the website, like forgot password, etc.
In the limited time that was alloted, I was only able to build this much of the project, but there is so much more to it, in which it could be extended.

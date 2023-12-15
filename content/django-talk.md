Title: DjangoCon 2023 Slides & Resources
Date: 2023-10-17
Author: James Walters
Category: Python
Tags: Django, deployment, DjangoCon, portfolio

It's such a delight to give a talk at this year's DjangoCon! This is my first tech conference, as well as my first time presenting. I'd love to thank [Will Vincent](https://fosstodon.org/@wsvincent), [Eric Matthes](https://fosstodon.org/@ehmatthes), and [Alyssa Nicholl](https://twitter.com/AlyssaNicoll) for all their help reviewing and refining this talk to be the best it could be. I also want to thank my good friend and colleague [Sam Crabtree](https://fosstodon.org/@CrashBandit1990), without whose influence I wouldn't have learned Python and Django in the first place. 💚️ After the conference is over, I'll take some time to reflect on everything and post about it here, so keep an eye 👀️ out for that! 

In the meantime, below are links to any resources I mentioned:

### Links to the Talk

- Link to [my slides on Google Docs](https://docs.google.com/presentation/d/1sIJ2NwSQD36IEj10bl1nX0z_Tf6Gfu62Z-vAyqSfKEc/edit?usp=sharing). The presenter notes contain a complete transcript of everything I said.
- Here's the [video of the talk](https://youtu.be/t-wsiW5mkgA)!

### Static Files

- Django Documentation - [How to manage static files](https://docs.djangoproject.com/en/stable/howto/static-files/)
- [Whitenoise with Django Documentation](https://whitenoise.readthedocs.io/en/latest/django.html)
- [Assets in Django Without Losing Your Hair](https://www.youtube.com/watch?v=E613X3RBegI), talk by Jacob Kaplan-Moss at PyCon 2019
- RealPython, [Serving Static Files Directly with nginx](https://realpython.com/django-nginx-gunicorn/#serving-static-files-directly-with-nginx)

### Database
- Django Documentation - [Databases (API Reference)](https://docs.djangoproject.com/en/4.2/ref/databases/)
- Django Documentation - [`DATABASE` Settings](https://docs.djangoproject.com/en/latest/ref/settings/#databases)
- Fly.io, [How SQLite Scales Read Concurrency](https://fly.io/blog/sqlite-internals-wal/)
- [Datasette](https://datasette.io/)

### WSGI

- Django Documentation - [How to deploy with WSGI](https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/)
- [WSGI for Web Developers](https://www.youtube.com/watch?v=WqrCnVAkLIo), talk by Ryan Wilson-Perkin at PyConCA 2018

### Web Servers

- Django Documentation - [How to use Django with Apache and mod_wsgi](https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/modwsgi/)
- RealPython, [Securely Deploy a Django App With Gunicorn, Nginx, & HTTPS](https://realpython.com/django-nginx-gunicorn/)

### Deployment Tools

- Django Documentation - [Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [django-simple-deploy](https://django-simple-deploy.readthedocs.io/en/latest/)
- [django-production](https://github.com/lincolnloop/django-production)

### Additional Resources

- Here's the [blog post]({filename}/django-deployment.md) from which this talk was adapted.
- Here's the [2023 Wagtail Developer Survery](https://wagtail.org/blog/2023-wagtail-deployment-survey/) I mentioned
- [Django Systemd Crashcourse](https://vsupalov.com/django-systemd-crashcourse/) 

<footer id="footer" style="font-weight: bold; text-align: center;">
Found this helpful or informative? <a href="https://ko-fi.com/iamjameswalters">Buy me a coffee!</a> ☕️
</footer>
<script>
    let now = new Date; 
    let oct31 = new Date('2023-10-31'); 
    if (now < oct31) {
      document.getElementById('footer').style.display = 'none';
    }
</script>
Title: PyOhio 2024 Slides & Resources
Date: 2024-07-27
Author: James Walters
Category: Python
Tags: Django, deployment, PyOhio, portfolio

Man, I love PyOhio! Last year was my first one, and I was so thrilled to hear that this year's event was going to be in person for the first time since COVID. I absolutely wanted to be a part of it, and I'm so glad I got to be! Thanks to _you_ for listening to my talk! I hope it served you and helped you understand the deployment process for a Python web app a little better.

Below are links to any resources I mentioned, and a few that I didn't:

### Links to the Talk

- Link to [my slides on Google Docs](https://docs.google.com/presentation/d/1sIJ2NwSQD36IEj10bl1nX0z_Tf6Gfu62Z-vAyqSfKEc/edit?usp=sharing). The presenter notes contain a complete transcript of everything I said.

### Static Files

- Django Documentation - [How to manage static files](https://docs.djangoproject.com/en/stable/howto/static-files/)
- [Whitenoise with Django Documentation](https://whitenoise.readthedocs.io/en/latest/django.html)
- [Assets in Django Without Losing Your Hair](https://www.youtube.com/watch?v=E613X3RBegI), talk by Jacob Kaplan-Moss at PyCon 2019
- RealPython, [Serving Static Files Directly with nginx](https://realpython.com/django-nginx-gunicorn/#serving-static-files-directly-with-nginx)

### Database
- Django Documentation - [Databases (API Reference)](https://docs.djangoproject.com/en/4.2/ref/databases/)
- Django Documentation - [`DATABASE` Settings](https://docs.djangoproject.com/en/latest/ref/settings/#databases)
- [Use SQLite in production](https://www.youtube.com/watch?v=yTicYJDT1zE), talk by Tom Dyson at DjangoCon Europe 2023
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

### Docker

- [Django, Docker and Postgres Tutorial - LearnDjango.com](https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial)

### Additional Resources

- Here's the [blog post]({filename}/django-deployment.md) from which this talk was adapted.
- Here's the [2023 Wagtail Developer Survey](https://wagtail.org/blog/2023-wagtail-deployment-survey/) I mentioned
- [Django Systemd Crashcourse](https://vsupalov.com/django-systemd-crashcourse/) 

<footer id="footer" style="font-weight: bold; text-align: center;">
Found this helpful or informative? <a href="https://ko-fi.com/iamjameswalters">Buy me a coffee!</a> ☕️
</footer>
<script>
    let now = new Date; 
    let month_after = new Date('2024-8-27'); 
    if (now < month_after) {
      document.getElementById('footer').style.display = 'none';
    }
</script>

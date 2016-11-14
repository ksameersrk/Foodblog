+Hierarchy:
> manage.py - start webserver for the framework
> settings.py - manage website settings
> urls.py - patterns to redirect to pages
> wsgi.py -

+About Django:
> Has its own webserver and site is easy to manage with different files for
settings and url resolution.
> Databsase modeled as object instead of writing boring programming seq.
> Different funtionalities developed as independent apps and is then used by
central site.
> OO approach - different tables modelled as tables with different columns as
attributes and functions to perform operations upon these columns.
> Integrates with well-known sqlite3
> URL redirected to function in views.py
> Views get requests, processes it and redirects it to template, connects models
and templates.
> templates folder - where requests are redirected after being returned from
views funcrtions.
> Queryset - list of objects of given model i.e data form DB
> {{Django var name}} - template tags to display Django model objects
> {% for i in obj %} {{i.columnname}} {% endfor %} - Django for loop in template
where i is one Django object representing one datarow
> {% load staticfiles %} - to load static files
> href="{% static 'css/blog.css' %}" - link to files in static folder
> Django forms - Creating model objects via code and not Django admin ineterface
> Rendering of forms and saving a form done in same view.
> Type of inputs areof various kind

+Commands:
> python manage.py migrate - to create database
> python manage.py runserver - to start server
> python manage.py startproject 'project name' - to start a new project
> python manage.py startapp 'app name' - to start a new app
> python manage.py makemigrations 'installed app name' - to commit model to DB
> python manage.py migrate 'installed app name' - to push model to DB
> provides admin interface to manage models in DB rather than complex seq. of
code.
> python manage.py createsuperuser - to create login for Django-login
> admin.site.register(Post) - register model in admin.py
> python manage.py shell - to enter interactive query mode
> 'modelname'.objects.all() - print all objects of model in interactive mode
> 'modelname'.objects.create(author=me, title='Sample title', text='Test') - creating
new object i.e database entry
> 'modelname'.objects.filter('columname' some condition) - to filter objects
returned
>
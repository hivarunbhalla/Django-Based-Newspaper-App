# Django-Based-Newspaper-App
A Django-based newspaper application with user authentication and article management.

## Project Structure
![image](https://github.com/hivarunbhalla/Django-Based-Newspaper-App/assets/106589945/bff41ce8-ec9d-43db-9d70-16bbdefc124f)


## Features

- User authentication (login, signup, password reset)
- Article management (create, read, update, delete)
- Custom user accounts
- Responsive design using Bootstrap 5
- Crispy forms for improved form rendering

## Dependencies

This project uses the following main dependencies:

- Django
- crispy-forms
- crispy-bootstrap5

The full list of installed apps:

```python
INSTALLED_APPS = [
    'django.contrib.auth',  
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd Party
    "crispy_forms", 
    "crispy_bootstrap5", 

    # Custom Apps
    'accounts',
    'pages',
    "articles",
]
```
## Configuration
The project uses several custom configurations, which can be found in settings.py:
Custom User Model
The project uses a custom user model:

```python
AUTH_USER_MODEL = "accounts.CustomUser"
```
This allows for easy extension of the user model if needed.

## Crispy Forms
Crispy Forms is configured to use Bootstrap 5:
```python
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

##Email Backend
The project is currently configured to use the console for email backend:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This means that emails sent by the application (such as password reset emails) will be printed to the console rather than actually sent.
For production use, you should configure a proper email backend. The project includes a commented-out configuration for using SendGrid:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```
Remember to never commit sensitive information like email passwords to version control. Use environment variables or a separate settings file for production configurations.

## Authentication Redirects
The login and logout redirect URLs are set to the home page:
```python
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
```

# URL Structure
## Main URLs (urls.py)
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path("articles/", include("articles.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("pages.urls"))
]
```z

## Accounts URLs (accounts/urls.py)
```python
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
```

## Articles URLs (articles/urls.py).
```python
urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/comment', CommentPost.as_view(), name='comment_post'),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]
```

## Pages URLs (pages/urls.py)
```python
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
```

# Setup

1. Clone the repository
  Create a virtual environment:```python -m venv venv```<br />
  Activate the virtual environment:<br />
        a. Windows: ```venv\Scripts\activate```<br />
        b. macOS/Linux: ```source venv/bin/activate```<br />

2. Install dependencies: 
```pip install -r requirements.txt```<br />
Run migrations: ```python manage.py migrate```<br />
Create a superuser: ```python manage.py createsuperuser```<br />
Run the development server: ```python manage.py runserver```<br />

## Usage
Navigate to ```http://localhost:8000``` in your web browser to access the application.

Home page: ```/```<br />
Article list: ```/articles/```<br />
Create new article: ```/articles/new/```<br />
Article detail: ```/articles/<id>/```<br />
Edit article: ```/articles/<id>/edit/```<br />
Delete article: ```/articles/<id>/delete/```<br />
Sign up: ```/accounts/signup/```<br />
Log in: ```/accounts/login/```<br />
Log out: ```/accounts/logout/```<br />

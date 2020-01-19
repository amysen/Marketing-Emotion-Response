# this defines the url for static files
# eg: base-url.com/static/your-js-file.js
STATIC_URL = '/static/'

# this is directory paths where you have to put your project level static files
# you can put multiple folders here
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
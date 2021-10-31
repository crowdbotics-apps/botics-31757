from home.models import App, Plan


def app_exists(data, user):
    """
    Check app with name for user exists
    """
    name = data.get('name', None)
    app_exists = App.objects.filter(name=name, user=user).exists()
    return app_exists

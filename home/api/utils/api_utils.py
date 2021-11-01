from home.models import App, Plan, Subscription


def app_exists(data, user, id=None):
    """
    Check app with name for user exists
    """
    name = data.get('name', None)
    app_exists = App.objects.filter(name=name, user=user).exclude(pk=id).exists()
    return app_exists

def sub_exists(data, user):
    """
    Check user has active subscription for app exists
    """
    app = data.get('app', None)
    active = data.get('active', None)
    sub_exists = Subscription.objects.filter(
        app=app,
        active=active,
        user=user
    ).exists()
    return sub_exists

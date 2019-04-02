from django_google_auth.models import DjangoGoogleAuthenticator2



# from django_google_auth.google.deletegoogleauth.deletegoogleauth import delete_google_auth

def delete_google_auth(user):
    """
    删除google令牌
    :param user: 邮箱
    :return: None
    """

    DjangoGoogleAuthenticator2.objects.filter(
        username=user
    ).delete()



    return None
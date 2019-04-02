from django_google_auth.models import DjangoGoogleAuthenticator2
import base64,codecs,random,re
from django_google_auth.utils.googletotp import googletotp





# from django_google_auth.google.bindgoogleauth.bindgoogleauth import bind_google_auth

def bind_google_auth(user):
    """
    绑定google令牌
    :param user:  用户邮箱
    :return: google令牌二维码
    """

    queryset_user = DjangoGoogleAuthenticator2.objects.filter(
        username=user
    )

    if queryset_user.exists():
        return {
            "success":False,
            "data":"{}用户已经绑定google令牌,不能二次绑定".format(user)
        }

    base_32_secret = \
        base64.b32encode(
            codecs.decode(codecs.encode(
                '{0:020x}'.format(random.getrandbits(80))
            ), 'hex_codec'))

    totp_obj = googletotp.TOTP(base_32_secret.decode("utf-8"))
    qr_code = re.sub(r'=+$', '', totp_obj.provisioning_uri(user))
    key = str(base_32_secret, encoding="utf-8")
    DjangoGoogleAuthenticator2.objects.create(
        username=user,
        key=key,
    )

    return {
        "success":True,
        "data":qr_code
    }


from django_google_auth.models import DjangoGoogleAuthenticator2
import pyotp







def check_google_auth(user,code):
    """
    验证google令牌
    :param user: 邮箱
    :param code: 客服端动态码
    :return: True/False
    """

    queryset_user = DjangoGoogleAuthenticator2.objects.filter(
        username=user
    )

    if not queryset_user.exists():
        return "{}用户未绑定google令牌".format(user)

    obj_user = queryset_user.first()
    key = obj_user.key # 用户秘钥

    t = pyotp.TOTP(key)
    result = t.verify(code)  # 对输入验证码进行校验，正确返回True
    res = result if result is True else False

    return res

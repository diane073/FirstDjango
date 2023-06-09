from django.db import models
from user.models import UserModel
from django.core.validators import MinValueValidator

# Create your models here.


class ProductModel(models.Model):
    class Meta:
        db_table = "product_data"

    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
    code = models.AutoField(primary_key=True)  # 자동으로 번호를 부여하는 필드
    name = models.CharField(max_length=150)
    user = models.ForeignKey(
        UserModel, on_delete=models.RESTRICT, null=True, blank=True)
    description = models.CharField(max_length=150)
    price = models.IntegerField(default=0, validators=[
                                MinValueValidator(1000)], help_text="1000 이상의 값을 입력하세요.")
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    """
    choices 매개변수는 Django 모델 필드에서 사용하는 매개변수 중 하나로
    해당 필드에서 선택 가능한 옵션을 지정하는 역할을 합니다.
    변수를 통해 튜플 리스트를 받으면 첫번째 요소는 실제 DB에 저장되는 값이 되고,
    두번째 요소는 사용자가 볼 수 있는 레이블(옵션의 이름)이 됩니다.
    """

    def __str__(self):  # 문자열 반환해야하는데 튜플형태로 반환함
        return self.name


class Inbound(models.Model):
    """
    입고 모델입니다.
    상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
    """
    pass

# model


class Outbound(models.Model):
    """
    출고 모델입니다.
    상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
    """
    pass

    # def save(self, *args, **kwargs):
    #     pass


# model
class Invetory(models.Model):
    """
    창고의 제품과 수량 정보를 담는 모델입니다.
    상품, 수량 필드를 작성합니다.
    작성한 Product 모델을 OneToOne 관계로 작성합시다.
    """
    pass

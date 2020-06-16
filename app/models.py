from django.db import models

from users.models import User



class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """
    # 施設名
    F_name = models.CharField(
        verbose_name='施設名',
        max_length=20,
        blank=True,
        null=True,
    )

    # 入力者氏名
    I_name = models.ForeignKey(
        User,
        verbose_name='入力者氏名',
        max_length=20,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    # サンプル項目2 メモ
    memo = models.TextField(
        verbose_name='備考',
        blank=True,
        null=True,
    )

    # サンプル項目3 整数
    quontity = models.IntegerField(
        verbose_name='何kgほしいか',
        blank=True,
        null=True,
    )

    # サンプル項目7 日付
    deadline = models.DateField(
        verbose_name='いつほしいか',
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（固定）
    vege_choice = (
        (1, '人参'),
        (2, '大根'),
        (3, 'じゃがいも'),
        (4, 'キャベツ'),
        (5, 'ホウレンソウ'),
        (6, 'ピーマン'),
        (7, 'なんでもいい'),
    )

    vegetable = models.IntegerField(
        verbose_name='ほしい野菜',
        choices=vege_choice,
        blank=True,
        null=True,
    )
        # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='C_CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='C_UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.sample_1

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'


class F_Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # 出品者
    I_name = models.ForeignKey(
        User,
        verbose_name='出品者',
        max_length=20,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        editable=False,
    )

    # サンプル項目2 メモ
    memo = models.TextField(
        verbose_name='備考',
        blank=True,
        null=True,
    )

    # サンプル項目3 整数
    quontity = models.IntegerField(
        verbose_name='何kg出そうか',
        blank=True,
        null=True,
    )

    quontity_left = models.IntegerField(
        verbose_name='在庫',
        blank=True,
        null=True,
    )

    price = models.IntegerField(
        verbose_name='価格',
        blank=True,
        null=True,
    )

    # サンプル項目7 日付
    deadline = models.DateField(
        verbose_name='いつ出そうか',
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（固定）
    vege_choice = (
        (1, '人参'),
        (2, '大根'),
        (3, 'じゃがいも'),
        (4, 'キャベツ'),
        (5, 'ホウレンソウ'),
        (6, 'ピーマン'),
        (7, 'なにかしら'),
    )

    vegetable = models.IntegerField(
        verbose_name='出せる野菜',
        choices=vege_choice,
        blank=True,
        null=True,
    )

    photo = models.ImageField(
        verbose_name='写真',
        upload_to='f_items/',
        default=None,

    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='F_CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='F_UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.vege_choice[self.vegetable-1][1]

    def get_filename(self):
        return os.path.basename(self.photo.name)

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'


class Reservation(models.Model):

    subscriber = models.ForeignKey(
        User,
        verbose_name='購入者',
        blank=True,
        null=True,
        related_name='Subscriber',
        on_delete=models.SET_NULL,
        editable=False,
    )
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )
    target = models.ForeignKey(
        F_Item,
        verbose_name='商品アイテム',
        blank=True,
        null=True,
        related_name='F_Item',
        on_delete=models.SET_NULL,
        editable=False,
    )
    total_price = models.IntegerField(
        verbose_name='合計金額',
        blank=True,
        null=True,
    )
    quontity = models.IntegerField(
        verbose_name='購入数量',
        blank=True,
        null=True,
    )
    memo = models.TextField(
        verbose_name='備考',
        blank=True,
        null=True,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.subscriber

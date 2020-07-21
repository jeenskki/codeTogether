from django.db import models

#회원정보 DB

class Accounts(models.Model):
    account_id = models.AutoField('account_id', primary_key=True)
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=16)
    user_name = models.CharField(max_length=30)
    email = models.EmailField(default=None)
    user_type = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "accounts"
    
    def __str__(self):
        return self.user_id + ' / ' + self.email

class t_list(models.Model):
    table_id = models.AutoField('table_id', primary_key=True)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    field_main = models.CharField(max_length=20)
    field_sub = models.CharField(max_length=20)

    class Meta:
        db_table = 't_list'
    
    def __str__(self):
        return self.table_id + ' / ' + self.account
from django import forms

class MyForm(forms.Form):
    text = forms.CharField(max_length=100)
#とりあえず手始めに文字入力用のフィールドであるCharFieldを設定してみます．
# CharFieldは必須引数として最長文字数（max_length）を指定する必要があるので，
# とりあえず100文字を設定します．


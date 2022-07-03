<!--<!DOCTYPE html>-->
<!--<html lang="en">-->
<!--    <head>-->
<!--        <meta charset="UTF-8">-->
<!--        <title> </title>-->
<!--    </head>-->
<!--    <body>-->
<!--        <h1 class="all-info-title">All info</h1>-->
<!--        <tr>-->
<!--            <th scope="col">VERON</th>-->
<!--            <th scope="col">Ваш личный мастер</th>-->
<!--            <th scope="col">Адрес</th>-->
<!--            <th scope="col">Телефон</th>-->
<!--            <th scope="col">Как добраться</th>-->
<!--            <th scope="col">Услуги</th>-->
<!--            <th scope="col">Прайсы</th>-->
<!--            <th scope="col">Подарочный сертификат</th>-->
<!--            <th scope="col">Акции</th>-->
<!--        <tr>-->
<!--    </body>-->
<!--    {% for info in context.info %}-->
<!--        <tr>-->
<!--            <td>{{ info.name_services }}</td>-->
<!--            <td>{{ info.name_master }}</td>-->
<!--            <td>{{ info.address }}</td>-->
<!--            <td>{{ info.telephone }}</td>-->
<!--            <td>{{ info.how_to_get }}</td>-->
<!--            <td>{{ info.first_service_name }}, {{ info.second_service_name }}</td>-->
<!--            <td>{{ info.link_to_price }}</td>-->
<!--            <td>{{ info.gift_certificate }}</td>-->
<!--            <td>{{ info.stock }}</td>-->
<!--        </tr>-->
<!--    {% endfor %}-->
<!--    </body>-->
<!--</body>-->
<!--</html>-->

name_master = models.CharField(max_length=255, blank=True, null=True)
address = models.CharField(max_length=255, blank=True, null=True)
telephone = models.IntegerField(blank=True, null=True)
how_to_get = models.CharField(max_length=255, blank=True, null=True)
first_service_name = models.CharField(max_length=255, blank=True, null=True)
second_service_name = models.CharField(max_length=255, blank=True, null=True)
link_to_price = models.CharField(max_length=255, blank=True, null=True)
gift_certificate = models.CharField(max_length=255, blank=True, null=True)
stock = models.CharField(max_length=255, blank=True, null=True)

<p><h2>Брови:</h2></p>
   <p><h3>Молелирование</h3></p>
   <p><h3>Окрашивание</h3></p>
   <p><h3>Корекция</h3></p>
  <img alt='eyebrow_photo' src="https://"  width="500">
  <img alt='eyebrow_photo' src="https://"  width="500">
  <img alt='eyebrow_photo' src="https://"  width="500">
  <p><h3>Отзывы:</h3></p>
  <p>(отзывы)</p>
  <p><h3>Оставь свой отзыв:</h3></p>
  <p>(форма оставить отзыв)</p>
  <p><h2>Ресницы:</h2></p>
   <p><h3>Классика</h3></p>
   <p><h3>1,5D</h3></p>
   <p><h3>2D</h3></p>
   <p><h3>3D</h3></p>
  <img alt='eyelash_photo' src="https://"  width="500">
  <img alt='eyelash_photo' src="https://"  width="500">
  <img alt='eyelash_photo' src="https://"  width="500">
  <img alt='eyelash_photo' src="https://"  width="500">
  <p><h3>Отзывы:</h3></p>
  <p>(отзывы)</p>
  <p><h3>Оставь свой отзыв:</h3></p>
  <p>(форма оставить отзыв)</p>


<table class="book-table table table-striped table-hover">
    <thead>
    <tr>
        <th scope="col">Услуга</th>
        <th scope="col">Информация о услуге</th>
        <th scope="col">Стоимость</th>
    </tr>
    </thead>
    <tbody>
    {% for service in context.services %}
        <tr>
            <td scope="row">{{ service.name_service }} </td>
            <td>{{ service.info_service }}</td>
            <td>{{ service.price }}</td>
        </tr>
    {% endfor %}
    </tbody>
</table>
<img alt='eyebrow_photo' src="https://clipstips.ru/x/1600/606/IMG_7220.jpg"  width="200">
<img alt='eyebrow_photo' src="https://lash.ru/upload/%D0%A0%D0%BE%D0%BC%D0%B0%D0%BD%D0%BE%D0%B2%D0%B0%20%D0%9D%D0%B0%D1%82%D0%B0%D0%BB%D1%8C%D1%8F.jpg"  width="200">
<img alt='eyebrow_photo' src="https://barb.pro/uploads/images/korrekcia-brovey-brave-beauty-bar-min%5B1%5D.jpg"  width="200">
<p>  </p>
<img alt='eyelash_photo' src="https://oblaka4you.ru/thumb/2/R_s4Rd-wPH2hGZrr-VWVdQ/r/d/foto_1_narashchivanie_resnic_do_i_posle.jpg"  width="200">
<img alt='eyelash_photo' src="https://vplate.ru/images/article/orig/2020/01/narashchivanie-resnic-1-5d.jpg"  width="200">
<img alt='eyelash_photo' src="https://redsale.by/rfiles/krutolevich-si/W85921z8s29R0647l8T9N55r50HRa1-redsale_max.jpg"  width="200">
<img alt='eyelash_photo' src="https://gomel.redsale.by/rfiles/kasyan-mv/9NwQ25FR57RfRuE09hE4hL90tZLvLp-redsale_max.jpg"  width="200">
<p>  </p>
<table class="book-table table table-striped table-hover">
    <thead>
    <tr>
        <th scope="col">Отзывы:</th>
    </tr>
    </thead>
    <tbody>
    {% for review in context.reviews %}
        <tr>
            <td scope="row">{{ review.text }}</td>
        </tr>
    {% endfor %}
    </tbody>
</table>

{% endblock %}
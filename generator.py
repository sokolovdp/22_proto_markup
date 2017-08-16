from staticjinja import make_site

sample_order = {
    'time': 'Вчера, в 21:30',
    'text': '60 шт. ПК от 72-15 до ПК 21-15, Криводановка, с доставкой',
    'name': 'Алексей',
    'views': 12}

sample_comment = {
    'name': 'Кирилл',
    'age': 29,
    'city': 'Барабинск',
    'text': 'Бла бла... мне помогло, все супер! ' * 7}

index_context = {
    'user': 'Дмитрий Соколов',
    'region': 'Новосибирск и область',
    'orders': [sample_order] * 3,
    'comments': [sample_comment] * 3,
    'index_page': True}

orders_context = {
    'region': 'Новосибирск и область',
    'orders': [sample_order] * 7,
    'pages':  5,
    'index_page': False}

if __name__ == "__main__":
    site = make_site(outpath='static', contexts=[
        ('index.html', index_context),
        ('orders.html', orders_context)])
    site.render()

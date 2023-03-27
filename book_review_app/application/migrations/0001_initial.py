# Generated by Django 4.1.7 on 2023-03-27 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('followers', models.IntegerField()),
            ],
            options={
                'db_table': 'Author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cover_image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('book_title', models.CharField(max_length=255)),
                ('book_description', models.CharField(blank=True, max_length=255, null=True)),
                ('book_softcopy_link', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Books',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'Category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('feed_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('upvotes', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Feed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('offer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('offer_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'Offer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('publisher_name', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Publisher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.IntegerField(primary_key=True, serialize=False)),
                ('reviews', models.CharField(max_length=255)),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
            ],
            options={
                'db_table': 'Review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('subscription_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subscription_name', models.CharField(max_length=255, unique=True)),
                ('duration', models.IntegerField()),
                ('price', models.IntegerField()),
                ('subscribers', models.IntegerField()),
            ],
            options={
                'db_table': 'Subscriptions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('fellow_reviewers', models.IntegerField()),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthorBooks',
            fields=[
                ('author_author', models.OneToOneField(db_column='Author_author_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='application.author')),
            ],
            options={
                'db_table': 'Author_Books',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksPublisher',
            fields=[
                ('books_book', models.OneToOneField(db_column='Books_book_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='application.books')),
            ],
            options={
                'db_table': 'Books_Publisher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PublisherUser',
            fields=[
                ('publisher_publisher', models.OneToOneField(db_column='Publisher_publisher_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='application.publisher')),
            ],
            options={
                'db_table': 'Publisher_User',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserAuthor',
            fields=[
                ('user_user', models.OneToOneField(db_column='User_user_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='application.user')),
            ],
            options={
                'db_table': 'User_Author',
                'managed': False,
            },
        ),
    ]

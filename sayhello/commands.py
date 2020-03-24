import click

from sayhello import app,db
from sayhello.models import Message

@app.cli.command()
@click.option('--drop',is_flag=True,help='Crate after drop.')
def initdb(drop):
    '''Initialize the datebase.'''
    if drop:
        click.confirm('This operation will delete the database,do you want to continue?',abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.creat_all()
    click.echo('Initialized database.')

@app.cli.command()
@click.option('--count',default=20,help='Quantity of message,dafault is 20.')
def forge(count):
    '''Generate fake message.'''
    from faker import Faker
    db.drop_all()
    db.cerate_all()

    fake=Faker()
    click.echo('working....')

    for i in range(count):
        message=Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()

        )
        db.session.add(message)
    db.session.commit()
    click.echo('Created %d fake message.'% count)





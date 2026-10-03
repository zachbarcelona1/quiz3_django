from django.core.management.base import BaseCommand
from main.models import Student

SAMPLES = [
    ('Andrea Lim', 'Dre', 'Batangas City', 2, 'Web Development', 'Coding Club',
     'Ship it, then fix it.'),
    ('Rafael Cortez', 'Raf', 'Lipa City', 3, 'Database Systems', 'Esports Team',
     'Every bug is a lesson.'),
    ('Bianca Torres', 'Bia', 'Tanauan', 1, 'Graphic Design', 'Arts Guild',
     'Keep it simple.'),
    ('Dominic Pascual', 'Dom', 'Calamba', 4, 'Networking', 'Robotics Club',
     'Plug in, power up.'),
    ('Lara Mercado', 'Lars', 'San Pablo', 2, 'Mobile Apps', 'Debate Society',
     'Small steps, big builds.'),
]


class Command(BaseCommand):
    help = 'Adds sample student records (safe to run more than once).'

    def handle(self, *args, **kwargs):
        for name, nick, town, year, subject, club, motto in SAMPLES:
            _, created = Student.objects.get_or_create(
                name=name,
                defaults=dict(nickname=nick, hometown=town, year_level=year,
                              favorite_subject=subject, club=club, motto=motto),
            )
            self.stdout.write(('Added ' if created else 'Exists ') + name)
